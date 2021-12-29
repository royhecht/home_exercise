import csv, sqlite3, json
from DB import Handler
con = sqlite3.connect("DB\mydb.db")
cur = con.cursor()
# columns='InvoiceId,CustomerId,InvoiceDate,BillingAddress,BillingCity,BillingState,BillingCountry,BillingPostalCode,Total'
# # cur.execute("CREATE TABLE invoices (InvoiceId,CustomerId,InvoiceDate,BillingAddress,BillingCity,BillingState,BillingCountry,BillingPostalCode,Total);") # use your column names here

# a = cur.execute(f'''select * from invoices''')
# columns = [columns[0] for columns in a.description]
# print(columns)

# mydb = Handler.dbHandler(r'DB\mydb.db')
# cur = mydb.connect().cursor()
# a = cur.execute(f'''select * from invoices''')
# columns = [columns[0] for columns in a.description]
# print(columns)

# cur.execute("delete from invoices")
# con.commit()
# con.close()

# cur.execute("select * from invoices")
# a = cur.fetchall()
# print(a)

#########dict
# dict_json = json.load(open(r'C:\Users\royhe\OneDrive\Desktop\home_exercise\invoices_2010.json'))
# print(dict_json)
# o = [(i['InvoiceId'],i['CustomerId'],i['InvoiceDate'],i['BillingAddress'],i['BillingCity'],i['BillingState'],i['BillingCountry'],i['BillingPostalCode'],i['Total']) for i in dict_json]
# print(o)
# cur.executemany(f"INSERT INTO invoices ({columns}) VALUES (?,?,?,?,?,?,?,?,?);",o)
# con.commit()
# con.close()

##########csv
# dict_json = csv.DictReader(open(r'C:\Users\royhe\OneDrive\Desktop\home_exercise\invoices_2012.csv'))
# o = [(i['InvoiceId'],i['CustomerId'],i['InvoiceDate'],i['BillingAddress'],i['BillingCity'],i['BillingState'],i['BillingCountry'],i['BillingPostalCode'],i['Total']) for i in dict_json]
# cur.executemany(f"INSERT INTO invoices ({columns}) VALUES (?,?,?,?,?,?,?,?,?);",o)
# con.commit()
# con.close()


######bytes

# n = r'C:\Users\royhe\OneDrive\Desktop\home_exercise\invoices_2013.csv, csv, invoices'
# n = bytes(n, 'utf-8')
# print(n)