from flask import Flask
from flask_cors import CORS
from user import user

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, supports_credentials=True)
# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

#注册蓝图
app.register_blueprint(user)

if __name__ == '__main__':
    # app.run(debug=True,port=4000)
    app.run(debug=True,port=4000,use_reloader=False)