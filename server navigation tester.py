# flask create server
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


# requests the return function above
import requests
r = requests.get('https://github.com/timeline.json')
print(r.text)
 
            # The Requests library also comes with a built-in JSON decoder,
            # just in case you have to deal with JSON data
 
import requests
r = requests.get('https://github.com/timeline.json')
print(r.json)

# same as 1st one
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)


# rest serer example
from flask import Flask

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    
    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from Model import db
    db.init_app(app)

    return app


if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)