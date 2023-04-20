from flask import request
from flask_restful import Resource, reqparse
import sqlite3

class Location(Resource):
    parser = reqparse.RequestParser()
    def get(self):
        args = request.args
        loc_x = args.get("loc_x", None)
        loc_y = args.get("loc_y", None)

        if loc_x == loc_y ==None:
            return {"message":"Bad Request, no params specified"}, 500
        
        connection = sqlite3.connect("sample.db")
        cursor = connection.cursor()
        query = "SELECT speed FROM location WHERE loc_x=? AND loc_y=?"

        try:
            res = cursor.execute(query, (loc_x, loc_y))
        except BaseException as msg:
            return {"message":"An error occured while accessing database"}, 500
        
        val = res.fetchone()
        connection.commit()
        connection.close()
        
        if val:
            return {"speed_limit":val[0]}, 200
        else:
            return {"message":"Given location is not registered"}, 201



