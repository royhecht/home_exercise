from DB.Handler import dbHandler
import csv,json

def table_inserter(values):
    #db connection
    mydb = dbHandler(r'DB\mydb.db')
    cur = mydb.connect().cursor()

    #getting columns from chosen table
    a = cur.execute(f'''select * from invoices''')
    columns = [columns[0] for columns in a.description]

    #opening clients file
    with open(f'{values[0]}', 'r') as f:
        #checking if csv or json
        if values[1] == 'csv':
            dr = csv.DictReader(f)
        elif values[1] == 'json':
            dr = json.load(f)

        #getting all values from file into a list of tuples
        to_db = [(i[columns[0]],i[columns[1]],i[columns[2]],i[columns[3]],i[columns[4]],i[columns[5]],i[columns[6]],i[columns[7]],i[columns[8]]) for i in dr]

    #inserting into database
    mydb.select(f"INSERT INTO {values[2]} ({','.join(columns)}) VALUES (?,?,?,?,?,?,?,?,?);",to_db)

