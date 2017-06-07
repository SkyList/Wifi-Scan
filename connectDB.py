import MySQLdb

con = MySQLdb.connect(host="localhost", user='root', passwd="", db="wifiscan")
#con.select_db ('redes')

cursor = con.cursor()

cursor.execute("SELECT * FROM scan")

numrows = int(cursor.rowcount)

print ("--------------------------------------------------")
print ("| ID  Campo                                      |")
print ("--------------------------------------------------")

for row in cursor.fetchall():
   print (" ",row[0]," ",row[1])

con.commit()