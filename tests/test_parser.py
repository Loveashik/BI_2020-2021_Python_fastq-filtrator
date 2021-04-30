from parser import parse


def test_base():

    command = 'python filter_fastq.py simple_data.fastq --min_length 10 --gc_bounds 70' \
              ' --keep_filtered --output_base_name result.fastq'
    args = command.split(' ')[1:]
    parsed_dict = parse(args)
    assert len(parsed_dict['reads']) == 2
    assert parsed_dict['min length'] == 10
    assert parsed_dict['gc bounds'] == [70]
    assert parsed_dict['output base name'] == ['result.fastq__passed.fastq', 'result.fastq__failed.factq']
    assert parsed_dict['keep filtered'] == 'True'


def test_params_skipped_and_shuffled():
    command = 'python filter_fastq.py simple_data.fastq --output_base_name result.fastq --gc_bounds 1 99'
    args = command.split(' ')[1:]
    parsed_dict = parse(args)
    assert len(parsed_dict['reads']) == 2
    assert parsed_dict['min length'] == 1
    assert parsed_dict['gc bounds'] == [1, 99]
    assert parsed_dict['output base name'] == ['result.fastq__passed.fastq']
    assert parsed_dict['keep filtered'] == 'False'
