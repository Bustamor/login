from flask_app import app
from flask_app.controllers import user_controller


#remember to import controllers

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5001)