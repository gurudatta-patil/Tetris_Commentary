import cv2
import numpy as np

def detect_blocks(image):
    # Get the dimensions of the image
    height, width, _ = image.shape

    # Calculate the dimensions of each small image
    small_width = width // 10
    small_height = height // 20

    # Define the color range for the blocks
    block_color_range = ([100, 100, 100], [255, 255, 255])  # Not Black

    # Initialize the output string
    output = ''

    # Loop over the image
    for i in range(20):
        for j in range(10):
            # Get the small image
            small_image = image[i*small_height:(i+1)*small_height, j*small_width:(j+1)*small_width]
            
            # Calculate the average color of the small image
            avg_color = np.mean(small_image, axis=(0, 1))

            # Determine if a block is present based on the average color
            if any(block_color_range[0][k] <= avg_color[k] <= block_color_range[1][k] for k in range(3)):
                output += '/'
            else:
                output += '.'
        output += '\n'

    return output