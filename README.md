# EPIC Kitchens Dataset
Initial Release, April 2018

[Website]()

## Authors
Dima Damen (1)
Hazel Doughty (1)
Sanja Fidler (2)
Antonino Furnari (3)
Evangelos Kazakos (1)
Giovanni Maria Farinella (3)
Davide Moltisanti (1)
Jonathan Munro (1)
Toby Perrett (1)
Will Price (1)
Michael Wray (1)

* (1 University of Bristol)
* (2 University of Toronto)
* (3 University of Catania)

**Contact:** dima.damen@bristol.ac.uk


## Citing
When using the dataset, kindly reference:

> BibTex of 
> Arxiv dataset 
> paper

## Dataset Details

### Ground Truth
We provide ground truth for action segments and object bounding boxes.

* **Objects:** Full bounding boxes for every annotated frame.
* **Actions:** Split into weak and strong labels:
    * Weak labels containing the narrated sentence with the timestamp.
    * Strong labels containing the verb and noun labels along with the start and end times of the segment.

### Dataset Splits
The dataset is comprised of three splits with the corresponding ground truth:

* Training set - Full ground truth.
* Test set - Weak action labels only.

Initially we are only releasing the full ground truth for the training set in order to run action and object challenges.


### Important Files
* `README.md (this file)`
* `license.txt`
* `EPIC.zip`:
    * `EPIC_train_action_weak.csv`
    * `EPIC_train_action_strong.csv`
    * `EPIC_train_action_strong.pkl`
    * `EPIC_train_object.csv`
    * `EPIC_S1_weak.csv`
    * `EPIC_S2_weak.csv`

We direct the reader to [RSDF]() for the videos and rgb/flow frames.

## Files Structure
### EPIC_train_action_weak.csv
Csv file containing n columns:

* Col 1
* Col 2
* ...

### EPIC_train_action_strong.csv
Csv file containing n columns:

* Col 1
* Col 2
* ...

Please note we have included a python pickle file for ease of use. This includes
a pandas dataframe with the same layout as above.

### EPIC_train_object.csv
Csv file containing n columns:

* Col 1
* Col 2
* ...

## Video Information
Videos are recorded in 1080p at 59.94 FPS on a GoPro Hero 5 with linear field of
view. There are a minority of videos which were shot at different resolutions,
field of views, or FPS due to participant error or camera. These videos
identified using `ffprobe` are:

* 1280x720: `P12_01`, `P12_02`, `P12_03`, `P12_04`.
* 2560x1440: `P12_05`, `P12_06` 
* 29.97 FPS: `P09_07`, `P09_08`, `P10_01`, `P10_04`, `P11_01`, `P18_02`,
    `P18_03`
* 48 FPS: `P17_01`, `P17_02`, `P17_03`, `P17_04`
* 90 FPS: `P18_09`

The GoPro Hero 5 was also set to drop the framerate in low light conditions to
preserve exposure leading to variable FPS in some videos.  If you wish to
extract frames we suggest you resample at 60 FPS to mitigate issues with
variable FPS, this can be achieved in a single step with FFmpeg: 

```
ffmpeg -i 'P##_**.MP4' -vf 'scale=-2:256' -q:v 4 -r 60 'P##_**/frame_%010d.jpg'
```

Optical flow was extracted using a fork of
[`gpu_flow`](https://github.com/feichtenhofer/gpu_flow) made 
[available on github](https://github.com/dl-container-registry/furnari-flow).
 We set the parameters: stride = 2, dilation = 3, bound = 25 and size = 256.

Please go [here]() if you wish to download the videos/frames.

## License
All files in this dataset are copyright by us and published under the 
Creative Commons Attribution-NonCommerial 4.0 International License, found 
[here](https://creativecommons.org/licenses/by-nc/4.0/).
This means that you must give appropriate credit, provide a link to the license,
and indicate if changes were made. You may do so in any reasonable manner,
but not in any way that suggests the licensor endorses you or your use. You
may not use the material for commercial purposes.

## Changelog
* 01/04/18: Initial Release
