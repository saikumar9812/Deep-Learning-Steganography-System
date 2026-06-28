from PIL import Image

def center_image_on_a4(input_image_path, output_image_path='output.jpg'):
    # Open the input image
    input_image = Image.open(input_image_path)

    # Create a blank A4 size sheet
    a4_width = 768
    a4_height = 1024
    a4_sheet = Image.new('RGB', (a4_width, a4_height), color='white')

    # Calculate position to center the input image on the A4 sheet
    x_offset = (a4_width - input_image.width) // 2
    y_offset = (a4_height - input_image.height) // 2

    # Paste the input image onto the A4 sheet at the centered position
    a4_sheet.paste(input_image, (x_offset, y_offset))

    # Save the resulting image
    a4_sheet.save(output_image_path)

# Example usage:
input_image_path = 'out/merged.png'  # Change this to your input image path
output_image_path = 'out/output.png'  # Change this to the desired output image path
center_image_on_a4(input_image_path, output_image_path)