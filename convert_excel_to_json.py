import pandas as pd
import json
import sys

def convert_excel_to_json(excel_file, json_file):
    # Read the Excel file
    df = pd.read_excel(excel_file)

    # Convert the DataFrame to a JSON format
    json_data = df.to_json(orient='records', lines=True)

    # Write the JSON data to a file
    with open(json_file, 'w') as f:
        f.write(json_data)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_excel_to_json.py <excel_file> <json_file>")
    else:
        convert_excel_to_json(sys.argv[1], sys.argv[2])