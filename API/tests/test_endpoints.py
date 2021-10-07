"""

from flask import Flask
from flask_restx import Resource, Api
import db.db as db 

app = Flask(__name__)
api = Api(app)

@api.route('/hello')
class HelloWorld(Resource):
    """




class EndpointTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(Self):
        pass

    def test_hello(self):
        hello = ep.HelloWorld(Resource)
        ret = hello.get()
        self.assertIsInstance(ret, dict)
        self.assertIn('hello', 'ret)


