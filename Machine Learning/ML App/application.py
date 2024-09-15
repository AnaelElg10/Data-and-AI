import gradio as gr
import tensorflow as tf

# Load the pre-trained model
model = tf.keras.models.load_model("mnist.h5")

def identify_digit(image):
    """
    Identify the digit in the given image using the pre-trained model.
    
    Args:
        image (numpy.ndarray): The input image of shape (28, 28).
    
    Returns:
        dict: A dictionary with digit predictions and their probabilities.
    """
    if image is not None:
        # Preprocess the image
        image = image.reshape((1, 28, 28, 1)).astype('float32') / 255
        
        # Predict the digit
        prediction = model.predict(image)
        
        # Return the prediction as a dictionary
        return {str(i): float(prediction[0][i]) for i in range(10)}
    else:
        return ''

# Create the Gradio interface
iface = gr.Interface(
    fn=identify_digit, 
    inputs=gr.Image(shape=(28, 28), image_mode='L', invert_colors=True, source='canvas'), 
    outputs=gr.Label(num_top_classes=5), 
    live=True
)

# Launch the interface
if __name__ == "__main__":
    iface.launch()