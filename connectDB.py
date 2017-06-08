import MySQLdb

con = MySQLdb.connect(host="192.168.0.62", user='root', passwd="1", db="wifiscan")
cursor = con.cursor()

#cursor.execute("INSERT INTO `wifiscan`.`scan` (`SSID`, `MAC`, `QUALITY`, `SIGNAL`, `CHANNEL`, `FREQUENCY`, `BEACON`) VALUES ('teste', '10:10:10:10:10:10', '10', '10', '10', '10', '10');")
cursor.execute("SELECT * FROM scan")




print "--------------------------------------------------"
print "| ID  Campo                                      |"
print "--------------------------------------------------"

for row in cursor.fetchall():
   print " ",row[0]," ",row[1]

con.commit()