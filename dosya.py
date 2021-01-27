from flask import Flask, jsonify, request
import json


app = Flask(__name__)

def okulan():
    r = open(r"data.json", "r", encoding="UTF-8").read()
    r = json.loads(r)

    return r

def arakardes(key):
    data = okulan()

    bulundu = list()

    for _ in data:
        if key in _["search"]:
            bulundu.append(_)

    return bulundu
            

@app.route("/stations")
def stations():
    return jsonify(okulan())

@app.route("/arama", methods=["GET"])
def ara():
    key = request.args.get("search")
    
    kim_o = request.headers.get('kim_o')

    if kim_o == "lps-project":

        result = arakardes(key)
        return jsonify(result)
    return "kusura kalma kardeş giremezsin"


if __name__ == "__main__":
    app.run(debug=True)
