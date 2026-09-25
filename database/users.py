from .connection import get_connection

def create_user(email, password_hash, name):

    connection = get_connection()

    with connection.cursor() as cursor:

        cursor.execute(
            '''
            INSERT INTO users (email, password_hash, name)
            VALUES (%s, %s, %s)
            ''',
            (email, password_hash, name)
        )

    connection.commit()
    connection.close()

def get_user_by_email(email):

    connection = get_connection()

    with connection.cursor() as cursor:

        cursor.execute(
            '''
            SELECT id, email, password_hash, name
            FROM users
            WHERE email = %s
            ''',
            (email,)
        )

        user = cursor.fetchone()

    connection.close()

    return user
