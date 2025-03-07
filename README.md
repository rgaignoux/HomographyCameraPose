# Camera Pose Estimation

## Overview

This project estimates the camera pose in a video recorded with a smartphone. The method involves:
- **Camera Calibration**: Computing the intrinsic parameters using a calibration pattern.
- **Pose Estimation**: Using homographies and keypoint matching to track the camera pose across frames.
- **3D Visualization**: Drawing the world coordinate axes on each frame of the video.

## Video Result

![Alt Text](https://github.com/rgaignoux/HomographyCameraPose/blob/main/result.gif)

## Methodology

### 1. Camera Calibration
We calibrate the smartphone camera using OpenCV's calibration functions. The intrinsic matrix **K** is obtained by capturing multiple images of a checkerboard pattern from different angles.

### 2. Pose Estimation for Frame 0
- Select 4 known points on a planar object in the image.
- Define their 3D coordinates in the world frame (assuming Z=0).
- Compute the **homography** between the world and image coordinates using the **Direct Linear Transform (DLT)** method (`cv2.findHomography()`).
- Extract the extrinsic parameters **[R|t]** (rotation and translation) by decomposing the homography matrix.
- Normalize the vectors to ensure a valid rotation matrix.

### 3. Pose Estimation for Frame k
- Detect and match **SIFT keypoints** between consecutive frames.
- Compute the homography **H(k-1 → k)** between frame **k-1** and frame **k**.
- Chain transformations to get **H(W → k)**, relating the world frame to frame **k**.
- Extract the new pose **[R|t]** for frame **k**.
- Project the world coordinate axes into the image.

### 4. Iterative Process
This process is repeated for each frame, providing a continuous estimation of the camera pose throughout the video.
