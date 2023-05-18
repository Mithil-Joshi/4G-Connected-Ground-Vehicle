from flask import request
from flask_restful import Resource, reqparse
import sqlite3

class Violations(Resource):
    parser = reqparse.RequestParser()
    def post(self):
        args = request.args
        id=args.get("id", None)
        name = args.get("name", None)
        lic = args.get("lic", None)
        timestamp = args.get("timestamp", None)
        loc_x = args.get("loc_x", None)
        loc_y = args.get("loc_y", None)

        if loc_x == loc_y ==None:
            return {"message":"Bad Request, no params specified"}, 500
        
        connection = sqlite3.connect("sample.db")
        cursor = connection.cursor()
        query = "INSERT INTO violations VALUES (?,?,?,?,?,?)"

        try:
            res = cursor.execute(query, (id,name, lic, timestamp, loc_x, loc_y))
        except BaseException as msg:
            return {"message":"An error occured while accessing database"}, 500
        
        
        connection.commit()
        connection.close()
        '''
        if val:
            return {"speed_limit":val[0]}, 200
        else:
            return {"message":"Given location is not registered"}, 201
    '''
    
    