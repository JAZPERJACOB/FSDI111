from flask import Flask # From the flask module import the Flask class

app = Flask(__name__) # Create an instance of the Flask into app (now an object)

@app.get("/") # Flask decorator that maps routes to view functions
def index(): # In flask, "wrapped" functions are referred to as "view functions"
    me = { # python dictionary (key-value pairs)
        "first_name": "Jazper",
        "lastName": "Jacob",
        "hobbies": "Basketball",
        "online": True
    }
    
    return me # In flask, when you return a dictionary, it is automatically converted to JSON