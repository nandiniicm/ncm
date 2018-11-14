from flask import Flask, render_template, request
from empdata import Employee
app=Flask(__name__)
getEmployee = Employee()

@app.route('/')
def index():
    return render_template('home.html')
@app.route('/home')
def home():
    return render_template('home.html') 
@app.route('/empdata') 
def empdata():
    return render_template('empdata.html', employeeList=getEmployee)


if(__name__=='__main__'):
    app.run(debug=True)