from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template('index.html', num=3)

@app.route('/play/<num>')
def play_times(num):
    return render_template('index.html',num=int(num))

@app.route('/play/<int:num>/<color>')
def change_color(num,color):
    return render_template('index.html',num=num,color=color)








if __name__=="__main__":
    app.run(debug=True)  