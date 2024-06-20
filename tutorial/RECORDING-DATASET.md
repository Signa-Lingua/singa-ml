## Dataset Recording Instructions for Singa (Sign Language Recognition)

This document provides detailed instructions on how to record your own dataset using the `slr_collecting_data.ipynb` Jupyter notebook. This is essential for creating and customizing a dataset for training the sign language recognition model in the Singa project.

### How to Record Your Own Dataset

1. Running the Notebook:
    - Open and run the Jupyter notebook file `slr_collecting_data.ipynb`.

2. Adjusting Parameters:
    - Videos per Label: You can change the number of videos per label/action by adjusting the `videos_per_label` variable. The default value is `60`.
    - Frames per Video: You can change the number of frames per video by adjusting the `frames_per_video` variable. The default value is `60`.

3. Using Mediapipe TaskVision:
    - For more information on how to use Mediapipe TaskVision, refer to the following resources:
        - [`Hand Landmarker Options`](https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker)
        - [`Pose Landmarker Options`](https://ai.google.dev/edge/mediapipe/solutions/vision/pose_landmarker)


### Recording Session Details

- Video Capture:
    - The script will capture the specified number of videos (60 by default) per label action.
    - Each video will consist of `60 frames by default`.
    - There will be a pause of approximately `1.5 seconds` between each video capture to allow the actor to adjust for the next video.

- Debugging:
    - For debugging purposes, you can set `debug_landmark=True` to visualize the keypoints detected by Mediapipe TaskVision. This helps the actor verify if their sign actions are being detected properly.

- Exiting the Recording Session:
    - To quit the recording session, press `q` on the keyboard.

By following these instructions, you can efficiently record and customize your dataset for training the sign language recognition model. Ensure that the parameters are set according to your requirements and refer to the Mediapipe documentation for additional customization options.
