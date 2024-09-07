# Computer Vision Projects

This repository contains different projects focusing on different aspects of computer vision and image processing using Python.

## Projects

### 1. Filtering
- **Description**: This project demonstrates how to perform background subtraction on a traffic video using OpenCV. The background subtraction technique is used to detect moving objects in the video.
- **Main Script**: `Filtering/FilteringMain.py`
- **Usage**:
  1. Place a video file named `TrafficJam.mp4` in the same directory as the script.
  2. Run the script to see the moving objects highlighted in the video.

### 2. Number Plate Recognition
- **Description**: This project focuses on Automatic Number Plate Recognition (ANPR) using image processing techniques. It includes a Jupyter notebook that processes images to detect and read number plates.
- **Main Notebook**: `NumberPlateRecognition/ANPR.ipynb`
- **Usage**:
  1. Open the notebook.
  2. Follow the steps to process images and recognize number plates.

### 3. Segmentation
- **Description**: This project implements an interactive graph cut method for image segmentation, based on a well-known research paper. It allows users to segment objects in images by constructing and cutting a graph.
- **Main Script**: `Segmentation/InteractivGraphCuts.py`
- **Usage**:
  1. Place an image in the `images` directory.
  2. Modify the script to point to the image.
  3. Run the script to see the segmented result.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/computer-vision-projects.git
   cd computer-vision-projects
    ```
2. Install the required libraries:
    ```sh
    pip install opencv-python numpy matplotlib scikit-image scikit-learn jupyter
    ```

## License

This repository is licensed under the MIT License. See `LICENSE` for more information.
```
