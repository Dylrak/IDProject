import psycopg2


try:
    conn=psycopg2.connect("dbname='Sportschool' user='postgres' host='192.168.1.2' password='omgidpomg'")
except:
    print("Cannot connect to the database!")
