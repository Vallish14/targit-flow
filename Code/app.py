from flask import *
import os

app = Flask(__name__) 

def does_assest_exist(asset):
    return os.path.isfile(f"./static/{asset}")

@app.route("/") 

@app.route("/home")
def home():
    asset = "home.html"
    if not does_assest_exist(asset):
        return false 
    return render_template(asset)

@app.route("/account", methods=["POST", "GET"])
def account():
    usr = "<User Not Defined>" 
    if (request.method == "POST"): 
        usr = request.form["name"] 
        if not usr: 
            usr = "<User Not Defined>"
    return render_template("account.html",username=usr) 

if __name__ == "__main__": 
    app.run(debug=True,port=4949) #running flask (Initalised on line 4)
