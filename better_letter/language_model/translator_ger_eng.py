from transformers import MarianMTModel, MarianTokenizer
import os

# initialize the tokenizer and model for translation
tokenizer_translate = MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-de-en")
model_translate = MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-de-en")

def translate_to_english_and_print(german_text):
    """
    translates german text to english using a pre-trained MarianMT model and prints the translation.

    Args:
        german_text (str):  german text to translate.

    Returns:
        str:  translated english text.
    """
    inputs = tokenizer_translate(german_text, return_tensors="pt", padding=True, truncation=True)
    translated = model_translate.generate(**inputs)
    translated_text = tokenizer_translate.batch_decode(translated, skip_special_tokens=True)[0]

    # print("Translated text:")
    # print(translated_text)

    return translated_text




################################################################################
### OLD: this part translate the text and then safe the ouput locally
################################################################################

# om transformers import MarianMTModel, MarianTokenizer
# port os
#
# Initialize the tokenizer and model for translation
# kenizer_translate = MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-de-en")
# del_translate = MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-de-en")
#
# f translate_to_english(german_text):
#   """
#   Translates German text to English using a pre-trained MarianMT model.
#
#   Args:
#       german_text (str): The German text to translate.
#
#   Returns:
#       str: The translated English text.
#   """
#   inputs = tokenizer_translate(german_text, return_tensors="pt", padding=True, truncation=True)
#   translated = model_translate.generate(**inputs)
#   translated_text = tokenizer_translate.batch_decode(translated, skip_special_tokens=True)
#   return translated_text[0]
#
# f translate_summaries(input_directory_german, output_directory_english):
#   """
#   Translates German summary text files to English and saves them to the specified output directory.
#
#   Args:
#       input_directory_german (str): Path to the directory containing the German summary text files.
#       output_directory_english (str): Path to the directory where translated English summary text files will be saved.
#   """
#   if not os.path.exists(output_directory_english):
#       os.makedirs(output_directory_english)
#
#   for filename in os.listdir(input_directory_german):
#       if filename.endswith('.txt'):
#           with open(os.path.join(input_directory_german, filename), 'r', encoding='utf-8') as file:
#               german_summary = file.read()
#
#           english_summary = translate_to_english(german_summary)
#
#           output_file_path_english = os.path.join(output_directory_english, filename)
#
#           with open(output_file_path_english, 'w', encoding='utf-8') as output_file:
#               output_file.write(english_summary)
#
#           print(f'Translated summary has been saved to: {output_file_path_english}')
#
