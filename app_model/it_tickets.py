import pandas as pd
def migrate_it_tickets(connection):
    data = pd.read_csv('DATA/it_tickets.csv')
    data.to_sql('it_tickets', connection)
   

def get_all_it_tickets(connection):
    sql = 'SELECT * FROM it_tickets'
    data = pd.read_sql(sql, connection)
    connection.close()
    return data
