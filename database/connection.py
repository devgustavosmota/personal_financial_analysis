import psycopg

def get_connection():
    return psycopg.connect(
        host='localhost',
        dbname='personal_financial_analysis',
        user='postgres',
        password='059411',
        port=5432
    )
