import pyodbc

def return_connection_sql():
    server = 'localhost'
    database = 'My_database'
    string_conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';Trusted_Connection=yes;'
    conexao = pyodbc.connect(string_conexao)
    return conexao.cursor()
    
response = return_connection_sql()
try:
    print(f'Conectado ao banco de dados com sucesso:{response}')
except Exception as e:
    print(e)
    
for driver in pyodbc.drivers():
    print(driver)
    
 def execute_query(query):
    cursor = return_connection_sql()
    return cursor.execute(query)

query_info = "SELECT * FROM HumanResources.Department"
table = execute_query(query_info)

for row in table:
    print(row)
