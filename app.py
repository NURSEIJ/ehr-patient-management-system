from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

def get_db_connection():
    try:
        return mysql.connector.connect(
            host='localhost',
            user='root',
            password='130787JULbc#',
            database='ehr_system'
        )
    except mysql.connector.Error as err:
        print(f'Error: {err}')
        return None

@app.route('/')
def home():
    return jsonify({'message': 'Server working! ✅'})

@app.route('/api/patients')
def get_patients():
    conn = get_db_connection()
    if not conn:
        return jsonify({'error': 'DB connection failed'}), 500
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM patients')
        return jsonify(cursor.fetchall())
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == '__main__':
    print('🚀 Server starting...')
    app.run(debug=True, port=5000)