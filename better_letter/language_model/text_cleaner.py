import os
import re

def clean_extracted_text(text):
    """
    cleans the extracted text by removing hyphens at line breaks, newlines,
    extra spaces, and text inside brackets. Also processes specific markers
    and removes unnecessary parts.

    Args:
        text (str): the extracted text to be cleaned.

    returns:
        str: the cleaned text.
    """
    text = re.sub(r'(\w+)-\n(\w+)', r'\1\2', text)  # remove hyphens at line breaks
    text = text.replace('\n', ' ')  # replace newlines with spaces
    text = re.sub(r'\s+', ' ', text).strip()  # remove extra spaces
    text = re.sub(r';', ',', text)  # replace semicolons with commas
    text = re.sub(r':', '.', text)  # replace colons with periods

    # remove text inside curly or other brackets
    text = re.sub(r'\{.*?\}', '', text)
    text = re.sub(r'\(.*?\)', '', text)
    text = re.sub(r'\[.*?\]', '', text)

    # find the index of the first occurrence of "Datum:" and remove text before it
    datum_index = text.find("Datum:")
    if datum_index != -1:
        text = text[datum_index+len("Datum:"):]

    # remove text before "Sehr geehrt" followed by any characters
    sehr_geehrt_index = re.search(r'Sehr geehrt.*', text, flags=re.IGNORECASE)
    if sehr_geehrt_index:
        text = text[sehr_geehrt_index.start():]

    # find the index of "Berliner Sparkasse" and remove everything after it
    berliner_sparkasse_index = text.find("Berliner Sparkasse")
    if berliner_sparkasse_index != -1:
        text = text[:berliner_sparkasse_index]

    # print("Cleaned text:")
    # print(text)
    return text

def clean_extracted_text_and_print(text):
    """
    Cleans the extracted text and prints the cleaned text.

    Args:
        text (str): The extracted text to be cleaned.
    """
    cleaned_text = clean_extracted_text(text)
    return cleaned_text








################################################################################
### OLD: this part cleans the text and then safe the ouput locally
################################################################################


# import os
# import re
#
# def clean_extracted_text(text):
#     """
#     Cleans the extracted text by removing hyphens at line breaks, newlines,
#     extra spaces, and text inside brackets. Also processes specific markers
#     and removes unnecessary parts.
#
#     Args:
#         text (str): The extracted text to be cleaned.
#
#     Returns:
#         str: The cleaned text.
#     """
#     text = re.sub(r'(\w+)-\n(\w+)', r'\1\2', text)  # remove hyphens at line breaks
#     text = text.replace('\n', ' ')  # replace newlines with spaces
#     text = re.sub(r'\s+', ' ', text).strip()  # remove extra spaces
#     text = re.sub(r';', ',', text)  # replace semicolons with commas
#     text = re.sub(r':', '.', text)  # replace colons with periods
#
#     # remove text inside curly or other brackets
#     text = re.sub(r'\{.*?\}', '', text)
#     text = re.sub(r'\(.*?\)', '', text)
#     text = re.sub(r'\[.*?\]', '', text)
#
#     # find the index of the first occurrence of "Datum:" and remove text before it
#     datum_index = text.find("Datum:")
#     if datum_index != -1:
#         text = text[datum_index+len("Datum:"):]
#
#     # remove text before "Sehr geehrt" followed by any characters
#     sehr_geehrt_index = re.search(r'Sehr geehrt.*', text, flags=re.IGNORECASE)
#     if sehr_geehrt_index:
#         text = text[sehr_geehrt_index.start():]
#
#     # find the index of "Berliner Sparkasse" and remove everything after it
#     berliner_sparkasse_index = text.find("Berliner Sparkasse")
#     if berliner_sparkasse_index != -1:
#         text = text[:berliner_sparkasse_index]
#
#     return text
#
# def clean_and_save_files(input_directory, output_directory):
#     """
#     Cleans and saves text files from the input directory to the output directory.
#
#     Args:
#         input_directory (str): Path to the directory containing the input text files.
#         output_directory (str): Path to the directory where cleaned text files will be saved.
#     """
#     if not os.path.exists(output_directory):
#         os.makedirs(output_directory)
#
#     for filename in os.listdir(input_directory):
#         if filename.endswith('.txt'):
#             input_file_path = os.path.join(input_directory, filename)
#             output_file_path = os.path.join(output_directory, filename.replace('.txt', '_cldn.txt'))
#
#             if os.path.exists(output_file_path):
#                 print(f"Skipping {filename}. Output file {output_file_path} already exists.")
#                 continue
#
#             with open(input_file_path, 'r', encoding='utf-8') as file:
#                 extracted_text = file.read()
#
#             cleaned_text = clean_extracted_text(extracted_text)
#
#             with open(output_file_path, 'w', encoding='utf-8') as file:
#                 file.write(cleaned_text)
#
#             print(f'Cleaned text has been saved to: {output_file_path}')
#
