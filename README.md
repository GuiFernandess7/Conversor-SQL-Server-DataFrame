# PYODBC-SQL_Server

## AVISO: Repositório ainda em desenvolvimento

 Nos últimos anos, a linguagem python tem se tornado uma das linguagens de programação mais populares e vem ganhando espaço nas grandes empresas. Sua eficiência em diversas áreas como linguagem de máquina (machine learning), criptomoedas, desenvolvimento de jogos e desenvolvimento web expandiu os horizontes para desenvolvedores profissionais e abriu portas para a entrada de novos programadores nesse mercado em ascensão. Contudo, sua fama começou dentro da área de ciência de dados e em processos de automação.

<p align="center">
  <img src="Img/pic01.png" >
</p>
 
 Python pemite acessar diversos gerenciadores como Oracle, Sqliter, MySQL, Postgresql e SQL Server. A seguir estão os primeiros códigos para criar uma conexão com o servidor do SQL Server.
 
 ```
 import pyodbc
 ```
```
def return_connection_sql():
    server = 'localhost'
    database = 'My_database'
    string_conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';Trusted_Connection=yes;'
    conexao = pyodbc.connect(string_conexao)
    return conexao.cursor()
```
```
response = return_connection_sql()
try:
    print(f'Conectado ao banco de dados com sucesso:{response}')
except Exception as e:
    print(e)
```
 Esse repositório é voltado para:
 
 * **Acesso ao banco de dados SQL Server e conversão para DataFrames Pandas (Acesse scr)**
 * **Conversão de dataframes para arquivos excel e criação de gráficos com matplotlib (scr e Jupyter Notebook)**
 * **Automação de arquivos excel por meio de novos bancos de dados (Acesse scr)**

 Backup do banco de dados utilizado (AdventureWorks2017.bak): https://bit.ly/3oaLJCm
