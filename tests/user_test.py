"""This test checks the USER, SONG, TITLE, GENRE, YEAR"""
import logging

from app import db
from app.db.models import User, Song


def test_adding_user(application):
    log = logging.getLogger("myApp")
    with application.app_context():
        assert db.session.query(User).count() == 0
        assert db.session.query(Song).count() == 0
        #showing how to add a record
        #create a record
        user = User('keith@webizly.com', 'testtest')
        #add it to get ready to be committed
        db.session.add(user)
        #call the commit
        #db.session.commit()
        #assert that we now have a new user
        #assert db.session.query(User).count() == 1
        #finding one user record by email
        user = User.query.filter_by(email='keith@webizly.com').first()
        log.info(user)
        #asserting that the user retrieved is correct
        assert user.email == 'keith@webizly.com'
        #this is how you get a related record ready for insert
        user.songs= [Song("songA","artistA","genreA","yearA"),Song("songA","artistB","genreB","yearB")]
        #commit is what saves the songs
        db.session.commit()
        assert db.session.query(Song).count() == 2

        song1 = Song.query.filter_by(title='songA').first()
        assert song1.title == "songA"
        #changing the title of the song
        song1.title = "SuperSongTitle"
        #saving the new title of the song
        db.session.commit()
        song2 = Song.query.filter_by(title='SuperSongTitle').first()
        assert song2.title == "SuperSongTitle"
        #checking cascade delete
        db.session.delete(user)
        assert db.session.query(User).count() == 0
        assert db.session.query(Song).count() == 0

#Test to check for the another user. User has songName which contains artist, genre, and year

def test_adding_one_user(application):
    log = logging.getLogger("myApp")
    with application.app_context():
        assert db.session.query(User).count() == 0
        assert db.session.query(Song).count() == 0
        # showing how to add a record
        # create a record
        user = User('parth@webizly.com', 'testtest')
        # add it to get ready to be committed
        db.session.add(user)

        user = User.query.filter_by(email='parth@webizly.com').first()
        log.info(user)
        # asserting that the user retrieved is correct
        assert user.email == 'parth@webizly.com'
        # this is how you get a related record ready for insert
        user.songs= [Song("songNameC","artistC","genreC","yearC")]
        # commit is what saves the songs
        db.session.commit()
        assert db.session.query(Song).count() == 1

#Test to check for the third user. User has songName which contains artist, genre, and year

def test_adding_second_user(application):
    log = logging.getLogger("myApp")
    with application.app_context():
        assert db.session.query(User).count() == 0
        assert db.session.query(Song).count() == 0
        # showing how to add a record
        # create a record
        user = User('parth@test.com', 'testtest')
        # add it to get ready to be committed
        db.session.add(user)

        user = User.query.filter_by(email='parth@test.com').first()
        log.info(user)
        # asserting that the user retrieved is correct
        assert user.email == 'parth@test.com'
        # this is how you get a related record ready for insert
        user.songs= [Song("songNameD","artistD","genreD","yearD")]
        # commit is what saves the songs
        db.session.commit()
        assert db.session.query(Song).count() == 1





