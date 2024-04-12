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

def getConnection():
    conn = connect(dbname=dbname, user=user,password=password, host=host, port=port )
    return conn

@app.get('/api/users')
def get_users():
    return 'getting users'

@app.post('/api/users')
def create_user():
    new_user = request.get_json()
    username = new_user['username']
    email = new_user['email']
    password = new_user['password']

    print(username, email, password)
    return 'creating users'

@app.delete('/api/users/:id')
def delete_user():
    return 'deleting users'

@app.put('/api/users/:id')
def update_users():
    return 'updating users'

@app.get('/api/users/:id')
def get_user():
    return 'getting user'

if __name__ == '__main__':
    app.run(debug=True, port=3000)
