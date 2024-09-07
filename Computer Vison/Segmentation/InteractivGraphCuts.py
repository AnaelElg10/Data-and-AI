import cv2
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def build_graph(image, foreground, background):

    G = nx.Graph() # Create a graph
    height, width = image.shape[:2]
    source, sink = 'source', 'sink' # Define source and sink nodes
    G.add_node(source) # Add source node
    G.add_node(sink) # Add sink node

    # Add nodes
    for y in range(height):
        for x in range(width):
            pixel_node = (x, y)
            G.add_node(pixel_node)

    # Add edges
    for y in range(height):
        for x in range(width):
            pixel_node = (x, y)
            intensity = image[y, x]

            # Define neighboring pixels
            neighbors = [(x - 1, y), (x, y - 1), (x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1), (x + 1, y + 1), (x + 1, y), (x, y + 1)]

            # Add weight to edges between neighboring pixels
            for neighbor in neighbors:
                nx1, ny = neighbor
                if 0 <= nx1 < width and 0 <= ny < height:
                    neighbor_intensity = image[ny, nx1]
                    diff = intensity - neighbor_intensity
                    clipped_diff = np.clip(diff, -10, 10)
                    weight = np.exp(-abs(clipped_diff))
                    G.add_edge(neighbor, pixel_node, capacity=weight)

    return G

def apply_graph_cut(G, source, sink): # Apply graph cut to the graph
    flow_value, partitions = nx.minimum_cut(G, source, sink) # Find the minimum cut of the graph
    reachable, non_reachable = partitions # Split the graph into reachable and non-reachable nodes
    return reachable # Return the reachable nodes

def extract_segmentation(reachable, image_shape): # Extract the segmentation from the reachable nodes
    mask = np.zeros(image_shape[:2], dtype=np.uint8)
    for node in reachable:
        if node != 'source':
            x, y = node
            mask[y, x] = 1
    return mask



# Example usage
image_path = "images/carton.jpg"
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
foreground = [(50, 60), (70, 80)]  # Replace with actual foreground seed coordinates
background = [(10, 20), (30, 40)]  # Replace with actual background seed coordinates

G = build_graph(image, foreground, background)
print("Graph built")
reachable = apply_graph_cut(G, 'source', 'sink')
print("Graph cut applied")
mask = extract_segmentation(reachable, image.shape)
print("Segmentation extracted")

segmented_image = cv2.bitwise_and(image, image, mask=mask.astype(np.uint8) * 255)

# Convert the image to RGBA
image_rgba = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)

# Create a mask for the alpha channel
alpha = np.ones(mask.shape, dtype=np.uint8) * 255

# Set the alpha channel to be transparent where the mask is 0
alpha[mask == 0] = 0

# Replace the alpha channel in the image
image_rgba[:, :, 3] = alpha

# Display the image
image_rgba = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)

# Create a mask for the alpha channel
alpha = np.ones(mask.shape, dtype=np.uint8) * 255

# Set the alpha channel to be transparent where the mask is 0
alpha[mask == 0] = 0

# Replace the alpha channel in the image
image_rgba[:, :, 3] = alpha

# Display the images sie by side
plt.figure(figsize=(20, 10))
plt.subplot(1, 2, 1)
plt.imshow(image_rgba)
plt.title('Original Image')
plt.subplot(1, 2, 2)
plt.imshow(segmented_image)
plt.title('Segmented Image')
plt.show()

# Save the segmented image
cv2.imwrite('images/segmented_image.png', segmented_image)

# Save the image with alpha channel
cv2.imwrite('images/segmented_image_alpha.png', image_rgba)

# Save the mask
cv2.imwrite('images/mask.png', mask * 255)
