from flask import Flask
from map_generation import map_generation


app = Flask(__name__)

map2 = map_generation()
map = map2.generate()

@app.route("/state")
def test():
    return map

@app.route("/move")
def move():
    # # get current human colony
    # check if new != empty
    #     add new to colony list

    # # get recommendations for next planet to colonize
    # scores, best = recommender(map) 
    # # add best planet to human colony
    # add best candidate to new
    # # return the new human colony to frontend
    # return 



