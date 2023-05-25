from flask import request
from flask_restful import Resource, reqparse
import sqlite3

class Location(Resource):
    # Define a request parser to parse the incoming request arguments
    parser = reqparse.RequestParser()

    def get(self):
        # Parse the arguments from the request
        args = request.args
        loc_x = args.get("loc_x", None)
        loc_y = args.get("loc_y", None)

        # Check if both loc_x and loc_y are not provided
        if loc_x == loc_y ==None:
            return {"message":"Bad Request, no params specified"}, 500
        
        # Establish a connection to the SQLite database
        connection = sqlite3.connect("sample.db")
        cursor = connection.cursor()

        # Define the SQL query to retrieve the speed for the given location
        query = "SELECT speed FROM location WHERE loc_x=? AND loc_y=?"

        try:
            # Execute the query with the provided loc_x and loc_y values
            res = cursor.execute(query, (loc_x, loc_y))
        except BaseException as msg:
            # Handle any errors that occur while accessing the database
            return {"message":"An error occured while accessing database"}, 500
        
        # Fetch the result of the query
        val = res.fetchone()

        # Commit the transaction and close the database connection
        connection.commit()
        connection.close()
        
        if val:
            # If a value is found for the given location, return the speed limit
            return {"speed_limit":val[0]}, 200
        else:
            # If no value is found for the given location, return an appropriate message
            return {"message":"Given location is not registered"}, 201
