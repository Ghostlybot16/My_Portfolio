#Importing Modules
from flask import Flask

#This creates the web application on the web
#Starts up the local host page and displays all the code 
app = Flask(__name__)

#This is a URL route to a specific page 
@app.route("/home")
def hello():
    return "Hello Kramptj"

if __name__ == "__main__":
    app.run()
