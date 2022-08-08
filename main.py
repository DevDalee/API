from flask import Flask,request
from teste import inserir
from predicao import execusoes

app = Flask("teste")

@app.route("/predicao", methods=["POST"])
def predicao():
    body = request.get_json()

    listOfValues = body.values()
    listOfValues = list(listOfValues)
    inserir(listOfValues)
    print(len(listOfValues))
    re = execusoes()
    print(re)
    return 'OK'

app.run()