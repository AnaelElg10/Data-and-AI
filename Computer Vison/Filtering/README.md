# Traffic Video Background Subtraction

This project demonstrates how to perform background subtraction on a traffic video using OpenCV in Python. The background subtraction is used to detect moving objects in the video.

## Requirements

- Python 3.x
- OpenCV

## Installation

1. Install Python from [python.org](https://www.python.org/).
2. Install OpenCV using pip:

    ```sh
    pip install opencv-python
    ```

## Usage

1. Place your video file (`TrafficJam.mp4`) in the same directory as `FilteringMain.py`.
2. Run the script:

    ```sh
    python FilteringMain.py
    ```

3. The script will open a window displaying the mask of the moving objects. Press 'q' or close the window to exit.

## Code Explanation

- The script loads a video file using `cv.VideoCapture`.
- It checks if the video file is opened successfully.
- A background subtractor is created using `cv.createBackgroundSubtractorMOG2`.
- The script reads frames from the video in a loop and applies the background subtractor to get the mask of moving objects.
- The mask is displayed in a window.
- The script exits when 'q' is pressed or the window is closed.
- Resources are released properly at the end.

## License

This project is licensed under the MIT License.