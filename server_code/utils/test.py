from flask_restful import Api, Resource

class Akhilesh_get(Resource):
    def get(self):
        return {"status" : "True"}
