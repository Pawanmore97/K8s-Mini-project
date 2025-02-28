from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def welcome_msg():
    if request.method == "POST":
        name = request.form.get("name")
        return render_template("index.html", name=name) 
    return render_template("index.html", name=None)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)