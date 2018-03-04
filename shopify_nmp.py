#!/usr/bin/python3
import os
import sys
import csv
import time
import json
from datetime import datetime
from pprint import pprint
'''
#!/usr/bin/python3 (running in python 3) Will remove 'u' which is a unicode character

name = order nummber
<shop name>  = name of shopify store
https://<shop name>.myshopify.com/admin/orders.json?name=7703E&fields=name,billing_address,shipping_address,discount_codes,shipping_lines,gateway,total_price,subtotal_price,created_at
'''


#the timestamp, in time_t format
now=str(int(time.time()))
str_now=str(datetime.now())


#if len(sys.argv)==2:
inputfile = sys.argv[1]

#if len(sys.argv)==3:
outputFile = sys.argv[2]

'''
if not os.path.isfile(file) or not os.access(file,os.R_OK):
    print"Can't read input file: " + file + " - exiting"
    sys.exit(1)
'''
with open(inputfile,'r') as json_file:
    data = json.load(json_file)
    #data = ast.literal_eval(json.dumps(data)) #removes unicode character from output


#Flatten Json as  would be accessible if indexing a dictionary
def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + '['+"'"+a +"'"+ ']'+' ')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + '['+"'"+ str(i)+"'"+']' +' ')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out
try:
    total_price=data['orders'][0]['total_price']
except:
    total_price ='False'
try:
    subtotal_price =data['orders'][0]['subtotal_price']
except:
    subtotal_price='False'

try:
    shipping_price =data['orders'][0]['shipping_lines'][0]['price']
except:
    shipping_price ='False'


try:
    shipping_zip =data['orders'][0]['shipping_address']['zip']

except:
    shipping_zip='False'
try:
    shipping_name =data['orders'][0]['shipping_address']['name']
except:
    shipping_name ='False'


try:
    shipping_last_name =data['orders'][0]['shipping_address']['last_name']

except:
    shipping_last_name='False'

try:
    shipping_first_name = data['orders'][0]['shipping_address']['first_name']
except:
    shipping_first_name ='False'

try:
    shipping_country =data['orders'][0]['shipping_address']['country']
except:
    shipping_country ='False'

try:
    shipping_city =data['orders'][0]['shipping_address']['city']
except:
    shipping_city ='False'

try:
    shipping_address_line_2 =data['orders'][0]['shipping_address']['address2']
except:
    shipping_address_line_2 ='False'

try:
    shipping_address_line_1 =data['orders'][0]['shipping_address']['address1']
except:
    shipping_address_line_1 ='False'

try:
    gateway =data['orders'][0]['gateway']
except:
    gateway ='False'

try:
    name =data['orders'][0]['name']
except:
    name ='False'


try:
    billing_zip =data['orders'][0]['billing_address']['zip']

except:
    billing_zip='False'
try:
    billing_name =data['orders'][0]['billing_address']['name']
except:
    billing_name ='False'


try:
    billing_last_name =data['orders'][0]['billing_address']['last_name']

except:
    billing_last_name='False'

try:
    billing_first_name = data['orders'][0]['billing_address']['first_name']
except:
    billing_first_name ='False'

try:
    billing_country =data['orders'][0]['billing_address']['country']
except:
    billing_country ='False'

try:
    billing_city =data['orders'][0]['billing_address']['city']
except:
    billing_city ='False'

try:
    billing_address_line_2 =data['orders'][0]['billing_address']['address2']
except:
    billing_address_line_2 ='False'

try:
    billing_address_line_1 =data['orders'][0]['billing_address']['address1']
except:
    billing_address_line_1 ='False'

try:
    order_creation=data['orders'][0]['created_at']
except:
    order = 'False'

try:
    discount_codes=data['orders'][0]['discount_codes']
except:
    discount_codes = 'False'




with open(outputFile, "w") as myfile1:
    writer1=csv.writer(myfile1)
    writer1.writerow(['total_price','subtotal_price','shipping_price','gateway','order number','order_creation','discount_codes',
    'shipping_address_line_1','shipping_address_line_2','shipping_first_name','shipping_last_name',
    'shipping_city','shipping_country','shipping_zip',
    'billing_first_name','billing_last_name',
    'billing_address_line_1','billing_address_line_2','billing_city','billing_country','billing_zip'])
    writer1.writerow([total_price,subtotal_price,shipping_price,gateway,name,order_creation,discount_codes,
    shipping_address_line_1,shipping_address_line_2,shipping_first_name,shipping_last_name,
    shipping_city,shipping_country,shipping_zip,
    billing_first_name,billing_last_name,
    billing_address_line_1,billing_address_line_2,billing_city,billing_country,billing_zip])


myfile1.close()
#Print a flatten version of the json file
#pprint(flatten_json(data))


'''
#summary report
summary_f="summary_json_"+now+".txt"
summary_fp=open(summary_f,"w")
print >>summary_fp, "Ran " + sys.argv[0] + " at " + str_now + " (" + now + ")" +  " with file " + sys.argv[1]
print >>summary_fp, "Files created:"
print >>summary_fp, "\tjson_test_"+now+".csv"
'''
