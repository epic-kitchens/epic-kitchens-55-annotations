import os
import sys
import argparse
import pandas as pd
from pathlib import Path


def test_files(pkl_paths, csv_paths, commit_hash, version_number):
    for i, p_file in enumerate(pkl_paths):
        c_file = csv_paths[i]
        csv = pd.read_csv(c_file)
        df = pd.read_pickle(p_file)
        assert df._metadata['commit_hash'] == commit_hash
        assert df._metadata['version_number'] == version_number
        assert len(csv) == len(df)
        csv_uid = set(csv.uid)
        df_uid = set(df.index)
        assert csv_uid == df_uid


def main(args):
    get_file_names = lambda L: {str(l).split('/')[-1].split('.')[0] for l in L}
    pickle_file_names = get_file_names(args.pickle_paths)
    csv_file_names = get_file_names(args.csv_paths)
    assert pickle_file_names == csv_file_names

    pickle_file_paths = sorted(list(args.pickle_paths))
    csv_file_paths = sorted(list(args.csv_paths))
    test_files(pickle_file_paths, csv_file_paths, args.commit_hash, args.version_number)


#git log --all --grep='skip' --max-count=1 | grep -oP 'pickles from* \K.*'
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Tests pickles can be read and the metadata exists')
    parser.add_argument('pickle_paths', type=Path, nargs='+',
            help='Pickle file containing pandas dataframe to add metadata to')
    parser.add_argument('--csv-paths', required=True, type=Path, nargs='+',
            help='Csv filepaths, should contain the same files as in the pickles')
    parser.add_argument('--commit-hash', type=str, 
            help='Commit hash metadata to store in pandas dataframe.')
    parser.add_argument('--version-number', type=str, 
            help='Version Number metadata to store in pandas dataframe.')

    args = parser.parse_args()
    main(args)
