import easyocr
from PIL import Image
from io import BytesIO
def process_image(input):
    """
    process an image file or image data using OCR and return the extracted text.
    Args:
        input (str or bytes): the image file path or the raw image data as bytes.
    Returns:
        str: the extracted text.
    """
    reader = easyocr.Reader(['de'])
    if isinstance(input, str):  # if input is a file path
        try:
            with open(input, 'rb') as file:
                image_data = file.read()
        except Exception as e:
            print(f"Error reading image from path {input}: {e}")
            return None
    elif isinstance(input, bytes):  # if input is raw image data
        image_data = input
    else:
        raise TypeError("Input must be a file path or raw image data as bytes.")
    try:
        # open image from bytes
        image = Image.open(BytesIO(image_data))
        result = reader.readtext(image)
    except Exception as e:
        print("Error processing image:", e)
        return None
    # Eetract and return the text
    text = '\n'.join([entry[1] for entry in result])
    return text