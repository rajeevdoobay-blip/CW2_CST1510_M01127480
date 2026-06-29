import pandas as pd
def migrate_cyber_incidents(connection):
    data = pd.read_csv('DATA/cyber_incidents.csv')
    data.to_sql('cyber_incidents', connection)


def get_all_cyber_incidents(connection):
    sql = 'SELECT * FROM cyber_incidents'
    data = pd.read_sql(sql, connection)
    connection.close()
    return data