import matplotlib.pyplot as plt
from matplotlib import style
from DB.Handler import dbHandler
from matplotlib.animation import FuncAnimation
import pandas as pd


def graph():
    # style
    style.use('fivethirtyeight')

    def animate(self):
        #getting data for graph
        mydb = dbHandler(r'.\DB\mydb.db')
        conn = mydb.connect()
        df = pd.read_sql('SELECT * FROM invoices',conn)

        #cutting date to only year and month
        df['InvoiceDate'] = df['InvoiceDate'].str[:7]

        #getting amount of sales for each month of each year
        sold_each_month = df.value_counts('InvoiceDate').sort_index()

        #getting active Customers for each month of each year
        active_customers = df.groupby('InvoiceDate')['CustomerId'].value_counts().to_frame().value_counts('InvoiceDate').sort_index()


        x = list(sold_each_month.to_frame().to_dict()[0].keys())
        y1 = list(sold_each_month.to_frame().to_dict()[0].values())
        y2= list(active_customers.to_frame().to_dict()[0].values())

        plt.cla()

        plt.bar(x, y1)
        plt.plot(x, y2,color='red',marker='o')

        plt.xlabel("Date")
        plt.ylabel("No. Of Sales / Active Customers")
        plt.legend(["No. Of Sales", "No. Of Active Customers"], loc="upper right", bbox_to_anchor=(1, 1.1))
        plt.title("No. Of Sales / Active Customers For Each Month")


    ani = FuncAnimation(plt.gcf(), animate, interval=1000)

    plt.show()

