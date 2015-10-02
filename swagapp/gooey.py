from flask import Flask, render_template
from imdbchecker import  movie_finder

app = Flask(__name__)


@app.route('/')
def home():
    """
    loads homepage
    """

    return render_template('main.html')


@app.route("/data")
def data_page():

    data = movie_finder('big')

    # pass the data to the template
    return render_template('data.html', data=data)


if __name__ == '__main__':
    app.run()
