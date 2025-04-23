import re
import json
import sys

def remove_json_comments(json_str):
    # Remove // single-line comments
    json_str = re.sub(r'\/\/.*', '', json_str)
    # Remove /* */ multi-line comments
    json_str = re.sub(r'\/\*[\s\S]*?\*\/', '', json_str)
    return json_str.strip()

def process_theme(input_file, output_file):
    with open(input_file, 'r') as f:
        content = f.read()

    clean_json = remove_json_comments(content)
    data = json.loads(clean_json)

    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python clean_bntheme.py input_with_comments.bntheme output_clean.bntheme")
    else:
        process_theme(sys.argv[1], sys.argv[2])

