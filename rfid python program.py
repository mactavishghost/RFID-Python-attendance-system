import serial
import MySQLdb
import time

dbConn = MySQLdb.connect("127.0.0.1","root","","rfid") or die ("could not connect to database")
cursor = dbConn.cursor()

device = 'COM3'
try:
    print("Trying..."),device
    arduino = serial.Serial(device,9600)
except:
    print ("failed to connect on"),device
while True:
    time.sleep(1)
    try:
        data=arduino.readline()


        print ("inside--->")
        print ("inside2--->")
        print (data)
        data1=print(data)
        print("befoe try")
        try:
            print ("before first insert..")
            cursor=dbConn.cursor()
            sql = "INSERT INTO rfid_read ( member_id,rfid_data) VALUES ( %s,%s)"
            val = (1, data)
            cursor.execute(sql, val)
            #cursor.execute("""INSERT INTO rfid_read(id,member_id,allowed_members) VALUES (11,1,data1)""")
            dbConn.commit();
            print ("after first insert")
          #  cursor.execute("""INSERT INTO rfid_read(id,member_id,allowed_members,time) VALUES (NULL,%s,%s)""", (pieces[0],pieces[1]))
           # dbConn.commit()
           # cursor.close()
        except MySQLdb.IntegrityError:
            print ("failed to insert data")
        finally:
            cursor.close()
    except:
        print ("processing")
