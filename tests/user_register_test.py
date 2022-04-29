"""This test checks the user's registration and login before entering into the account, then access to the dashboard and logout"""
import logging

from app import db
from app.db.models import User


def test_user_register_in_app(client):
    #registration of user

    new_email = 'parth_song@test.com'
    new_password = 'Mytest123#'
    data = {
        'email' : new_email,
        'password' : new_password,
        'confirm' : new_password
    }
    resp = client.post('register', data=data)

    assert resp.status_code == 302

    # verify new user is registered and eligible to log in the application
    registered_user = User.query.filter_by(email='parth_song@test.com').first()
    assert registered_user.email == 'parth_song@test.com'
    # application is able to remove the user from database
    db.session.delete(registered_user)

def test_user_login_post_registration(client):
    #this checks if after completing the registration user is allowed to log in

    data = {
        'email' : 'parth_song@test.com',
        'password' : 'Mytest123#'
    }
    resp = client.post('login', data=data)
    assert resp.status_code == 302

def login_user_access_dashboard(client):
    # this checks if the login user is able to get access at dashboard

    response = client.get("/dashboard")
    assert response.status_code == 200
    assert b"{{render_nav_item('auth.dashboard', 'Dashboard')}}"in response.data
    return client.get('/dashboard', follow_redirects=True)











