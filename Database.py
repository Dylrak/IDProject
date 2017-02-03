import psycopg2


def authenticate(uID):
    try:
        conn=psycopg2.connect("dbname='Sportschool' user='postgres' host='192.168.1.2' password='omgidpomg'")
    except Exception as e:
        print(e)
        return False
    cur = conn.cursor()
    try:
		print("SELECT datuminschrijving FROM klantlidmaatschap WHERE nfcid = '%s' AND (datumuitschrijving IS NULL OR datumuitschrijving < current_date);" % uID)
		cur.execute("SELECT datuminschrijving FROM klantlidmaatschap WHERE nfcid = %s AND (datumuitschrijving IS NULL OR datumuitschrijving < current_date);", (uID,))  # Using this query,
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

def customerDevice(deviceID, uID):
    try:
        conn = psycopg2.connect("dbname='Sportschool' user='postgres' host='192.168.1.2' password='omgidpomg'")
        dat = conn.cursor()
        dat.execute("SELECT begintijd FROM klantapparaat WHERE nfcid = %s AND eindtijd IS NULL", uID)
        ingecheckt = dat.fetchone()
        if ingecheckt is not None:
            dat.execute("UPDATE klantapparaat SET eindtijd=LOCALTIMESTAMP(0) WHERE nfcid = %s AND begintijd=%s", (uID, ingecheckt))
        else:
            print("INSERT INTO klantapparaat (nfcid, apparaatid, begintijd, eindtijd) VALUES ('%s', '%s', LOCALTIMESTAMP(0), NULL)" % (uID, deviceID))
            dat.execute("INSERT INTO klantapparaat (nfcid, apparaatid, begintijd, eindtijd) VALUES (%s, %s, LOCALTIMESTAMP(0), NULL)", (uID, deviceID))
    except Exception as e:
        print(e)
    finally:
        dat.close()
        conn.close()

def addCustomer(data):
    try:
        conn=psycopg2.connect("dbname='Sportschool' user='postgres' host='192.168.1.2' password='omgidpomg'")
        dat = conn.cursor()
        command = "INSERT INTO klant (nfcid, voornaamklant, achternaamklant, emailadresklant, iban, geboortedatum, straatnaam, huisnummer, plaats, postcode) VALUES ('"
        command += "', '".join(data[:-2]) + "');"
        print(command)
        dat.execute(command)
        data.append(data[0])
        command = "INSERT INTO account (gebruikersnaam, wachtwoord, nfcid) VALUES ('%s', '%s', '%s');" % data[-3:]
        print(command)
        dat.execute(command)
        command = "INSERT INTO klantlidmaatschap (nfcid, lidmaatschapid, datuminschrijving) VALUES ('%s', 1, CURRENT_DATE);" % data[0]
        print(command)
        dat.execute(command)
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        dat.close()
        conn.close()
