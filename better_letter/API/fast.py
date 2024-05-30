
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from better_letter.language_model.translator_ger_eng import translate_to_english
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
    translated_text = translate_to_english(german_text)
    return {"translated_text": translated_text}

@app.post("/summary_eng")
async def process(file: UploadFile):
    contents = await file.read()
    image = Image.open(BytesIO(contents)).convert("L")
