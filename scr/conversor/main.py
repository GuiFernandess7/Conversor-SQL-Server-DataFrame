class ConnectionSQL:

    # Método Construtor
    def __init__(self, server, database, string_connection):
        self.server = server
        self.database = database
        self.string_connection = string_connection
        self.connection = pyodbc.connect(self.string_connection)
        self.connection.add_output_converter(-151, handle_datetime_info)

    # Status de conexão com o servidor
    def connetion_status(self):
        self.cursor = self.connection.cursor()
        try:
            self.response = (f'SQL Server conectado com sucesso: {self.cursor}')
            return self.response
        except Exception as E:
            print(f'Erro de conexão: {E}')
        

    # Leitura da query e retorno do DataFrame
    def read_query(self, query, read_key):

        df = pd.read_sql_query(query, read_key)
        return df
    

# Lidando com datas em DataFrames
def handle_datetime_info(datetime):
    return str(datetime)

# Converter query criada para arquivo excel
def convert_to_excel_file(query):
    path = access_path()
    xlsx_file = query.to_excel(path, index=False, header=True)
    

def main():

    # Configurações de conexão
    server = return_connetion_info()[0]
    database = return_connetion_info()[1]
    string_connection = return_connetion_info()[2]
    conn = ConnectionSQL(server, database, string_connection)
    connection_test = conn.connetion_status()
    print(connection_test)

    key = conn.__dict__['connection']
    try:
        # Para ver todas as tabelas do banco de dados
        all_tables = conn.read_query("SELECT schema_name(t.schema_id) as schema_name, t.name as table_name FROM sys.tables t ORDER BY schema_name, table_name;", key)
        # print(all_tables)

        # ALTERE AQUI
        query1 = conn.read_query('SELECT * FROM Person.Password', key)
        #print(query1)
        convert_to_excel_file(query1)
        
    except Exception as E:
        print(f'Erro de leitura: {E}')
    


if __name__ == '__main__':
    
    import pyodbc
    from connection_info import return_connetion_info
    from path import access_path
    import pandas as pd

    main()
