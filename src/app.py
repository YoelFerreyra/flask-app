from flask import Flask, render_template, request, redirect, url_for, jsonify, send_file
from psycopg2 import connect, extras
from dotenv import load_dotenv
from os import environ

load_dotenv()

app = Flask(__name__)

host = environ.get('DB_HOST')
port = environ.get('DB_PORT')
dbname = environ.get('DB_NAME')
user = environ.get('DB_USER')
password = environ.get('DB_PASSWORD')


def getConnection():
    conn = connect(dbname=dbname, user=user,
                   password=password, host=host, port=port)
    return conn


@app.get('/api/users')
def get_users():
    conn = getConnection()
    cursor = conn.cursor(cursor_factory=extras.RealDictCursor)

    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    cursor.close()
    conn.close()
    return jsonify(users)


@app.get('/api/users/<int:id>')
def get_user(id):
    conn = getConnection()
    cursor = conn.cursor(cursor_factory=extras.RealDictCursor)

    cursor.execute('SELECT * FROM users WHERE id = %s', (id,))
    user = cursor.fetchone()
    print(user)
    conn.commit()
    cursor.close()
    conn.close()

    if user is None:
        return jsonify({'message': 'User not found'}), 404
    return jsonify(user)


@app.post('/api/users')
def create_user():
    new_user = request.get_json()
    username = new_user['username']
    email = new_user['email']
    password = new_user['password']

    conn = getConnection()
    cursor = conn.cursor()

    cursor.execute('INSERT INTO users (username, email, password) VALUES (%s, %s, %s)',
                   (username, email, password))

    conn.commit()
    cursor.close()
    conn.close()
    return 'creating users'


@app.delete('/api/users/<id>')
def delete_user(id):
    conn = getConnection()
    cursor = conn.cursor(cursor_factory=extras.RealDictCursor)

    cursor.execute('DELETE FROM users WHERE id = %s RETURNING *', (id))
    user = cursor.fetchone()

    conn.commit()

    cursor.close()
    conn.close()

    if user is None:
        return jsonify({'message': 'User not found'}), 404
    return jsonify(user)


@app.put('/api/users/:id')
def update_users():
    return 'updating users'

@app.get('/')
def home():
    return send_file('static/index.html')

if __name__ == '__main__':
    app.run(debug=True, port=3000)
