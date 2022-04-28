"""This test checks the Database, logs, and Uploads folder"""

import logging
import os
from pathlib import Path
from click.testing import CliRunner

from app import create_database
import logs
from app.db import config
runner = CliRunner()

# Test to check if Database folder File is created

def test_create_database():
    response = runner.invoke(create_database)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    dbdir = os.path.join(root, '../database')
    # make a directory if it doesn't exist
    assert os.path.exists(dbdir) == True


# Test to check if Logs folder is created

def test_create_log_folder():
    logdir = config.Config.LOG_DIR
    path = Path(logdir)

    if path.is_file():
        print(f'The file {logs} exists')
    else:
        print(f'The file {logs} does not exist')


# Test to check if uploads folder is created for CSV file

def test_create_uploads_folder():
    root = config.Config.BASE_DIR
    # set the name of the apps log folder to logs
    uploadfolder = os.path.join(root, '..', config.Config.UPLOAD_FOLDER)
    # make a directory if it doesn't exist
    assert os.path.exists(uploadfolder) == True
