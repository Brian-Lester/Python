from flask_app import app

from flask_app.controllers import band_controller, login_reg_controller




if __name__=="__main__":
    app.run(debug=True)