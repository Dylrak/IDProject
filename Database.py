import psycopg2


def authenticate(uID):
    try:
        conn=psycopg2.connect("dbname='Sportschool' user='postgres' host='192.168.1.2' password='omgidpomg'")
    except Exception as e:
        print(e)
        return False
    cur = conn.cursor()
    try:
		command = "SELECT datuminschrijving FROM klantlidmaatschap WHERE nfcid = '%s' AND (datumuitschrijving IS NULL OR datumuitschrijving < current_date);" % uID
		cur.execute(command)  # Using this query,
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

def customerGym(uID, is_ingang):
	try:
		conn = psycopg2.connect("dbname='Sportschool' user='postgres' host='192.168.1.2' password='omgidpomg'")
		dat = conn.cursor()
		if is_ingang:
			command = "INSERT INTO klantsportschool (nfcid, sportschoolid) VALUES ('%s', 1);" %  uID
		else:
			command = "DELETE FROM klantsportschool WHERE nfcid='%s';" %  uID
		print(command)
		dat.execute(command)
	except Exception as e:
		print(e)
	finally:
		conn.commit()
		dat.close()
		conn.close()

def customerDevice(deviceID, uID):
    try:
        conn = psycopg2.connect("dbname='Sportschool' user='postgres' host='192.168.1.2' password='omgidpomg'")
        dat = conn.cursor()
        command = "SELECT begintijd FROM klantapparaat WHERE nfcid = '%s' AND eindtijd IS NULL;" %  uID
        dat.execute(command)
        ingecheckt = dat.fetchone()
        print(ingecheckt)
        if ingecheckt is not None:
            dat.execute("UPDATE klantapparaat SET eindtijd=LOCALTIMESTAMP(0) WHERE nfcid=%s AND begintijd=%s;", (uID, ingecheckt))
        else:
            command = "INSERT INTO klantapparaat (nfcid, apparaatid, begintijd) VALUES ('" 
            command += "', '".join((uID, str(deviceID))) + "', LOCALTIMESTAMP(0));"
            print(command)
            dat.execute(command)
    except Exception as e:
        print(e)
    finally:
		conn.commit()
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
        command = "INSERT INTO account (gebruikersnaam, wachtwoord, nfcid) VALUES ('"
        command += "', '".join(data[-3:]) + "');"
        print(command)
        dat.execute(command)
        command = "INSERT INTO klantlidmaatschap (nfcid, lidmaatschapid, datuminschrijving) VALUES ('%s', 1, CURRENT_DATE);" % data[0]
        print(command)
        dat.execute(command)
    except Exception as e:
        print(e)
    finally:
		conn.commit()
		dat.close()
		conn.close()
