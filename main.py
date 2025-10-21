from flask import Flask, redirect, url_for, render_template, request, jsonify
from funcs import validar_cpf
import pandas as pd
import socket, sys, os

base_dir = ""

def resource_path(filename: str) -> str:
    """Retorna o caminho absoluto para recursos, útil quando empacotado com PyInstaller."""
    if getattr(sys, 'frozen', False):
        # Caminho do executável em execução (dist/)
        base_dir = os.path.dirname(sys.executable)
    else:
        # Caminho do script (modo desenvolvimento)
        base_dir = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_dir, filename)

# Caminho do arquivo CSV (gravável e acessível)
arquivo = resource_path("data.csv")

app = Flask(__name__,
            template_folder=resource_path("templates"),
            static_folder=resource_path("static"))

@app.route("/", methods=["GET"])
def index():
    return redirect(url_for("checkin"))

@ app.route("/checkin", methods=["GET"])
def checkin():
    return render_template("checkin_form.html")

@app.route("/buscar", methods=["GET"])
def buscar():
    df = pd.read_csv(arquivo)
    df.columns = df.columns.str.lower()
    dados = df.to_dict(orient="records")
    query = request.args.get("cpf", "")
    resultado = [
        u for u in dados if str(u["cpf"]).startswith(query)
    ]
    return jsonify(resultado)

@app.route("/buscar_pulseira", methods=["GET"])
def buscar_pulseira():
    return render_template("buscar_pulseira.html")

@app.route("/buscar_numero", methods=["GET"])
def buscar_numero():
    df = pd.read_csv(arquivo)
    df.columns = df.columns.str.lower()
    dados = df.to_dict(orient="records")
    query = request.args.get("numeroPulseira", "")
    resultado = [
        u for u in dados if str(u["numero"]).startswith(query)
    ]
    return jsonify(resultado)

@app.route("/checkin_validate", methods=["POST"])
def validate():
    data = request.get_json()
    cpf = str(data.get("cpf"))
    
    df = pd.read_csv(arquivo)
    df.columns = df.columns.str.lower()
    
    # Atualiza a coluna validado
    df.loc[df["cpf"].astype(str) == cpf, "validado"] = "sim"
    df.to_csv(arquivo, index=False)
    
    # Retorna JSON informando que deu certo
    return jsonify({"success": True, "cpf": cpf})

@app.route("/preencher_campos", methods=["POST"])
def preencher_campos():
    try:
        dados = request.get_json(force=True)

        print(dados)

        numero = str(dados.get("numero", "")).strip()
        nome = str(dados.get("nome", "")).strip()
        cpf = str(dados.get("cpf", "")).strip()

        if not numero or not nome or not cpf:
            return jsonify({"mensagem": "Todos os campos são obrigatórios."}), 400

        df = pd.read_csv(arquivo)
        df.columns = df.columns.str.lower()

        mask = df["numero"].astype(str) == numero
        if not mask.any():
            return jsonify({"mensagem": "Número não encontrado no arquivo."}), 404

        df.loc[mask, "nome"] = nome
        df.loc[mask, "cpf"] = cpf
        df.loc[mask, "validado"] = "sim"
        df.to_csv(arquivo, index=False)

        return jsonify({"mensagem": f"Dados do número {numero} atualizados com sucesso!"})

    except Exception as e:
        print("Erro ao processar JSON:", e)
        return jsonify({"mensagem": "Erro ao processar requisição."}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)