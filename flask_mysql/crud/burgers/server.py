from flask_app.controllers import burgers_controller
# ...server.py

from flask_app import app
# ...server.py


if __name__=="__main__":
    app.run(debug=True)