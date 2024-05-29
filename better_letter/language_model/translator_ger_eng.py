from transformers import MarianMTModel, MarianTokenizer
import os

tokenizer_translate = MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-de-en")
model_translate = MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-de-en")

def translate_to_english(german_text):
    inputs = tokenizer_translate(german_text, return_tensors="pt", padding=True, truncation=True)
    translated = model_translate.generate(**inputs)
    translated_text = tokenizer_translate.batch_decode(translated, skip_special_tokens=True)
    return translated_text[0]

def translate_summaries(input_directory_german, output_directory_english):
    if not os.path.exists(output_directory_english):
        os.makedirs(output_directory_english)

    for filename in os.listdir(input_directory_german):
        if filename.endswith('.txt'):
            with open(os.path.join(input_directory_german, filename), 'r', encoding='utf-8') as file:
                german_summary = file.read()

            english_summary = translate_to_english(german_summary)

            output_file_path_english = os.path.join(output_directory_english, filename)

            with open(output_file_path_english, 'w', encoding='utf-8') as output_file:
                output_file.write(english_summary)

            print(f'Translated summary has been saved to: {output_file_path_english}')
