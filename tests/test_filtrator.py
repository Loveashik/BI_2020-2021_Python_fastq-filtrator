from filtration_logic import filter_reads
from parser import parse


def test_gc_bounds():

    # -------------------------------------------------------------------
    # GC bounds: 0 - 1
    # -------------------------------------------------------------------

    command = 'python filter_fastq.py simple_data.fastq --gc_bounds 0 1' \
              ' --keep_filtered --output_base_name result.fastq'
    args = command.split(' ')[1:]
    parsed_dict = parse(args)
    reads_passed, reads_failed = filter_reads(parsed_dict)
    assert len(reads_passed) == 1
    assert len(reads_failed) == 1

    # -------------------------------------------------------------------
    # GC bounds: 0 - 99
    # -------------------------------------------------------------------

    command = 'python filter_fastq.py simple_data.fastq --gc_bounds 0 99' \
              ' --keep_filtered --output_base_name result.fastq'
    args = command.split(' ')[1:]
    parsed_dict = parse(args)
    reads_passed, reads_failed = filter_reads(parsed_dict)
    assert len(reads_passed) == 1
    assert len(reads_failed) == 1

    # -------------------------------------------------------------------
    # GC bounds: 0 - 100
    # -------------------------------------------------------------------

    command = 'python filter_fastq.py simple_data.fastq --gc_bounds 0 100' \
              ' --keep_filtered --output_base_name result.fastq'
    args = command.split(' ')[1:]
    parsed_dict = parse(args)
    reads_passed, reads_failed = filter_reads(parsed_dict)
    assert len(reads_passed) == 2
    assert len(reads_failed) == 0

    # -------------------------------------------------------------------
    # GC bounds: 1 - 99
    # -------------------------------------------------------------------

    command = 'python filter_fastq.py simple_data.fastq --gc_bounds 1 99' \
              ' --keep_filtered --output_base_name result.fastq'
    args = command.split(' ')[1:]
    parsed_dict = parse(args)
    reads_passed, reads_failed = filter_reads(parsed_dict)
    assert len(reads_passed) == 0
    assert len(reads_failed) == 2


def test_min_length():

    # -------------------------------------------------------------------
    # Min length 1000
    # -------------------------------------------------------------------

    command = 'python filter_fastq.py simple_data.fastq --gc_bounds 0 100' \
              ' --keep_filtered --min_length 1000 --output_base_name result.fastq'
    args = command.split(' ')[1:]
    parsed_dict = parse(args)
    reads_passed, reads_failed = filter_reads(parsed_dict)
    assert len(reads_passed) == 0
    assert len(reads_failed) == 2

    # -------------------------------------------------------------------
    # Min length 100
    # -------------------------------------------------------------------

    command = 'python filter_fastq.py simple_data.fastq --gc_bounds 0 100' \
              ' --keep_filtered --min_length 100 --output_base_name result.fastq'
    args = command.split(' ')[1:]
    parsed_dict = parse(args)
    reads_passed, reads_failed = filter_reads(parsed_dict)
    assert len(reads_passed) == 1
    assert len(reads_failed) == 1

    # -------------------------------------------------------------------
    # Min length 5
    # -------------------------------------------------------------------

    command = 'python filter_fastq.py simple_data.fastq --gc_bounds 0 100' \
              ' --keep_filtered --min_length 5 --output_base_name result.fastq'
    args = command.split(' ')[1:]
    parsed_dict = parse(args)
    reads_passed, reads_failed = filter_reads(parsed_dict)
    assert len(reads_passed) == 2
    assert len(reads_failed) == 0
