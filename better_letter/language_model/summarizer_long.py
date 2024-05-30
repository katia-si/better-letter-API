from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import os

# Load pre-trained BART model and tokenizer for German
tokenizer = AutoTokenizer.from_pretrained("Shahm/bart-german")
model = AutoModelForSeq2SeqLM.from_pretrained("Shahm/bart-german")

def calculate_dynamic_lengths(input_text, max_tokens=1024):
    """
    calculate dynamic max_length and min_length based on the length of the input text.

    Args:
        input_text (str):  input text.
        max_tokens (int): maximum number of tokens the model can handle (default 1024 for BART).

    Returns:
        max_length (int): calculated maximum length for the summary.
        min_length (int): calculated minimum length for the summary.
    """
    # tkenize the input text
    tokenized_text = tokenizer.encode(input_text, return_tensors="pt", truncation=True)
    input_length = tokenized_text.size(1)

    # define the dynamic lengths as a percentage of the input length
    max_length = min(max(input_length // 2, 50), max_tokens)  # max half the input length, but min 50 and at most max_tokens
    min_length = max(min(input_length // 4, 100), 30)  # max a quarter of the input length, but min 30 and at most 100

    return max_length, min_length

def generate_summary_dynamic(text: str) -> str:
    """
    generate a dynamic summary of the input text.

    Args:
        text (str): input text.

    Returns:
        str: generated summary.
    """
    # calculate dynamic lengths
    max_length, min_length = calculate_dynamic_lengths(text)

    # Ttkenize and generate summary
    inputs = tokenizer.encode(text, return_tensors="pt", truncation=True, max_length=1024)
    summary_ids = model.generate(
        inputs,
        max_length=max_length,
        min_length=min_length,
        length_penalty=2.0,
        num_beams=2,
        early_stopping=True
    )
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary


def summarize_text_and_print(input_text):
    """
    summarize the input text and print the summary.

    Args:
        input_text (str): The input text to be summarized.

    Returns:
        str: generated summary.
    """
    summary = generate_summary_dynamic(input_text)
    # print("Summary:")
    # print(summary)
    return summary





################################################################################
### OLD: this part summarizes the text and then safe the ouput locally
################################################################################


# m transformers import AutoTokenizer, AutoModelForSeq2SeqLM
# ort os
#
#
# oad pre-trained BART model and tokenizer for German
# enizer = AutoTokenizer.from_pretrained("Shahm/bart-german")
# el = AutoModelForSeq2SeqLM.from_pretrained("Shahm/bart-german")
#
#  calculate_dynamic_lengths(input_text, max_tokens=1024):
#  """
#  calculate dynamic max_length and min_length based on the length of the input text.
#  args:
#      input_text (str): the input text.
#      max_tokens (int): maximum number of tokens the model can handle (default 1024 for BART).
#  returns:
#      max_length (int): calculated maximum length for the summary.
#      min_length (int): calculated minimum length for the summary.
#  """
#  # tokenize the input text
#  tokenized_text = tokenizer.encode(input_text, return_tensors="pt", truncation=True)
#  input_length = tokenized_text.size(1)
#
#  # define the dynamic lengths as a percentage of the input length
#  max_length = min(max(input_length // 2, 50), max_tokens)  # at most half the input length, but at least 50 and at most max_tokens
#  min_length = max(min(input_length // 4, 100), 30)  # at most a quarter of the input length, but at least 30 and at most 100
#
#  return max_length, min_length
#
#  generate_summary_dynamic(text: str) -> str:
#  # calculate dynamic lengths
#  max_length, min_length = calculate_dynamic_lengths(text)
#
#  # tokenize and generate summary
#  inputs = tokenizer.encode(text, return_tensors="pt", truncation=True, max_length=1024)
#  summary_ids = model.generate(
#      inputs,
#      max_length=max_length,
#      min_length=min_length,
#      length_penalty=2.0,
#      num_beams=2,
#      early_stopping=True
#  )
#  summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
#  return summary
#
#
#  summarize_text(input_directory, output_directory):
#  """
#  Summarize text files in the input directory and save the summaries in the output directory.
#
#  Args:
#      input_directory (str): Path to the directory containing the input text files.
#      output_directory (str): Path to the directory where summary text files will be saved.
#  """
#  if not os.path.exists(output_directory):
#      os.makedirs(output_directory)
#
#  for filename in os.listdir(input_directory):
#      if filename.endswith('.txt'):
#          input_file_path = os.path.join(input_directory, filename)
#          output_file_path = os.path.join(output_directory, f'{os.path.splitext(filename)[0]}_sum.txt')
#
#          if os.path.exists(output_file_path):
#              print(f'Skipping {filename}. Output file {output_file_path} already exists.')
#              continue
#
#          with open(input_file_path, 'r', encoding='utf-8') as file:
#              text = file.read()
#
#          summary = generate_summary_dynamic(text)
#
#          with open(output_file_path, 'w', encoding='utf-8') as output_file:
#              output_file.write(summary)
#
#          print(f'Summary has been generated and saved to: {output_file_path}')
#
