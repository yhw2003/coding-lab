from flask import Flask

app = Flask(__name__)

num = 0

@app.route("/")
def numH(): 
    global num
    num += 1
    return {"msg": num}


if __name__ == "__main__":
    app.debug = True
    app.run()