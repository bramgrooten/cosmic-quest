from flask import Flask


app = Flask(__name__)



@app.route("/move")
def move():
    # get current human colony

    # get recommendations for next planet to colonize

    # add best planet to human colony

    # return the new human colony to frontend