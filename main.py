from Rabbit import send
from DB import inserter
from Graph import graph_data
from threading import Thread

# path = r'C:\Users\royhe\OneDrive\Desktop\home_exercise\invoices_2013.csv' #insert path
# file_type = 'csv' # insert file type
# table = 'invoices' # insert destination table in database

def main():
    while True:
        path = input("Please enter file path:  ")
        file_type = input("Please enter file type (csv/json):  ")
        table = input("Please enter destination table:  ")
        rpc = send.RpcClient()
        response = rpc.call(f'{path},{file_type},{table}')
        inserter.table_inserter(response)



if __name__ == '__main__':
    Thread(target=main).start()
    Thread(target=graph_data.graph).start()



















