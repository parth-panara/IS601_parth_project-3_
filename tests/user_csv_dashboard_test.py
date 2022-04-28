"""This test checks the USER's entry, exit, access deny, and file upload"""
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




# Test to check when access deny to user to the song Management at dashboard

def test_access_song_manage_denied(client):
    response = client.get("/browse_songs")
    assert response.status_code == 404

# Test to check when access deny to user to upload the songs at dashboard

def test_upload_csvfile_access_denied(client):
    response = client.get("/upload")
    assert response.status_code == 404