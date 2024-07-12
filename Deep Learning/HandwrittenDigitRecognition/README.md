# Handwritten Digit Recognition with CNN

This project demonstrates the application of Convolutional Neural Networks (CNN) to recognize handwritten digits using the MNIST dataset. The MNIST dataset comprises 28x28 grayscale images of handwritten digits (0 to 9) along with their corresponding labels. It is divided into 60,000 training images and 10,000 test images.

## Project Structure

- `Main.ipynb`: The Jupyter notebook containing the entire project workflow, including data loading, model building, training, and evaluation.

## Getting Started

### Prerequisites

- Python 3.x
- Jupyter Notebook or JupyterLab
- PyTorch
- torchvision

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone [repository_url]
   ```

2. Navigate to the project directory:

   ```
   cd HandwrittenDigitRecognition
   ```

   This step is necessary to navigate to the project directory before installing the required Python packages.

3. Install the required Python packages:

   ```bash
   pip install torch torchvision matplotlib numpy jupyter
   ```

### Running the Project

Open the `Main.ipynb` notebook in Jupyter Notebook or JupyterLab or any other compatible environment.

for example, if you are using Jupyter Notebook, run the following command:

```bash
jupyter notebook Main.ipynb
```


Follow the instructions within the notebook to train and evaluate the model.

## Model Architecture

The project utilizes a Convolutional Neural Network (CNN) for the task of handwritten digit recognition. The CNN architecture is defined within the `Main.ipynb` notebook. It consists of convolutional layers followed by fully connected layers. The model is trained using the cross-entropy loss function and optimized using the Adam optimizer.

## Training

The model is trained on the MNIST dataset's training set, which consists of 60,000 images. The training process is detailed in the `Main.ipynb` notebook, including loading the dataset, defining the model architecture, setting the loss function and optimizer, and running the training loop.

## Evaluation

After training, the model is evaluated on the MNIST dataset's test set, which consists of 10,000 images. The evaluation metrics include the model's accuracy on the test set.

## Results

The trained model achieves an accuracy of approximately 96% on the MNIST test set. This demonstrates the effectiveness of CNNs in recognizing handwritten digits.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- The MNIST dataset, a fundamental benchmark in the field of machine learning.
- PyTorch, for providing an intuitive framework for building and training neural networks.