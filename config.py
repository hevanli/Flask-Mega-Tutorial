import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['evanlicubs@gmail.com']

    POSTS_PER_PAGE = 25
    LANGUAGES = ['en', 'es']

# python -m smtpd -n -c DebuggingServer localhost:8025
# export MAIL_SERVER=localhost
# export MAIL_PORT = 8025

# pybabel extract -F babel.cfg -k _l -o messages.pot .

# pybabel init -i messages.pot -d app/translations -l es
# pybabel update -i messages.pot -d app/translations

# pybabel compile -d app/translations