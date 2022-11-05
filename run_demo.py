from flask import Flask
from map import Map


app = Flask(__name__)

map = Map()
#map.generate()


@app.route("/move")
def move():
    # load json of map
    map = json.load("map.json" Map)

    # get current human colony
    check if new != empty
        add new to colony list

    # get recommendations for next planet to colonize
    scores = recommender() 
    # add best planet to human colony
    add best candidate to new
    # return the new human colony to frontend
    return 

