import sys
from parser import parse
from filtration_logic import filter_reads

if __name__ == '__main__':
    arguments = sys.argv
    parsed_data = parse(arguments)

    if parsed_data['keep filtered'] == 'True':
        reads_passed, reads_failed = filter_reads(parsed_data)
    else:
        reads_passed = filter_reads(parsed_data)

    output_file_sorted = parsed_data["output base name"][0]
    with open(output_file_sorted, 'w') as output:
        for read in reads_passed:
            for w in read:
                output.write(w + '\n')

    if parsed_data['keep filtered'] == 'True':
        output_file_error = parsed_data["output base name"][1]
        with open(output_file_error, 'w') as output:
            for read in reads_failed:
                for w in read:
                    output.write(w + '\n')
