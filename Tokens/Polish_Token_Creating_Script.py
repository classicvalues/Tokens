import itertools
import csv
import os

# Define the character set and lengths for tokens
CHARSET = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZąćęłńóśźż'  # Replace this with the character set for each language
MIN_TOKEN_LENGTH = 1
MAX_TOKEN_LENGTH = 4
MAX_COLUMNS = 400000  # Maximum number of rows per CSV

def generate_tokens(charset, min_length, max_length):
    """Generates tokens of lengths from `min_length` to `max_length` from the charset."""
    for length in range(min_length, max_length + 1):
        # Generate all combinations of a given length
        tokens = itertools.product(charset, repeat=length)
        yield from ("".join(token) for token in tokens)

def write_tokens_to_csv(tokens, max_columns, output_dir='C:\\Artificial_Intelligence\\Tokens\\Polish_Tokens'):
    """Writes tokens to multiple CSV files with a max number of rows per file, including a key and Unicode as columns."""
    os.makedirs(output_dir, exist_ok=True)
    file_count = 1
    token_count = 0
    current_file = os.path.join(output_dir, f"tokens_part_{file_count}.csv")
    csvfile = open(current_file, mode='w', newline='', encoding='utf-8')
    writer = csv.writer(csvfile)

    # Write the header row for metadata
    header = ['Token', 'Key', 'Unicode', 'Definition', 'POS', 'Frequency',
              'Contextual Use', 'Partial Token Use', 'Weight', 'Previous Token Influence']
    writer.writerow(header)

    key = 1  # Initialize key sequence starting from 1

    for token in tokens:
        # Generate the Unicode code point for each token
        unicode_code_point = " ".join(f"U+{ord(char):04X}" for char in token)
       
        # Create a row for the current token with all metadata as separate columns
        row = [
            token,                         # Token itself
            key,                           # Key: the sequence number
            unicode_code_point,            # Unicode code point(s)
            "",                            # Placeholder for 'Definition'
            "",                            # Placeholder for 'POS' (Part of Speech)
            0,                             # Placeholder for 'Frequency'
            "",                            # Placeholder for 'Contextual Use'
            "No",                          # Placeholder for 'Partial Token Use'
            0.0,                           # Placeholder for 'Weight'
            ""                             # Placeholder for 'Previous Token Influence'
        ]
       
        # Write the row to the CSV file
        writer.writerow(row)
        key += 1
        token_count += 1

        # If the number of tokens exceeds max_columns, create a new CSV file
        if token_count >= max_columns:
            csvfile.close()
            file_count += 1
            token_count = 0
            current_file = os.path.join(output_dir, f"tokens_part_{file_count}.csv")
            csvfile = open(current_file, mode='w', newline='', encoding='utf-8')
            writer = csv.writer(csvfile)
            writer.writerow(header)

    # Close the last open file
    csvfile.close()

    print(f"Tokens written across {file_count} CSV files in '{output_dir}' directory.")

# Generate and write tokens to CSV files
tokens = generate_tokens(CHARSET, MIN_TOKEN_LENGTH, MAX_TOKEN_LENGTH)
write_tokens_to_csv(tokens, MAX_COLUMNS)