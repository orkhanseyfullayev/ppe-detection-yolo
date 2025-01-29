import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

def rename_txt_files(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        if filename.lower().endswith('.txt'):
            input_path = os.path.join(input_directory, filename)
            new_filename = f"1-{filename}"
            output_path = os.path.join(output_directory, new_filename)

            with open(input_path, 'r', encoding='utf-8') as infile:
                content = infile.read()

            with open(output_path, 'w', encoding='utf-8') as outfile:
                outfile.write(content)

            print(f"{filename} successfully renamed and saved as: {new_filename}")

input_directory = "C:\\Users\\txt-in"
output_directory = "C:\\Users\\txt-out"

rename_txt_files(input_directory, output_directory)