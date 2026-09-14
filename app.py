from flask import Flask
from flask import render_template

from ascii_converter import generateAscii

app = Flask(__name__)

@app.route('/')
def hello():
    ascii_art = generateAscii("ascii-pineapple.jpg")
    return render_template('index.html', output=ascii_art) 

if __name__ == "__main__":
    app.run()