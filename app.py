from flask import Flask, jsonify, request

app = Flask(__name__)

alunos = [
{
'id': 1,
'nome': 'Fabiano',
'sobrenome': 'Ferreira',
'ativo':True
},

{
'id': 2,
'nome': 'Henrique',
'sobrenome': 'Magalhaes',
'ativo':True
},

{
'id': 3,
'nome': 'Darilson ',
'sobrenome': 'Cassiano',
'ativo':False
},
]

#Consultar (Todos)
@app.route('/alunos', methods =['GET'])

def obter_alunos():

    if not alunos:
     return jsonify([])
   
    return jsonify(alunos)

#Consultar(id)
@app.route('/alunos/<int:id>', methods =['GET'])
def obter_alunos_por_id(id):
    for aluno in alunos:
       if aluno.get('id') == id:
           return jsonify(aluno)
       

#Edidar 
@app.route('/alunos/<int:id>', methods =['PUT'])
def editar_aluno_por_id(id):
    #Para obter a informação enviada do usuario para api usar o request.getjson
   aluno_alterado = request.get_json()
   for indice, aluno in enumerate(alunos):
       # Verificar se o aluno  id é igual ao id que for passado
      if aluno.get('id') == id:
          alunos[indice].update(aluno_alterado) 
          return jsonify(alunos[indice])

#Criar
@app.route('/alunos',methods =['POST'])
def incluir_novo_aluno():
    novo_aluno = request.get_json()
    alunos.append(novo_aluno)
    return jsonify(alunos), 201
if __name__== '__main__':
    app.run()


#Excluir por id
@app.route('/alunos/<int:id>', methods=['DELETE'])
def excluir_aluno(id):
    for indice, aluno in enumerate(alunos):
        if aluno.get('id')== id:
            del alunos[indice]

    return jsonify(alunos)

# Alterar Status por ID
@app.route('/alunos/<int:id>/status', methods=['PUT'])
def alterar_status_por_id(id):
    aluno_encontrado = None
    for aluno in alunos:
        if aluno.get('id') == id:
            aluno_encontrado = aluno
            break

    if aluno_encontrado is None:
        return jsonify({'message': 'Aluno não encontrado'}), 404

    # Para obter a informação enviada do usuário para a API, usar request.get_json()
    dados_alteracao = request.get_json()
    status_aluno = dados_alteracao.get('ativo')

    if status_aluno is None:
        return jsonify({'message': 'Campo "ativo" não fornecido'}), 400

    aluno_encontrado['ativo'] = status_aluno
    return jsonify(aluno_encontrado)

app.run(port=5000,host='localhost',debug=True)
