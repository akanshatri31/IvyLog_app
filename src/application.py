from flask import Flask
import mysql.connector
from mysql import connector

app = Flask(__name__)

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port = 5000, debug = True)
