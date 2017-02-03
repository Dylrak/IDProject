import psycopg2


def authenticate(uID):
    string_uID = "%s,%s,%s,%s" % (str(uID[0]), str(uID[1]), str(uID[2]), str(uID[3]))
    try:
        conn=psycopg2.connect("dbname='Sportschool' user='postgres' host='192.168.1.2' password='omgidpomg'")
    except Exception as e:
        print(e)
        return False
    cur = conn.cursor()
    try:
        cur.execute("SELECT datuminschrijving FROM klantlidmaatschap WHERE nfcid = '%s' AND (datumuitschrijving IS NULL OR datumuitschrijving < current_date);", string_uID)  # Using this query,
        # any values returned will indicate that the user is authenticated.
    except Exception as e:
        print(e)
        return False
    authenticated = False
    try:
        if cur.fetchone() is not None:  # fetchone is a method used to fetch the results of the execute statement above.
            # It either returns the date of an active subscription, None when it's empty
            # and throws a ProgrammingError if the execute command found absolutely nothing.
            authenticated = True
    except psycopg2.ProgrammingError:
        print("Query returned no results, user is unknown.")
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
    return authenticated

def addCustomer(data):
    try:
        conn=psycopg2.connect("dbname='Sportschool' user='postgres' host='192.168.1.2' password='omgidpomg'")
        dat = conn.cursor()
        command = "INSERT INTO klant (nfcid, voornaamklant, achternaamklant, emailadresklant, iban, geboortedatum, straatnaam, huisnummer, plaats, postcode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        print(command % data)
        dat.execute(command, data)
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        dat.close()
        conn.close()

def addAccount(data):
    try:
        conn=psycopg2.connect("dbname='Sportschool' user='postgres' host='192.168.1.2' password='omgidpomg'")
        dat = conn.cursor()
        command = "INSERT INTO account (gebruikersnaam, wachtwoord, nfcid) VALUES (%s, %s, %s);"
        print(command % data)
        dat.execute(command, data)
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        dat.close()
        conn.close()