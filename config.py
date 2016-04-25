#!/usr/bin/env python
#coding:utf-8
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]


# mail server settings
MAIL_SERVER = 'smtp.xxx.com'
MAIL_PORT = 25
MAIL_USERNAME = "yourid@xxx.com"
MAIL_PASSWORD = "yourpw"

# administrator list
ADMINS = ['admin@xxx.com']


# pagination
POSTS_PER_PAGE = 3

WHOOSH_BASE = os.path.join(basedir, 'search.db')
MAX_SEARCH_RESULTS = 50

LANGUAGES = {
    'en':'English',
    'zh':'简体中文'
}

# microsoft translation service
MS_TRANSLATOR_CLIENT_ID = 'yourid' 
MS_TRANSLATOR_CLIENT_SECRET = 'yoursecret'