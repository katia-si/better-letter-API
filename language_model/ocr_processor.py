import os
import easyocr

def process_images(image_directory, output_directory):
    """
    Process all images in the specified directory using OCR and save the extracted text to text files.

    Args:
        image_directory (str): Path to the directory containing the image files.
        output_directory (str): Path to the directory where the output text files will be saved.
    """
    reader = easyocr.Reader(['de'])

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(image_directory):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.pdf')):
            image_path = os.path.join(image_directory, filename)
            try:
                with open(image_path, 'rb') as image_file:
                    image_bytes = image_file.read()
            except Exception as e:
                print(f"Error reading {filename}: {e}")
                continue

            try:
                result = reader.readtext(image_bytes)
            except Exception as e:
                print(f"Error processing {filename}: {e}")
                continue

            text = '\n'.join([entry[1] for entry in result])
            output_path = os.path.join(output_directory, f'{os.path.splitext(filename)[0]}.txt')

            if os.path.exists(output_path):
                print(f"Skipping {filename}. Output file {output_path} already exists.")
                continue

            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(text)

            print(f'Text from {filename} has been saved in: {output_path}.')
