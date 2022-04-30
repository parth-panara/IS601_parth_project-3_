"""This test the all logfiles"""
import logging
import os


import app.config


def test_logfile_myapp():
    root = os.path.dirname(os.path.abspath(__file__))
    logfile= os.path.join(root, '../logs/errors.log')
    assert os.path.exists(logfile) == True

def test_logfile_second_myapp():
    root = os.path.dirname(os.path.abspath(__file__))
    logfile= os.path.join(root, '../logs/handler.log')
    assert os.path.exists(logfile) == True

def test_logfile_third_myapp():
    root = os.path.dirname(os.path.abspath(__file__))
    logfile= os.path.join(root, '../logs/myapp.log')
    assert os.path.exists(logfile) == True

def test_logfile_fourth_myapp():
    root = os.path.dirname(os.path.abspath(__file__))
    logfile= os.path.join(root, '../logs/request.log')
    assert os.path.exists(logfile) == True

def test_logfile_fifth_myapp():
    root = os.path.dirname(os.path.abspath(__file__))
    logfile= os.path.join(root, '../logs/sqlalchemy.log')
    assert os.path.exists(logfile) == True

def test_logfile_sixth_myapp():
    root = os.path.dirname(os.path.abspath(__file__))
    logfile= os.path.join(root, '../logs/werkzeug.log')
    assert os.path.exists(logfile) == True


# the another way to check logfiles with one of the same files log files from above

def test_myapp_logfile():
    log_dir = app.config.Config.LOG_DIR
    filepath = os.path.join(log_dir, "myapp.log")
    assert os.path.isfile(filepath)

# test to check if csvfile.log exists

def test_csvfile_logfile():
    log_dir = app.config.Config.LOG_DIR
    filepath = os.path.join(log_dir, "csvfile.log")
    assert os.path.isfile(filepath)

# test to check if the functions of logfiles are from 'init_py' is readable

def test_add_path_to_logfile():

    path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(path, '../app/logging_config/__init__.py')
    with open(filepath, encoding="utf-8") as file:
        data = {
            'file': filepath
            }
    assert os.path.isfile(filepath)





