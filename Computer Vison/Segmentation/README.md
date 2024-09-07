# Interactive Graph Cuts for Image Segmentation

This project implements an interactive graph cut method for image segmentation, based on the paper "Interactive Graph Cuts for Optimal Boundary & Region Segmentation of Objects in N-D Images" by Yuri Boykov and Marie-Pierre Jolly.

## Requirements

- Python 3.x
- NumPy
- OpenCV
- NetworkX
- Matplotlib

## Installation

1. Install Python from [python.org](https://www.python.org/).
2. Install the required libraries using pip:

    ```sh
    pip install numpy opencv-python networkx matplotlib
    ```

## Usage

1. Place your image file in the `images` directory.
2. Modify the `image_path` variable in `InteractivGraphCuts.py` to point to your image file.
3. Run the script:

    ```sh
    python Segmentation/InteractivGraphCuts.py
    ```

## Code Explanation

- The script reads an image and constructs a graph where each pixel is a node.
- It adds edges between neighboring pixels with weights based on the intensity difference.
- The source and sink nodes are connected to the foreground and background pixels, respectively.
- The `build_graph` function constructs the graph.
- The `apply_graph_cut` function applies the graph cut algorithm to segment the image.
- The `extract_segmentation` function extracts the segmentation mask from the graph cut result.

## Example

Here is an example of how to use the script:

1. Place an image named `example.jpg` in the `images` directory.
2. Modify the `image_path` variable in `InteractivGraphCuts.py`:

    ```python
    image_path = 'images/example.jpg'
    ```

3. Run the script:

    ```sh
    python Segmentation/InteractivGraphCuts.py
    ```

4. The script will display the segmented image.

## License

This project is licensed under the MIT License.