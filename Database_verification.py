import MFRC522
import signal


def getNFCUID():
    continue_reading = True

    # Capture SIGINT for cleanup when the script is aborted
    def end_read(uid):
        global continue_reading
        print("uID is: %s,%s,%s,%s" % (str(uid[0]), str(uid[1]), str(uid[2]), str(uid[3])))
        continue_reading = False

    # Hook the SIGINT
    signal.signal(signal.SIGINT, end_read)

    # Create an object of the class MFRC522
    MIFAREReader = MFRC522.MFRC522()
    while continue_reading:
        # Scan for cards
        (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

        # If a card is found
        if status == MIFAREReader.MI_OK:
            print
            "Card detected"

        # Get the UID of the card
        (status, uid) = MIFAREReader.MFRC522_Anticoll()

        # If we have the UID, return it and clean up.
        if status == MIFAREReader.MI_OK:
            end_read(uid)
            return uid