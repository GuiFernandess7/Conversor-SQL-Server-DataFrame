from config import info

def return_connetion_info():
    # Insira seu servidor e banco de dados aqui
    server = info[0]
    database = info[1]
    
    # Altere a versão do sql server se necessário
    string_conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';Trusted_Connection=yes;'
    return server, database, string_conexao
