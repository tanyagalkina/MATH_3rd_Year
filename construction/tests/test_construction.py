import pytest

from construction import main_func
from answers import *





def test_wrong_number_args(capsys):
    argv = ['./305construction', 'not_exist', 'a']
    try:
        main_func(argv)
    except SystemExit:
        capture = capsys.readouterr()
        assert capture.err == WRONG_NUMBER_ARGS
    else:
        assert 3  is 4


##JUST LEFT THE EXAMPLES FOR LOOK AT


'''

def test_empty_file(capsys):
    argv = ['./303make', 'tests/empty_file']
    try:
        get_sources(argv)
    except SystemExit:
        capture = capsys.readouterr()
        assert capture.err == "Unfortunately, the file you provided is empty..(((\n"
    else:
        assert 3  is 4

def test_file_not_exist(capsys):
    argv = ['./303make', 'not_exist']
    try:
        get_sources(argv)
    except SystemExit:
        capture = capsys.readouterr()
        assert capture.err == "File not_exist not found.  Aborting\n"
    else:
        assert 3  is 4


def test_wrong_number_args(capsys):
    argv = ['./303make', 'not_exist', 'bla', 'bloo']
    try:
        get_sources(argv)
    except SystemExit:
        capture = capsys.readouterr()
        assert capture.err == "Wrong number of args\n"
    else:
        assert 3  is 4


def test_src_not_in_project(capsys):
    argv = ['./303make', 'tests/test_file1', 'tanya']
    try:
        main_func(argv)
    except SystemExit:
        capture = capsys.readouterr()
        assert capture.err == "The source you gave is not a part of the project\n"
    else:
        assert 3  is 4

def test_file1_depth(capsys):
    argv = ['./303make', 'tests/test_file1']
    main_func(argv)
    capture = capsys.readouterr()
    assert capture.out == FIRST_TEST


def test_file1_breadth(capsys):
    argv = ['./303make', 'tests/test_file1', 'fc.h']
    main_func(argv)
    capture = capsys.readouterr()
    assert capture.out == FIRST_TEST_BREADTH


def test_file1_breadth_two(capsys):
    argv = ['./303make', 'tests/test_file1', 'tty.c']
    main_func(argv)
    capture = capsys.readouterr()
    assert capture.out == TWO_TEST_BREADTH


def test_file1_breadth_nothing(capsys):
    argv = ['./303make', 'tests/test_file1', 'tty']
    try:
        main_func(argv)
    except SystemExit:
        capture = capsys.readouterr()
        assert capture.out == '\n'


def test_one_dependency_two_commands(capsys):
    argv = ['./303make', 'tests/test_file2', 'main.h']
    main_func(argv)
    capture = capsys.readouterr()
    assert capture.out == TWO_COMMANDS

def test_crazy_file_aa(capsys):
    argv = ['./303make', 'tests/test_file3', 'aa']
    main_func(argv)
    capture = capsys.readouterr()
    assert capture.out == CRAZY_FILE_AA

def test_crazy_file_ba(capsys):
    argv = ['./303make', 'tests/test_file3', 'ba']
    main_func(argv)
    capture = capsys.readouterr()
    assert capture.out == CRAZY_FILE_BA

def test_crazy_file_ca(capsys):
    argv = ['./303make', 'tests/test_file3', 'ca']
    main_func(argv)
    capture = capsys.readouterr()
    assert capture.out == CRAZY_FILE_CA'''
