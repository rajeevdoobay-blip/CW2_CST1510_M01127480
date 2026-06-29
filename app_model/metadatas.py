def migrate_datasets_metadata(connection):
    data = pd.read_csv('DATA/datasets_metadata.csv')
    data.to_sql('datasets_metadata', connection)

def get_all_datasets_metadata(connection):
    sql = 'SELECT * FROM datasets_metadata'
    data = pd.read_sql(sql, connection)
    connection.close()
    return data