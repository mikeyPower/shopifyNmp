import csv
import sys
import os

#for entry in os.scandir('.'):
 #   if entry.is_file():
  #      print(entry.name)
one = 'members_Data_Protection_2018_click_activity_Jul_6_2018.csv'
two = 'members_Data_Protection_2018_sent_Jul_6_2018.csv'
count = 0
listClicked =[]
listSent = []

with open(one) as clicked:
    #clicked.next()
    #wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    readClicked = csv.reader(clicked, delimiter=',')
    
    with open(two) as sent:
        #sent.next()
        #wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        readSent = csv.reader(sent, delimiter=',')
        
        for i in readClicked:
            listClicked.append(i[0]+" "+i[1]+" "+i[2])
            
            
        for j in readSent:
            listSent.append(j[0]+" "+j[1]+" "+j[2])
      
    
    sent.close()
clicked.close()
listDif =[]
listDif = set(listSent) - set(listClicked)



print(set([x for x in listClicked if listClicked.count(x) > 1]))



print(len(listDif))

print(len(set(listClicked)))
print(len(set(listSent)))



with open('testfile.csv','w') as myfile:
    writer=csv.writer(myfile)
    for i in listDif:
        writer.writerow(i.split())
    
myfile.close()