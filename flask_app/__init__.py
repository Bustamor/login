from flask import Flask, render_template, redirect, session, flash, request
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "asdlfjdsafjepowjfoleawjfoeqwjfewqofjeqwlkfjas;odfjd;osfjew;ofjewqofjeqwofjewq;"
