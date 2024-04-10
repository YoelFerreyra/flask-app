from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_mysqldb import MySQL

app=Flask(__name__)

# Connection MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'courses'

connectionDB = MySQL(app)

@app.before_request
def before_request():
    print('Before request')

@app.after_request
def after_request(response):
    print('After request')
    return response

@app.route('/') #decorator
def index():
    courses=['Kotlin','Javascript','Python','React']
    data={
        'title': 'Application',
        'welcome': 'Hi!',
        'courses': courses,
        'number_courses': len(courses)
    }
    return render_template('index.html', data=data)

@app.route('/contact/<name>/<int:age>')
def contact(name, age):
    data={
        'title': 'Contact',
        'name': name,
        'age': age
    }
    return render_template('contact.html', data=data)

def query_string():
    print(request)
    print(request.args)
    print(request.args.get('name'))
    print(request.args.get('age'))
    return 'OK'    

def page_not_found(error):
    # return render_template('404.html'), 404
    return redirect(url_for('index'))

@app.route('/courses')
def list_courses():
    data={}
    try:
        cursor=connectionDB.connection.cursor()
        sql='SELECT name FROM courses ORDER BY name ASC'
        cursor.execute(sql)
        courses=cursor.fetchall()
        data['message']=courses
        data['message']='All right'
    except Exception as ex:
        data['message']='Error'
    return jsonify(data)

if __name__ == '__main__':
    app.add_url_rule('/query_string', view_func=query_string)
    app.register_error_handler(404, page_not_found)
    app.run(debug=True, port=3000)
