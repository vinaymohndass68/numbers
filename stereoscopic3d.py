import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy.ndimage import gaussian_filter

def create_depth_map(text, width, height):
    # Create a blank depth map
    depth_map = np.zeros((height, width), dtype=np.uint8)

    # Add text as depth
    image = Image.fromarray(depth_map)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", size=100)

    # Calculate text size and position using textbbox
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2

    # Draw the text onto the depth map
    draw.text((text_x, text_y), text, fill=255, font=font)

    # Apply Gaussian blur to smooth edges (optional)
    depth_map = np.array(image)
    depth_map = gaussian_filter(depth_map, sigma=3)
    return depth_map

def generate_stereogram(depth_map):
    height, width = depth_map.shape
    stereogram = np.random.randint(0, 255, (height, width), dtype=np.uint8)

    # Generate stereogram
    for y in range(height):
        for x in range(width):
            shift = depth_map[y, x] // 10  # Increase scale for more disparity
            if x - shift >= 0:
                stereogram[y, x] = stereogram[y, x - shift]

    return stereogram

# Settings
width, height = 800, 600
text = "VINAY"

# Create depth map
depth_map = create_depth_map(text, width, height)

# Save and visualize depth map (for debugging)
depth_map_image = Image.fromarray(depth_map)
depth_map_image.save("depth_map_vinay.png")
depth_map_image.show()  # Optional: Check if text is visible here

# Generate stereogram
stereogram = generate_stereogram(depth_map)

# Save stereogram
stereogram_image = Image.fromarray(stereogram)
stereogram_image.save("stereogram_vinay.png")
stereogram_image.show()
