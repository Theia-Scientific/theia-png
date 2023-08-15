#!/usr/bin/env python3

from io import BytesIO
from tspng.extraction import extract,extract_from_bytes,extract_from_file,extract_from_files,extract_from_folder

def test_extract():
    '''
    Tests the dictionary keys from an example TSPNG file path.
    '''
    #test bytes
    with open('tests/assets/example_file_1.ts.png', 'rb') as fh:
        buf = BytesIO(fh.read())
        test_data = extract_from_bytes(buf)
        assert list(test_data.keys())==['info','licenses','images','annotations','models','categories']
    #test file
    test_data = extract('tests/assets/example_file_1.ts.png')
    assert list(test_data.keys())==['info','licenses','images','annotations','models','categories']
    #test list of files
    test_data = extract_from_files(['tests/assets/example_file_1.ts.png','tests/assets/example_file_2.ts.png'])
    assert list(test_data.keys())==['tests/assets/example_file_1.ts.png','tests/assets/example_file_2.ts.png']
    #test folder
    test_data = extract_from_folder('tests/assets')
    assert list(test_data.keys())==['tests/assets/example_file_1.ts.png','tests/assets/example_file_2.ts.png']

def test_extract_from_bytes():
    '''
    Tests the dictionary keys from an example TS byte stream.
    '''
    with open('tests/assets/example_file_1.ts.png', 'rb') as fh:
        buf = BytesIO(fh.read())
        test_data = extract_from_bytes(buf)
        assert list(test_data.keys())==['info','licenses','images','annotations','models','categories']

def test_extract_from_file():
    '''
    Tests the dictionary keys from an example TSPNG file path.
    '''
    test_data = extract_from_file('tests/assets/example_file_1.ts.png')
    assert list(test_data.keys())==['info','licenses','images','annotations','models','categories']

def test_extract_from_files():
    '''
    Tests the dictionary keys from a list of example TSPNG file paths.
    '''
    test_data = extract_from_files(['tests/assets/example_file_1.ts.png','tests/assets/example_file_2.ts.png'])
    assert list(test_data.keys())==['tests/assets/example_file_1.ts.png','tests/assets/example_file_2.ts.png']
    
def test_extract_from_folder():
    '''
    Tests the dictionary keys from a list of example TSPNG file paths.
    '''
    test_data = extract_from_folder('tests/assets')
    assert list(test_data.keys())==['tests/assets/example_file_1.ts.png','tests/assets/example_file_2.ts.png']
