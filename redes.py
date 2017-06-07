import MySQLdb
import os

con = MySQLdb.connect(host="localhost", user='root', passwd="12345678", db="redes")
con.select_db ('redes')

cursor = con.cursor()

#.execute("INSERT INTO `redes`.`dados_conexao` (`id`, `teste`) VALUES ('4', 'vaipf');")

cursor.execute("SELECT * FROM redes.dados_conexao")

numrows = int(cursor.rowcount)

print "--------------------------------------------------"
print "| ID  Campo                                      |"
print "--------------------------------------------------"

for row in cursor.fetchall():
   print " ",row[0]," ",row[1]

con.commit()

os.system("iwlist wlan0 scanning")
