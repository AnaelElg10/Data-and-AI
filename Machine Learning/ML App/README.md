# MNIST Digit Recognition App

This project involves training a Convolutional Neural Network (CNN) to recognize handwritten digits from the MNIST dataset and providing an interactive interface for digit recognition using Gradio.

## Directory Structure

```
ML App/ application.py README.md training.py mnist.h5
```

## Files

- **application.py**: Script to run a Gradio interface for digit recognition.
- **training.py**: Script to train the CNN model on the MNIST dataset.
- **mnist.h5**: Pre-trained model file.
- **README.md**: Documentation for the MNIST Digit Recognition project.

## Usage

### Training the Model

1. **Open the Project**: Open the project in Visual Studio Code.
2. **Run the Training Script**: Execute the [`training.py`]script to train the model.
   ```sh
   python training.py
   ```
3. **Save the Model**: The trained model will be saved as `mnist.h5`.

### Running the Application

1. **Run the Application Script**: Execute the [`application.py`] script to run the Gradio interface.
   ```sh
   python application.py
   ```
2. **Open the Link**: Open the link displayed in the terminal to view the interface.
3. **Draw and Recognize Digits**: Use the interface to draw digits and view the model predictions.


## Code Overview

- ``application.py``: Contains code to create the Gradio interface for digit recognition.

- ``training.py``: Contains code to load the MNIST dataset, preprocess the data, train the CNN model, and save the model.


## Technologies Used

- Programming Language: Python
- Libraries: TensorFlow, Gradio
- Dataset: MNIST


## Conclusion

This project demonstrates how to train a CNN model on the MNIST dataset and create an interactive interface for digit recognition using Gradio.

```python
print("Thank you!")
```
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.