import pymongo
from django.conf import settings
import json

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        client = pymongo.MongoClient(settings.MONGO_URI)
        db = client.get_database()
        collection = db.get_collection('requests_logs')

        try:
            body = json.loads(request.body)
        except:
            body = {}

        collection.insert_one({
            'method': request.method,
            'path': request.path,
            'headers': dict(request.headers),
            'body': body,
        })

        response = self.get_response(request)

        return response