import sys
from PIL import Image
from io import BytesIO
<<<<<<< Updated upstream
import numpy as np
=======
import pytesseract
>>>>>>> Stashed changes

def process_image(input):
    """
    process an image file or image data using OCR and return the extracted text.

    Args:
        input (str or bytes): the image file path or the raw image data as bytes.

    Returns:
        str: the extracted text.
    """
<<<<<<< Updated upstream
    reader = easyocr.Reader(['de'])

=======
>>>>>>> Stashed changes
    # determine if input is a file path or raw image data
    if isinstance(input, str):
        try:
            with open(input, 'rb') as file:
                image_data = file.read()
            input_format = 'file'
        except Exception as e:
            print(f"Error reading image from path {input}: {e}")
            return None
    elif isinstance(input, bytes):
        image_data = input
        input_format = 'bytes'
    else:
        raise TypeError("Input must be a file path or raw image data as bytes.")

    # try to process the image data
    try:
        # process image file (JPEG, PNG) or image data
        image = Image.open(BytesIO(image_data))
<<<<<<< Updated upstream
        image_np = np.array(image)  # convert PIL image to numpy array
        result = reader.readtext(image_np)
        text = '\n'.join([entry[1] for entry in result])
=======

        # perform OCR using pytesseract
        text = pytesseract.image_to_string(image, lang='deu')
        return text
>>>>>>> Stashed changes
    except Exception as e:
        print("Error processing image:", e)
        return None

<<<<<<< Updated upstream
    return text

=======
>>>>>>> Stashed changes
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python app/main.py <path_to_image>")
        sys.exit(1)

    input_path = sys.argv[1]
    extracted_text = process_image(input_path)

<<<<<<< Updated upstream
    if extracted_text is not None:
        print("Extracted text:")
        print(extracted_text)
    else:
        print("Failed to extract text from the image.")
=======
    if extracted_text:
        print("Extracted text:")
        print(extracted_text)
    else:
        print("Failed to extract text from the image.")
>>>>>>> Stashed changes
