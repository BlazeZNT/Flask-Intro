# Put your app in here.
from operations import add
from operations import sub
from operations import mult
from operations import div
from flask import Flask, request


app = Flask(__name__)

@app.route("/add")
def add_nums():
    a = int(request.args.get("a",0))
    b = int(request.args.get("b",0))
    new_num = add(a,b)
    return str(new_num)

@app.route("/sub")
def sub_nums():
    a = int(request.args.get("a",0))
    b = int(request.args.get("b",0))
    new_num = sub(a,b)
    return str(new_num)

@app.route("/mult")
def mult_nums():
    a = int(request.args.get("a",0))
    b = int(request.args.get("b",0))
    new_num = mult(a,b)
    return str(new_num)

@app.route("/div")
def div_nums():
    a = int(request.args.get("a",0))
    b = int(request.args.get("b",0))
    new_num = div(a,b)
    return str(new_num)

operations = {
    "add" : add,
    "sub" : sub,
    "mult" : mult,
    "div" : div
}

@app.route("/math/<oper>")
def do_all(oper):
    print(oper)
    a = int(request.args.get("a",0))
    b = int(request.args.get("b",0))
    result = operations[oper](a,b)
    return str(result)
    
    
    
    
