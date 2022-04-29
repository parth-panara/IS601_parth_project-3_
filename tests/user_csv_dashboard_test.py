"""This test checks the USER's entry & exit after login, access deny, and csv file upload, processing"""
import os
import pytest
from app import db
import logging
from app import config
from app.db.models import User, Song



# Test to add and delete the User from dashboard

def test_adding_deleting_user(application):
    with application.app_context():
    # current number of users in the database
      assert db.session.query(User).count() == 0

    # adding the user's credentials in the database
    user_email = 'parth@test.com'
    user_password = 'testtest'
    user = User(user_email, user_password)
    db.session.add(user)

    #commiting the user in the database
    user = User.query.filter_by(email='parth@test.com').first()
    assert user.email == 'parth@test.com'
    db.session.commit()

    # now checking the total number of users
    assert db.session.query(User).count() == 1

    # now checking the deleting the users and checking total users
    db.session.delete(user)
    assert db.session.query(User).count() == 0

# Test to check If the csv file is located in 'uploads' folder, considered upload request, and readable

def test_file_uploads(application, add_user):
    log = logging.getLogger("myApp")
    with application.app_context():
        assert db.session.query(User).count() == 1
        assert db.session.query(Song).count() == 0

    root = config.Config.BASE_DIR
    csv_file = 'music.csv'
    filepath = root + '/..app/uploads/' + csv_file


    uploadfolder = config.Config.UPLOAD_FOLDER
    file_upload = os.path.join(uploadfolder, csv_file)
    assert os.path.exists(file_upload) == True

    with application.test_client() as client:
        with open(file_upload, 'rb') as file:
            data = {
                'file': (file, csv_file),

                }
            resp = client.post('songs/upload', data=data)

    assert resp.status_code == 302


# this checks if the login user is able to log out from the application
def user_logout(client):

    response = client.get("/logout")
    assert response.status_code == 200
    return client.get('/logout', follow_redirects=True)


# Test to check when access deny to user to the song Management at dashboard

def test_access_song_manage_denied(client):
    response = client.get("/browse_songs", follow_redirects=False)
    assert response.status_code == 404

# Test to check when access deny to user to upload the csv songs file at dashboard

def test_upload_csvfile_access_denied(client):
    response = client.get("/upload", follow_redirects=False)
    assert response.status_code == 404

# Test to check if user is unable to reach at dashboard

def user_dashboard_access_deny(client):

    response = client.get("/dashboard")
    assert response.status_code == 403
    return client.get('/dashboard', follow_redirects=False)


# Test to check if user is approved and welcomed at the dashboard
def user_dashboard_access_approved(client):

    response = client.get("/dashboard")
    assert response.status_code == 200
    return client.get('/dashboard', follow_redirects=True)