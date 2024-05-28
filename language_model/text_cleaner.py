import os
import re

def clean_extracted_text(text):
    text = re.sub(r'(\w+)-\n(\w+)', r'\1\2', text)
    text = text.replace('\n', ' ')
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def clean_and_save_files(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        if filename.endswith('.txt'):
            input_file_path = os.path.join(input_directory, filename)
            output_file_path = os.path.join(output_directory, filename.replace('.txt', '_cldn.txt'))

            if os.path.exists(output_file_path):
                print(f"Skipping {filename}. Output file {output_file_path} already exists.")
                continue

            with open(input_file_path, 'r', encoding='utf-8') as file:
                extracted_text = file.read()

            cleaned_text = clean_extracted_text(extracted_text)

            with open(output_file_path, 'w', encoding='utf-8') as file:
                file.write(cleaned_text)

            print(f'Cleaned text has been saved to: {output_file_path}')
