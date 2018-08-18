import csv
import sys
import os

#for entry in os.scandir('.'):
 #   if entry.is_file():
  #      print(entry.name)
one = 'export.csv'
count = 0

#CustomerCode
#CustomerRef
#DeliveryRoute
#Company
#Address1
#Address2
#Address3
#Address4
#Town
#County
#Postcode
#Country
#Contact
#Phone
#ShipDate
#TotalItems
#TotalWeight
#GoodsDescription
#PackageTypeId

results = []

with open(one) as clicked:
    
    readClicked = csv.reader(clicked, delimiter=',')
   
    next(readClicked) #Skip header line
    for i in readClicked:
        results.append(i)
        print(i)
clicked.close()
    
    
        
for i in results:
    print(i[1])
     
     
 #Still have to figure out what to do for county i[10]
 #i[10] (town) as a placeholder for the time being
 #Also need to figure out what the customer code corresponds too
with open('ups.csv', "w",newline='') as myfile:
    writer=csv.writer(myfile)
    writer.writerow(['CUSTOMER CODE',	'CUSTOMER REF',	'DELIVERY CODE','DELIVERY NAME',	'ADDRESS1',	'ADDRESS2','ADDRESS3','POSTCODE',	'TOWN',	'COUNTY'	,'COUNTRY',	'CONTACT',	'PHONE',	'SHIP DATE'	,'TOTAL ITEMS',	'TOTAL WEIGHT',	'GOODS DECRIPTION',	'PACKAGE TYPE'])
    for i in results:
        writer.writerow(['N306',i[1],i[2],i[12],i[4],i[5],i[6],i[10],i[8],i[10],i[11],i[12],i[13],i[14],i[15],i[16],i[17],'0'])
myfile.close()


#Remve empty rows from csv
#Good to know but not needed here
input = open('ups.csv', 'r')
output = open('ups_new.csv', 'w',newline='')
writer = csv.writer(output)
for row in csv.reader(input):
    #if row:
    if any(field.strip() for field in row):
        writer.writerow(row)
input.close()
output.close()