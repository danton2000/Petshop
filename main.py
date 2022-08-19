from flask import Flask, render_template

app = Flask(__name__)

#lista de produtos
lista_produtos = [
    {
        "nome_produto": "Comida para cães",
        "url_link": "comida_para_caes",
        "destaque": '2'
    },
    {
        "nome_produto": "Comida para gatos",
        "url_link": "comida_para_gatos",
        "destaque": '2'
    },
    {
        "nome_produto": "Coleira Bacana",
        "url_link": "coleira_bacana",
        "destaque": '1'
    }
]
#lista de servicos
lista_servicos = [
    {
        "nome_servico": "Banho",
        "url_link": "banho",
        "destaque": '2'
    },
    {
        "nome_servico": "Massagem",
        "url_link": "massagem",
        "destaque": '2'
    },
    {
        "nome_servico": "Creche",
        "url_link": "creche",
        "destaque": '1'
    }
]

produto_detalhes = {
    'comida_para_caes': {
        'nome': 'Comida para Cães',
        'descricao': 'Coleira para cachorros bacanas',
        'valor': 'R$ 10,50'
    },
    'comida_para_gatos': {
        'nome': 'Comida para Gatos',
        'descricao': 'Coleira para gatos bacanas',
        'valor': 'R$ 50,00'
    },
    'coleira_bacana': {
        'nome': 'Coleira',
        'descricao': 'Uma ótima coleira para o seu Pet :)',
        'valor': 'R$ 2,99'
    },
}

servico_detalhes = {
    'banho': {
        'nome': 'Banho',
        'descricao': 'Banho para o seu Pet prediléto',
        'valor': 'R$ 50,50'
    },
    'massagem': {
        'nome': 'Massagem',
        'descricao': 'Massagem excelete para o seu Pet',
        'valor': 'R$ 100,00'
    },
    'creche': {
        'nome': 'Creche',
        'descricao': 'Um otimo ambiente para o seu Pet',
        'valor': 'R$ 200,00'
    },
}

@app.route("/")
def index():
    return render_template("index.html", produtos=lista_produtos, servicos=lista_servicos)

@app.route("/produtos/")
def produtos():
    return render_template("produtos.html", produtos=lista_produtos)

@app.route("/produtos/<nome_produto>/detalhes")
def produtos_detalhes(nome_produto):
    return render_template("produto.html", produto=produto_detalhes[nome_produto])

@app.route("/servicos/")
def servicos():
    return render_template("servicos.html", servicos=lista_servicos)

@app.route("/servicos/<nome_servico>/detalhes")
def servicos_detalhes(nome_servico):
    return render_template("servico.html", servico=servico_detalhes[nome_servico])