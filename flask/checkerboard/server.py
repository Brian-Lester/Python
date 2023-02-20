from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def checkerboard():
    return render_template('index.html', num=4)


@app.route("/<int:num>")
def checkerboard_1(num):
    return render_template('index.html', num=num, num1=2)

@app.route("/<int:num>/<int:num1>")
def checkerboard_2(num,num1):
    return render_template('index.html', num=int(num/2), num1=int(num1/2))


@app.route("/<int:num>/<int:num1>/<color3>")
def checkerboard_4(num,num1,color3,):
    return render_template('index.html', num=int(num/2), num1=int(num1/2),color3=color3)


@app.route("/<int:num>/<int:num1>/<color3>/<color4>")
def checkerboard_3(num,num1,color3,color4):
    return render_template('index.html', num=int(num/2), num1=int(num1/2),color3=color3,color4=color4)














if __name__=="__main__":
    app.run(debug=True)  