import os
import psycopg2


from app.utilities.db.tables import queries, droppings


def dbconnection():
    """making a connection to the db"""
    return psycopg2.connect("dbname=mydb user=postgres password=postgres")


def initializedb():
    try:
        """starting the database"""
        connection = dbconnection()
        connection.autocommit = True

        """activate cursor"""
        cursor = connection.cursor()
        for query in queries:
            cursor.execute(query)
        connection.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print("DB Error")
        print(error)

