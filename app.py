from flask import Flask, render_template, jsonify, redirect, request, url_for
import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

#Test connection to db
def get_connection():
    connection = pymysql.connect(
        host=os.getenv('HOST'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        database=os.getenv('DATABASE'),
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

@app.route('/')
def home():
    candies = []
    search_result = None
    search_error = None
    added_message = None
    search_id = request.args.get('candy_id', type=int)

    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM chuches ORDER BY id')
        candies = cursor.fetchall()

        if search_id:
            cursor.execute('SELECT * FROM chuches WHERE id = %s', (search_id,))
            search_result = cursor.fetchone()
            if search_result is None:
                search_error = f'No product found with ID {search_id}.'

        cursor.close()
        connection.close()
    except Exception as err:
        search_error = f'Database error: {err}'

    if request.args.get('added'):
        added_name = request.args.get('added_name', '')
        added_message = f'Added new product: {added_name}' if added_name else 'Added new product successfully.'

    return render_template(
        'home.html',
        candies=candies,
        search_result=search_result,
        search_error=search_error,
        search_id=search_id,
        added_message=added_message
    )

#Check through JSON db connection status
@app.route('/db')
def db_status():
    try:
        connection = get_connection()
        connection.close()
        return jsonify({
            'ok': True,
            'message': 'Connected to DB successfully'
        })
    except Exception as err:
        return jsonify({
            'ok': False,
            'error': str(err)
        }), 500

#See all candies
@app.route('/candies')
def list_candies():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM chuches ORDER BY id')
        candies = cursor.fetchall()

        cursor.close()
        connection.close()

        return jsonify(candies)
    except Exception as err:
        return jsonify({
            'ok': False,
            'error': str(err)
        }), 500

#See one candy
@app.route('/candies/<int:candy_id>')
def get_candy(candy_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            'SELECT * FROM chuches WHERE id = %s',
            (candy_id,)
        )

        candy = cursor.fetchone()

        cursor.close()
        connection.close()

        if candy is None:
            return jsonify({
                'error': 'Candy not found'
            }), 404
        return jsonify(candy)
    except Exception as err:
        return jsonify({
            'ok': False,
            'error': str(err)
        }), 500

#Insert new candy into db. TODO: Create HTML
@app.route('/candies', methods=['POST'])
def add_candy():
    name = request.form.get('nombre')
    desc = request.form.get('descripcion')

    if not name or not desc:
        return jsonify({
            'error': 'No name or description added',
        }), 400
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            'INSERT INTO chuches (nombre, descripcion) VALUES (%s, %s)',
            (name, desc)
        )
        connection.commit()

        new_id = cursor.lastrowid

        cursor.close()
        connection.close()

        return redirect(url_for('get_candy', candy_id = new_id))
    except Exception as err:
        return jsonify({
            'ok': False,
            'error': str(err)
        }), 500

#If u have two or more flask projects, port must be changed in order to see the project when run
if __name__ == '__main__':
    app.run(debug=True, port=5001)