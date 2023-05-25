from flask import request
from flask_restful import Resource, reqparse
import sqlite3

class Violations(Resource):
    parser = reqparse.RequestParser()
    
    def post(self):
        # Parse the arguments from the request
        args = request.args
        id = args.get("id", None)
        name = args.get("name", None)
        lic = args.get("lic", None)
        timestamp = args.get("timestamp", None)
        loc_x = args.get("loc_x", None)
        loc_y = args.get("loc_y", None)

        # Check if both loc_x and loc_y are not provided
        if loc_x == loc_y == None:
            return {"message": "Bad Request, no params specified"}, 500
        
        # Establish a connection to the SQLite database
        connection = sqlite3.connect("sample.db")
        cursor = connection.cursor()
        
        # Define the SQL query to insert the violation into the database
        query = "INSERT INTO violations VALUES (?,?,?,?,?,?)"

        try:
            # Execute the query with the provided values
            res = cursor.execute(query, (id, name, lic, timestamp, loc_x, loc_y))
        except BaseException as msg:
            # Handle any errors that occur while accessing the database
            return {"message": "An error occurred while accessing the database"}, 500
        
        # Commit the transaction and close the database connection
        connection.commit()
        connection.close()

