import psycopg2


def authenticate(uID):
    string_uID = "%s,%s,%s,%s" % (str(uID[0]), str(uID[1]), str(uID[2]), str(uID[3]))
    try:
        conn=psycopg2.connect("dbname='Sportschool' user='postgres' host='192.168.1.2' password='omgidpomg'")
    except:
        print("Cannot connect to the database!")
        return False
    cur = conn.cursor()
    try:
        print("SELECT datuminschrijving FROM klantlidmaatschap WHERE nfcid = '%s' AND (datumuitschrijving IS NULL OR datumuitschrijving < current_date);" % string_uID)
        cur.execute("SELECT datuminschrijving FROM klantlidmaatschap WHERE nfcid = '%s' AND (datumuitschrijving IS NULL OR datumuitschrijving < current_date);", string_uID)  # Using this query,
        # any values returned will indicate that the user is authenticated.
    except:
        print("Cannot find valid subscription!")
        return False
    authenticated = False
    try:
        if cur.fetchone() is not None:  # fetchone is a method used to fetch the results of the execute statement above.
            # It either returns the date of an active subscription, None when it's empty
            # and throws a ProgrammingError if the execute command found absolutely nothing.
            authenticated = True
    except psycopg2.ProgrammingError:
        print("Query returned no results, user is unknown.")
    finally:
        cur.close()
        conn.close()
    return authenticated

def addCustomer(data):
    try:
        conn=psycopg2.connect("dbname='Sportschool' user='postgres' host='192.168.1.2' password='omgidpomg'")
        dat = conn.cursor
        dat.execute("INSERT INTO klant (nfcid, iban, geboortedatum, straatnaam, huisnummer, plaats, postcode, voornaamklant, achternaamklant, emailadresklant) VALUES (%s);", data)
        conn.commit()
        conn.close()
    except:
        print("Cannot connect to the database!")
        return False
