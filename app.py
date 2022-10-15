from flask import Flask



app = Flask(__name__)

@app.get("/")
def pokemon_list():
    return "Charmander, pikachu, eevee, bulbasaur, diglett"


@app.get("/bulbasaur")
def bulbasaur_data():
    return "This is bulbasaur, a generation 1 pokemon who looks like a little dinosaur"


@app.get("/charmander")
def charmander_data():
    return "This is charmander, who looks like a little reptile"


@app.get("/pikachu")
def pikachu_data():
    return "This is pikachu, who looks like a little rodent"


@app.get("/eevee")
def eevee_data():
    return "This is eevee a generation 1 pokemon, who looks like a little fox"



@app.get("/diglett")
def diglett_data():
    return "This is diglett, a generation 1 pokemon, who looks like a little mole."


if __name__ == "__main__":
    app.run()
