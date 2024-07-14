from PIL import Image, ImageFilter

def add_blur_effect(image_path, output_path):
    original = Image.open(image_path)
    blurred = original.filter(ImageFilter.GaussianBlur(5))
    blurred.save(output_path)

add_blur_effect('input_image.png', 'output_image_with_blur.png')
