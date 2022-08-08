from flask import Flask,request
from teste import inserir
#from predicao import execusoes

app = Flask("teste")

@app.route("/predicao", methods=["POST"])
def predicao():
    body = request.get_json()
    inserir(body)
    return body

app.run()