import csv
import argparse
from openpyxl import Workbook
from pathlib import Path
from io import StringIO

parser = argparse.ArgumentParser(prog="csvtoexcel")
parser.add_argument("csvfile")
parser.add_argument("--delimiter", default=',', help="default: ,")
parser.add_argument("--quote", default='"', help="default: \"")
parser.add_argument("--escape", default='\\', help="default: \\")
parser.add_argument("--null", default='\\N', help="default: \\N")
args = parser.parse_args()
wb = Workbook()
wb.create_sheet(title="NEW")
ws = wb["NEW"]
with open(args.csvfile, 'r') as csvfile:
    data = csvfile.read()
    data = data.replace(args.null, "NULL")
    reader = csv.reader(StringIO(data), delimiter=args.delimiter, quotechar=args.quote, escapechar=args.escape, doublequote=False)
    for row in reader:
        ws.append(row)
p = Path(args.csvfile)
wb.save(p.with_suffix(".xlsx"))
