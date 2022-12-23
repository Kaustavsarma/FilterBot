import os
import time

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5741172694:AAHCsBhhVuqUZFhcmBmjZJ4N-a041KmYeU8")


    # Get from my.telegram.org (or @UseTGXBot)
    API_ID = int(os.environ.get("API_ID", 15491305))


    # Get from my.telegram.org (or @UseTGXBot)
    API_HASH = os.environ.get("API_HASH", "ff25a1e36480a412c8e4a73869d588d9")
    
    
    # Database URL from https://cloud.mongodb.com/
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://filter:filter@cluster0.ie2bgup.mongodb.net/?retryWrites=true&w=majority")


    # Your database name from mongoDB
    DATABASE_NAME = str(os.environ.get("DATABASE_NAME", "Cluster0"))


    # ID of users that can use the bot commands
    AUTH_USERS = set(str(x) for x in os.environ.get("AUTH_USERS", "1768540149").split())


    # To save user details (Usefull for getting userinfo and total user counts)
    # May reduce filter capacity :(
    # Give yes or no
    SAVE_USER = os.environ.get("SAVE_USER", "no").lower()


    # Go to https://dashboard.heroku.com/account, scroll down and press Reveal API
    # To check dyno status
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "")


    # OPTIONAL - To set alternate BOT COMMANDS
    ADD_FILTER_CMD = os.environ.get("ADD_FILTER_CMD", "add")
    DELETE_FILTER_CMD = os.environ.get("DELETE_FILTER_CMDD", "del")
    DELETE_ALL_CMD = os.environ.get("DELETE_ALL_CMDD", "delall")
    CONNECT_COMMAND = os.environ.get("CONNECT_COMMANDD", "connect")
    DISCONNECT_COMMAND = os.environ.get("DISCONNECT_COMMANDD", "disconnect")


    # To record start time of bot
    BOT_START_TIME = time.time()
