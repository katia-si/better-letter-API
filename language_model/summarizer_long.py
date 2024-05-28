from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import os

tokenizer = AutoTokenizer.from_pretrained("Shahm/bart-german")
model = AutoModelForSeq2SeqLM.from_pretrained("Shahm/bart-german")

def generate_summary_longer(text: str) -> str:
    inputs = tokenizer.encode(text, return_tensors="pt", truncation=True, max_length=1024)
    summary_ids = model.generate(
        inputs,
        max_length=400,
        min_length=150,
        length_penalty=2.0,
        num_beams=4,
        early_stopping=True
    )
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

def summarize_text(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        if filename.endswith('.txt'):
            input_file_path = os.path.join(input_directory, filename)
            output_file_path = os.path.join(output_directory, f'{os.path.splitext(filename)[0]}_sum.txt')

            if os.path.exists(output_file_path):
                print(f'Skipping {filename}. Output file {output_file_path} already exists.')
                continue

            with open(input_file_path, 'r', encoding='utf-8') as file:
                text = file.read()

            summary = generate_summary_longer(text)

            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(summary)

            print(f'Summary has been generated and saved to: {output_file_path}')
