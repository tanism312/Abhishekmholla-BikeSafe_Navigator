import mysql.connector
from mysql.connector import Error
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', active_page='Home')

@app.route('/safety_insights')
def safety_insights():
    return render_template('safety_insights.html', active_page='Safety Insights')

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/connect_mysql')
def connect_mysql():  # put application's code here
    try:
        # Establish the connection
        connection = mysql.connector.connect(
            user= 'boyu',
            password= '1234567890',
            host = '127.0.0.1',
            database= 'mydatabase')

        if connection.is_connected():
            connection.close()
            return 'MySQL working'
    except Error as e:
        print("Error while connecting to MySQL", e)

if __name__ == '__main__':
    app.run()
