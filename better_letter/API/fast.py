from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from better_letter.language_model.translator_ger_eng import translate_to_english_and_print
from better_letter.language_model.ocr_processor import process_image
from better_letter.language_model.summarizer_long import generate_summary_dynamic
from better_letter.language_model.text_cleaner import clean_extracted_text

app = FastAPI()

#app.state.model = load_model()

# allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # allows all methods
    allow_headers=["*"],  # allows all headers
)
@app.get("/")
def root():
    return {'better': 'letter'}

@app.post("/summary_eng")
async def german_summary(file: UploadFile):
    contents = await file.read()
    ocr_output_text = process_image(contents)
    if not ocr_output_text:
        return {"error": "Failed to extract text from the image."}
    # clean the extracted text
    cleaned_text = clean_extracted_text(ocr_output_text)
    # summarize the cleaned text
    summarized_text = generate_summary_dynamic(cleaned_text)
    # translate to english
    translated_eng_summary_text = translate_to_english_and_print(summarized_text)
    return {"summary": translated_eng_summary_text}
