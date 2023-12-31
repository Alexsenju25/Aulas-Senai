import mysql.connector.connection

config = {
    'user': 'root',
    'password': 'senai',
    'host': 'localhost',
    'database': 'loja_ii'
}

# Estabelecer a conexão com o banco de dados
conexao = mysql.connector.connect(**config)

# Criar um cursor para executar consultas SQL
cursor = conexao.cursor()

# Exemplo de consulta SQL
selecionarDB = "use loja_ii;"
consulta = "SELECT * FROM clientes"
 
# Executar a consulta
cursor.execute(selecionarDB)
cursor.execute(consulta)

# Recuperar os resultados
resultados = cursor.fetchall()

# Imprimir os resultados
for linha in resultados:
    print(linha)

# Fechar o cursor e a conexão
cursor.close()
conexao.close()