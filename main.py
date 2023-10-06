from flask import Flask
from public import public
from admin import admin
from employer import employer
from employees import employees

app=Flask(__name__)
app.secret_key="vb"
app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(employer,url_prefix='/employer')
app.register_blueprint(employees,url_prefix='/employees')
app.run(debug=True,port=5083)

