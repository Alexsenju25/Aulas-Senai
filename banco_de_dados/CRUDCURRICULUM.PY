import mysql.connector

# Conectar ao banco de dados
conn = mysql.connector.connect(
    host ='localhost', 
    user = 'root', 
    password = 'senai',
    database = 'banco_de_talentos'
)

cursor = conn.cursor()



#Função para inserir dados na tabela cliente

def inserir_candidato(idcandidato, email, cpf, linkdl, github, nome):
    query = 'INSERT INTO inserir_candidato(idcandidato, email, cpf, linkdl, github, nome) VALUES (%s, %s, %s, %s, %s, %s)'
    values = (idcandidato, email, cpf, linkdl, github, nome)
    cursor.execute(query, values)
    conn.commit()

#Função para listar todos os clientes

def listar_candidato():
    cursor.execute('SELECT * FROM banco_de_talentos')
    candidato = cursor.fetchall()
    for candidato in cliente:
        print(clientes)

#Função para atualizar a tabela cliente_vip

def atualizar_cliente_vip(idcliente, nome, endereco, telefone, email, cpf):
    query = 'UPDATE cliente_vip SET nome = %s, endereco = %s, telefone = %s, email=%s, cpf=%s WHERE idcliente = %s'
    values = (nome, endereco, telefone, email, cpf, idcliente)
    cursor.execute(query, values)

#Função para deletar um cliente

def delete_cliente(idcliente):
    query= 'DELETE FROM cliente_vip WHERE idcliente = %s'
    values = (idcliente)
    cursor.execute(query, values)
