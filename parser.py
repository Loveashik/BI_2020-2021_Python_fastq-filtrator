"""
RESULT:
dict: {'reads': [(), (), ...],
      'min length': int,
      'keep filtered': True/False,
      'gc bounds': [] - False/ L /L R values,
      'output base name': some string
      }
"""


def parse(arguments):
    file = ''
    diction = {}
    for arg in arguments:
        if arg.endswith(".fastq"):
            file = arg
            break

    reads = []  # reads = [ [s1, s2, s3, s4], [], ... ]
    if file:
        i = 0
        current_read = []
        with open(file) as infile:
            for s in infile:
                i += 1
                current_read.append(s.rstrip('\n'))
                if i % 4 == 0:
                    reads.append(tuple(current_read))
                    current_read = []
    diction['reads'] = reads

    if '--min_length' in arguments:
        min_len = arguments[arguments.index('--min_length') + 1]
        diction['min length'] = int(min_len)
    else:
        diction['min length'] = 1

    if '--keep_filtered' in arguments:
        diction['keep filtered'] = 'True'
    else:
        diction['keep filtered'] = 'False'

    # list containing 1 or 2 elements:
    if '--gc_bounds' in arguments:
        if arguments.index('--gc_bounds') + 1 != len(arguments)-1:
            if arguments[arguments.index('--gc_bounds') + 2].isdigit():
                diction['gc bounds'] = [int(arguments[arguments.index('--gc_bounds') + 1]), int(arguments[arguments.index('--gc_bounds') + 2])]
            else:
                diction['gc bounds'] = [int(arguments[arguments.index('--gc_bounds') + 1])]
        else:
            diction['gc bounds'] = [int(arguments[arguments.index('--gc_bounds') + 1])]
    else:
        diction['gc bounds'] = 'False'

    if '--output_base_name' in arguments:
        if '--keep_filtered' in arguments:
            diction['output base name'] = [str(arguments[arguments.index('--output_base_name') + 1]) + '__passed.fastq',
                                           str(arguments[arguments.index('--output_base_name') + 1]) + '__failed.factq']
        else:
            diction['output base name'] = [str(arguments[arguments.index('--output_base_name') + 1]) + '__passed.fastq']
    else:
        file_name = file[:-6]  # Text before .fastq
        if '--keep_filtered' in arguments:
            diction['output base name'] = [file_name + "__passed", file_name + "__failed"]
        else:
            diction['output base name'] = [file_name + "__passed"]

    return diction
