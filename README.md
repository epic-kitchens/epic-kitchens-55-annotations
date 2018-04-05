# EPIC Kitchens Dataset
Initial Release, April 2018

[Website](https://epic-kitchens.github.io/)

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

**Contact:** uob-epic-kitchens2018@bristol.ac.uk


## Citing
When using the dataset, kindly reference:

> BibTex of 
> Arxiv dataset 
> paper

## Dataset Details

### Ground Truth
We provide ground truth for action segments and object bounding boxes.

* **Objects:** Full bounding boxes of narrated objects for every annotated frame.
* **Actions:** Split into narrations and action labels:
    * Narrations containing the narrated sentence with the timestamp.
    * Action labels containing the verb and noun labels along with the start and end times of the segment.

### Dataset Splits
The dataset is comprised of three splits with the corresponding ground truth:

* Training set - Full ground truth.
* Test set - Timestamp and start/end times only.

Initially we are only releasing the full ground truth for the training set in order to run action and object challenges.


### Important Files
(click links to see information of each file)

* `README.md (this file)`
* [`license.txt`](#license)
* [`EPIC_train_action_narrations.csv`](#epic_train_action_narrationscsv)
* [`EPIC_train_action_labels.csv`](#epic_train_action_labelscsv)
* [`EPIC_train_action_labels.pkl`](#epic_train_action_labelscsv)
* [`EPIC_train_object_labels.csv`](#epic_train_object_labelscsv)
* [`EPIC_test_s1_timestamps.csv`](#epic_test_s1_timestampscsv)
* [`EPIC_test_s2_timestamps.csv`](#epic_test_s2_timestampscsv)

We direct the reader to [RDSF]() for the videos and rgb/flow frames.

## Files Structure
### EPIC_train_action_narrations.csv
CSV file containing 5 columns:

| Column Name       | Type   | Example        | Description                                                    |
| ----------------- | ------ |--------------- | -------------------------------------------------------------- |
| `participant_id`  | string | `'P03'`        | ID of the participant.                                         |
| `video_id`        | string | `'P03_01'`     | Video the segment is in.                                       |
| `start_timestamp` | string | `00:23:43.847` | Start time in `HH:mm:ss.SSS` of the action.                    |
| `stop_timestamp`  | string | `00:23:47.212` | End time in `HH:mm:ss.SSS` of the action.                      |
| `narration`       | string | `close fridge` | English description of the action provided by the participant. |

### EPIC_train_action_labels.csv
CSV file containing 14 columns:

| Column Name         | Type                         | Example                      | Description                                                                                                           |
| ------------------- | ---------------------------- | ---------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `uid`               | int                          | `6374`                       | Unique ID of the segment.                                                                                             |
| `video_id`          | string                       | `'P03_01'`                   | Video the segment is in.                                                                                              |
| `narration`         | string                       | `'close fridge'`             | English description of the action provided by the participant.                                                        |
| `start_timestamp`   | string                       | `'00:23:43.847'`             | Start time in `HH:mm:ss.SSS` of the action.                                                                           |
| `stop_timestamp`    | string                       | `'00:23:47.212'`             | End time in `HH:mm:ss.SSS` of the action.                                                                             |
| `start_frame`       | int                          | `85430`                      | Start frame of the action (WARNING only for frames extracted as detailed in [Video Information](#video-information).  |
| `stop_frame`        | int                          | `85643`                      | End frame of the action (WARNING only for frames  extracted as detailed in [Video Information](#video-information).   |
| `participant_id`    | string                       | `'P03'`                      | ID of the participant.                                                                                                |
| `verb`              | string                       | `'close'`                    | Parsed verb from the narration.                                                                                       |
| `noun`              | string                       | `'fridge'`                   | First parsed noun from the narration.                                                                                 |
| `verb_class`        | int                          | `3`                          | Numeric ID of the parsed verb's class.                                                                                |
| `noun_class`        | int                          | `10`                         | Numeric ID of the parsed noun's class.                                                                                |
| `all_nouns`         | list of string (1 or more)   | `['fridge']`                 | List of all parsed nouns from the narration.                                                                          |
| `all_nouns_class`   | list of int    (1 or more)   | `[10]`                       | List of numeric IDs corresponding to all of the parsed nouns' classes from the narration.                             |

Please note we have included a python pickle file for ease of use. This includes
a pandas dataframe with the same layout as above.

### EPIC_train_object_labels.csv
CSV file containing 6 columns:

| Column Name      | Type                        | Description                                                                   |
|------------------|-----------------------------|-------------------------------------------------------------------------------|
| `noun_class`     | int                         | Integer value representing the class in noun-classes.csv.                     |
| `noun`           | string                      | Original string name for the object.                                          |
| `participant_id` | string                      | ID of participant.                                                            |
| `video_id`       | string                      | Video the object was annotated in.                                            |
| `frame`          | int                         | Frame number of the annotated object.                                         |
| `bounding_boxes` | list of 4-tuple (0 or more) | Annotated boxes with format `(<top:int>,<left:int>,<width:int>,<height:int>)`.|

### EPIC_test_s1_timestamps.csv
CSV file containing 4 columns:

| Column Name       | Type   | Example        | Description                                                    |
| ----------------- | ------ |--------------- | -------------------------------------------------------------- |
| `participant_id`  | string | `'P03'`        | ID of the participant.                                         |
| `video_id`        | string | `'P03_01'`     | Video the segment is in.                                       |
| `start_timestamp` | string | `00:23:43.847` | Start time in `HH:mm:ss.SSS` of the action.                    |
| `stop_timestamp`  | string | `00:23:47.212` | End time in `HH:mm:ss.SSS` of the action.                      |

### EPIC_test_s2_timestamps.csv
CSV file containing 4 columns:

| Column Name       | Type   | Example        | Description                                                    |
| ----------------- | ------ |--------------- | -------------------------------------------------------------- |
| `participant_id`  | string | `'P03'`        | ID of the participant.                                         |
| `video_id`        | string | `'P03_01'`     | Video the segment is in.                                       |
| `start_timestamp` | string | `00:23:43.847` | Start time in `HH:mm:ss.SSS` of the action.                    |
| `stop_timestamp`  | string | `00:23:47.212` | End time in `HH:mm:ss.SSS` of the action.                      |



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
