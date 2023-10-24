from flask import Flask
import sys


app = Flask(__name__)
try:
    global data_obj
    data_obj = open("./data.obj", 'r+')
except:
    data_obj = open("./data.obj", 'w+')


try:
    global num
    num = int(data_obj.read())
except:
    num = 0

@app.route("/")
def numH(): 
    num = getNum()
    return {"msg": num}

def saveNum():
    data_obj.write(str(num))
    

def getNum():
    global num
    num += 1
    return num

if __name__ == "__main__":
    app.run()
    saveNum()
        