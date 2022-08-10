from flask import Flask,request
from inserir_nova_linha import inserir
from predicao import execusoes

app = Flask("teste")

@app.route("/predicao", methods=["POST"])
def predicao():
    body = request.get_json()

    listOfValues = body.values()
    listOfValues = list(listOfValues)
    inserir(listOfValues)
    re = execusoes()
    print("AOL: ",re)
    return 'OK'

app.run()