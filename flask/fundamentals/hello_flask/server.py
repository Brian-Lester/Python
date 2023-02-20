from flask import Flask 
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/success')
def success():
    return "success"

@app.route('/hello/<string :name>/<int : num>')
def name1(name, num):
    return f"hello {name * num }"
if __name__=="__main__":
    app.run(debug=True)  