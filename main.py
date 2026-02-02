from flask import Flask,render_template,request,redirect,url_for,session
#create a flask app
app=Flask(__name__)
#secret key
app.secret_key="PurpleMaryland"
#store user data
users={}
#home page
@app.route("/")
def home():
    #check if username is stored
    if "username" in session:
        #redirect to dashboard
        return redirect(url_for("dashboar"))
    #display the home page
    return redirect(url_for("login"))
#signup
@app.route("/signup",methods=["GET", "POST"])
def signup():
    error=None
    if request.method=="POST":
        #get the username and password from html form
        username=request.form["username"]
        password=request.form["password"]
        #username is already used
        if username in users:
            error="Username Exists try again"
        else:
            users[username]=password #assogning the password to the username
            session["username"]=username#create a storage for the username with the password
            #access the dashboard
            return redirect(url_for("Dashboard"))
        return render_template("signup.html",error=error)
#login function
@app.route("/login",methods=["GET","POST"])
def login():
    error=None
    if request.method=="POST":#Sending data to the server
        username=request.form["username"]
        password=request.form["password"]
        #username is not registered
        if username not in users:
            errors="Account not found"
        elif users[username]!=password:
            errors="wrong password"
        else:
            #correct username and password
            session["username"]=username#accessing the username
            #redirect to dashboard
            return redirect(url_for("dashboard"))
    return render_template("login.html",error=error)
#dashboard function
@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        #return to home page
        return redirect(url_for("login"))
    return render_template("dashboard.html",username-session["username"])
#logout function
@app.route("/logout")
def logout():
    #close the session
    session.pop("username",None)
    return redirect(url_for("login"))#takes back to login page
#run the flask app
if __name__=="__main__":
    app.run(debug=True)
    