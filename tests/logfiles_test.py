"""This test the logfiles"""

import os
from app.logging_config import log_con, LOGGING_CONFIG
import logs

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
