from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        message = request.get_json().get("events")[0]
        print(message)
        return "succeed"
    elif request.method == "GET":
        return "succeed"
    else:
        return "succeed"

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=5000,debug=True, use_reloader=False)

