#Importing Modules
from flask import Flask #Import Flask
from flask import render_template #Allows me to render HTML pages

#This creates the web application on the web
#Starts up the local host page and displays all the code 
app = Flask(__name__)

#This is a URL route to a specific page 
@app.route("/")
def index():
    #This sets the title tag in the HTML file as whatever value is within the full_name variable
    #In this case it is my name
    #Using Flask filters
    full_name = "Kramptj KC" 
    return render_template("portfolio.html", full_name=full_name)

@app.route("/user/<name>")
def user(name):
    return f"Hello {name}"

if __name__ == "__main__":
    app.run()
