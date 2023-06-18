
import csv
import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="root",
  database="Tuition"
)
mycursor = mydb.cursor()
with open('pincodes.csv', mode ='r')as file:
   
  # reading the CSV file
  csvFile = csv.reader(file)
  flag = False
  id = 1
  pincodes = []
  for lines in csvFile: 
    if flag:
        if pincodes.count(int(lines[0])) == 0:
            pincodes.append(int(lines[0]))
            sql = "INSERT INTO home_pincodes (id, Pincode,Devision,Region,Circle,Taluk,District,State) VALUES (%s, %s,%s,%s,%s,%s,%s,%s)"
            val = (id, lines[0],lines[1],lines[2],lines[3],lines[4],lines[5],lines[6])
            mycursor.execute(sql, val)
            id += 1 
        
    flag = True    

mydb.commit()


print("Data inserted")


