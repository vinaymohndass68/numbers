from PIL import Image, ImageDraw, ImageFont

def create_stereographic_text(text, font_path=None, font_size=100, shift=10, output_file="stereographic_vinay.png"):
    # Step 1: Set up parameters
    width, height = 600, 300  # Canvas size
    bg_color = "white"        # Background color
    text_color = "black"      # Text color
    
    # Step 2: Try loading the font
    try:
        if font_path:
            font = ImageFont.truetype(font_path, font_size)
        else:
            raise OSError("Custom font path not provided.")
    except OSError:
        print("Warning: Could not load custom font. Using default font.")
        font = ImageFont.load_default()
    
    # Step 3: Create left and right images
    canvas_left = Image.new("RGB", (width, height), bg_color)
    canvas_right = Image.new("RGB", (width, height), bg_color)
    draw_left = ImageDraw.Draw(canvas_left)
    draw_right = ImageDraw.Draw(canvas_right)
    
    # Calculate text size using getbbox
    text_bbox = font.getbbox(text)  # Returns (x_min, y_min, x_max, y_max)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2
    
    # Draw text shifted slightly for left and right views
    draw_left.text((text_x - shift, text_y), text, font=font, fill=text_color)
    draw_right.text((text_x + shift, text_y), text, font=font, fill=text_color)
    
    # Step 4: Combine the two images side by side
    combined_width = width * 2
    combined_image = Image.new("RGB", (combined_width, height), bg_color)
    combined_image.paste(canvas_right, (0, 0))  # Right-eye view on the left
    combined_image.paste(canvas_left, (width, 0))  # Left-eye view on the right
    
    # Step 5: Save the image
    combined_image.save(output_file)
    print(f"Stereographic 3D image saved to {output_file}")

# Usage
create_stereographic_text(
    text= input("Enter the text: "),
    font_path="C:\\Windows\\Fonts\\Arial.ttf",  # Update this to a valid font path
    font_size=100,
    shift=10,
    output_file="stereographic_vinay.png"
)