from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def add_numbers():
    if request.method == "POST":
        num = float(request.form["num"])
        if num==0:
            result =""
        if num%2==0 :
            result = "Result : EVEN"
        else:
            result = "Result : ODD"
        
        return render_template("index.html", result=result)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
