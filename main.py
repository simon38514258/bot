from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return 'succeed'

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000,debug=True, use_reloader=False)

