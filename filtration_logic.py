"""
Module with filtration logic
Input :: dictionary from parser
Output :: 1 or 2 saved files
"""


def filter_reads(diction):
    reads = diction['reads']
    reads_passed = []
    reads_failed = []

    if diction['gc bounds'] == 'False':
        for i in range(len(reads)):
            if len(reads[i][1]) < diction['min length']:
                reads_failed.append(reads[i])
            else:
                reads_passed.append(reads[i])

    elif diction['gc bounds'] != 'False':
        for i in range(len(reads)):
            if len(reads[i][1]) < diction['min length']:
                reads_failed.append(reads[i])
            else:
                count = 0.
                for nucl in reads[i][1]:
                    if (nucl == 'G') or (nucl == 'C'):
                        count += 1

                gc_content = (count / len(reads[i][1])) * 100

                if len(diction['gc bounds']) == 1:
                    if gc_content >= diction['gc bounds'][0]:
                        reads_passed.append(reads[i])
                    else:
                        reads_failed.append(reads[i])

                elif len(diction['gc bounds']) == 2:
                    if diction['gc bounds'][0] <= gc_content <= diction['gc bounds'][1]:
                        reads_passed.append(reads[i])
                    else:
                        reads_failed.append(reads[i])

    output_file_sorted = diction["output base name"][0]
    with open(output_file_sorted, 'w') as output:
        for read in reads_passed:
            for w in read:
                output.write(w + '\n')

    if diction['keep filtered'] == 'True':
        output_file_error = diction["output base name"][1]
        with open(output_file_error, 'w') as output:
            for read in reads_failed:
                for w in read:
                    output.write(w + '\n')
