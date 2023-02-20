from flask import Flask, render_template 


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", phrase="hello", times=5)


@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def say_name(name):
    return f'Hi {name}!'

@app.route('/repeat/<int:num1>/<string:name1>')
def repeat(num1, name1):
    return name1 * num1









@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
        {'name' : 'Michael', 'age' : 35},
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]
    return render_template("index.html", random_numbers = [3,1,5], students = student_info)

if __name__=="__main__":
    app.run(debug=True)  