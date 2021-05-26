from flask_restful import Api, Resource

class hi(Resource):
    def get(self):
        return {"status" : "True"}