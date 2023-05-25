from flask import Flask, render_template, request,redirect
from flask_restful import Api, Resource, reqparse
import sqlite3
from violations import Violations 
from location import Location

# Function to create the location database
def create_loc_db(name):
    connection = sqlite3.connect(name)
    curso = connection.cursor()

    # Create 'location' table if it doesn't exist
    create_table = "CREATE TABLE IF NOT EXISTS location (id INTEGER PRIMARY KEY, loc_x real, loc_y real, speed INTEGER)"
    curso.execute(create_table)

    # Create 'violations' table if it doesn't exist
    create_table = "CREATE TABLE IF NOT EXISTS violations (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, lic INTEGER, timestamp text, loc_x real, loc_y real)"
    curso.execute(create_table)

    connection.commit()
    connection.close()

# Create the location database
create_loc_db("sample.db")

class Item(Resource):
    parse = reqparse.RequestParser()
    parse.add_argument(
        "loc_x",
        type=float,
        required=False,
        help="x coordinate"
    )
    parse.add_argument(
        "loc_y",
        type=float,
        required=False,
        help="y coordinate"
    )
    
    def get(self, name):
        # Parse and retrieve the arguments from the request
        data = Item.parse.parse_args()
        return {"message": data}, 200
    
    def post(self, name):
        # Parse and retrieve the arguments from the request
        data = Item.parse.parse_args()
        return data, 200




app = Flask(__name__)
api = Api(app)
api.add_resource(Location, "/location")
api.add_resource(Violations, "/violation")

@app.route('/')
def display_table():
    # Retrieve data from the 'location' table
    conn = sqlite3.connect('sample.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM location")
    data = cursor.fetchall()
    conn.close()

    # Retrieve data from the 'violations' table
    conn = sqlite3.connect('sample.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM violations")
    data2 = cursor.fetchall()
    conn.close()

    # Pass the data to the template and render it
    return render_template('table.html', data=data, data2=data2)

@app.route('/add_row', methods=['POST'])
def add_row():
    # Retrieve form data from the request
    id = request.form['id']
    loc_x = request.form['loc_x']
    loc_y = request.form['loc_y']
    speed = request.form['speed']

    # Insert the data into the 'location' table
    conn = sqlite3.connect('sample.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO location (id,loc_x,loc_y,speed) VALUES (?, ?, ?, ?)', (id, loc_x, loc_y, speed))
    conn.commit()
    conn.close()

    # Redirect to the main page    
    return redirect('/')


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000, debug=True)
    
