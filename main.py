import sqlalchemy as db
import conn_params
import pandas as pd


engine = db.create_engine(conn_params.CONNECTION_STRING)
connection = engine.connect()
metadata = db.MetaData()
flats = db.Table(
    'main',
    metadata,
    autoload=True,
    autoload_with=engine)


def get_table_columns(
    table:db.Table
    ):
    return table.columns.keys()


def select_from_table(
    table:db.Table,
    conn:db.engine.Connection
    ):
    '''EQUIVALENT OF SELECT * FROM ...'''
    query = db.select([table])
    result:db.engine.CursorResult = conn.execute(query)
    result_set = result.fetchall()
    return result_set

def build_dataframe_from_result_set(
    result_set
    ):
    '''result of .fetchall() executed on db.CursorResult'''
    df = pd.DataFrame(
        result_set
    )
    df.columns = result_set[0].keys()
    return df



result_set = select_from_table(
    table=flats,
    conn=connection
)

if __name__ == '__main__':
    engine = db.create_engine(conn_params.CONNECTION_STRING)
    connection = engine.connect()
    metadata = db.MetaData()
    flats = db.Table(
        'main',
        metadata,
        autoload=True,
        autoload_with=engine)
    # df:pd.DataFrame = build_dataframe_from_result_set(result_set)
    filtered_on_piątkowo_query = db.select([flats]).where(
        flats.columns.district == 'piątkowo'
        ).order_by(
            'price')
    results = connection.execute(filtered_on_piątkowo_query)
    result_set = results.fetchall()

    for r in result_set:
        print(r.price, r.title)


    


