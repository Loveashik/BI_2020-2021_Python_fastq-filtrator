import sys
from parser import parse
from filtration_logic import filter_reads

if __name__ == '__main__':
    arguments = sys.argv
    parsed_data = parse(arguments)
    filter_reads(parsed_data)