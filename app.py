from flask import Flask, render_template, request, redirect, url_for, jsonify
from psycopg2 import connect
from dotenv import load_dotenv
from os import environ

load_dotenv()

app=Flask(__name__)

host = environ.get('DB_HOST')
port = environ.get('DB_PORT')
dbname = environ.get('DB_NAME')
user = environ.get('DB_USER')
password = environ.get('DB_PASSWORD')

print("db",environ.get('DB_HOST'))
print("db",environ.get('DB_PORT'))
print("db",environ.get('DB_NAME'))
print("db",environ.get('DB_USER'))
print("pass",password)

def getConnection():
    conn = connect(dbname=dbname, user=user,password=password, host=host, port=port )
    return conn

@app.get('/')
def home():
    conn = getConnection()
    cursor = conn.cursor()

    cursor.execute("SELECT 1 + 1")
    result = cursor.fetchone()

    print(result)
    return 'home'

if __name__ == '__main__':
    app.run(debug=True, port=3000)
