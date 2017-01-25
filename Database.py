import psycopg2


try:
    conn=psycopg2.connect("dbname='Sportschool' user='Postgres' password='omgidpomg'")
except:
    print("I am unable to connect to the database.")
