import tensorflow as tf
from tensorflow.keras import layers, models

def load_and_preprocess_data():
    """Load and preprocess the MNIST dataset."""
    (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()
    
    # Reshape and normalize the images
    train_images = train_images.reshape((60000, 28, 28, 1)).astype('float32') / 255
    test_images = test_images.reshape((10000, 28, 28, 1)).astype('float32') / 255
    
    # Convert labels to categorical format
    train_labels = tf.keras.utils.to_categorical(train_labels)
    test_labels = tf.keras.utils.to_categorical(test_labels)
    
    return (train_images, train_labels), (test_images, test_labels)

def build_model(input_shape):
    """Build and compile the CNN model."""
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(10, activation='softmax')
    ])
    
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

def train_model(model, train_images, train_labels):
    """Train the CNN model."""
    model.fit(train_images, train_labels, epochs=5, batch_size=64, validation_split=0.1)

def save_model(model, filename):
    """Save the trained model to a file."""
    model.save(filename)

def main():
    """Main function to execute the training pipeline."""
    (train_images, train_labels), (test_images, test_labels) = load_and_preprocess_data()
    model = build_model(input_shape=(28, 28, 1))
    train_model(model, train_images, train_labels)
    save_model(model, 'mnist.h5')

if __name__ == "__main__":
    main()