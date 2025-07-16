import csv
from io import StringIO

def process_csv_data(csv_content: str):
    csv_file = StringIO(csv_content)
    reader = csv.DictReader(csv_file)
    parsed_data = list(reader)
    header = list(parsed_data[0].keys())
    return parsed_data, header