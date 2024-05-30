
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from better_letter.language_model.translator_ger_eng import translate_to_english_and_print
from better_letter.language_model.ocr_processor import process_image
from better_letter.language_model.summarizer_long import generate_summary_dynamic
from better_letter.language_model.text_cleaner import clean_extracted_text
from fastapi import FastAPI, UploadFile
from PIL import Image
from io import BytesIO

app = FastAPI()

# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def root():
    return {
    'better': 'letter'
}

@app.get("/translate")
def translate_text(german_text: str):
    translated_text = translate_to_english_and_print(german_text)
    return {"translated_text": translated_text}

@app.post("/summary_eng")
async def process(file: UploadFile):
    contents = await file.read()
    image = Image.open(BytesIO(contents)).convert("L")
    ocr_output_text = process_image(image)
    if not ocr_output_text:
        print("error: failed to extract text from the image.")
        return

    # step 2: clean the extracted text
    cleaned_text = clean_extracted_text(ocr_output_text)

    # step 3: summarize the cleaned text
    summarized_text = generate_summary_dynamic(cleaned_text)

    # step 4: translate the summaries to english
    translated_text = translate_to_english_and_print(summarized_text)
    
    return {"Summary":translated_text}
