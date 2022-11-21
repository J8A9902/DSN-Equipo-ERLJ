import os
from flask import Flask
from helpers.extensions import initialize_database, receive_publisher_messages

app=Flask(__name__)

app_context=app.app_context()
app_context.push()

initialize_database(app)
receive_publisher_messages(app)
