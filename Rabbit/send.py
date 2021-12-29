import pika
import uuid

class RpcClient(object):

    def __init__(self):
        #creating connection to RabbitMQ
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))

        #opening Channel
        self.channel = self.connection.channel()

        #declaring Queue
        result = self.channel.queue_declare(queue='', exclusive=True)

        # making callback reply with a response
        self.callback_queue = result.method.queue
        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

    #asigning body to response
    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    #returning response
    def call(self, file_data):
        file_data = file_data.encode('utf-8')
        self.response = None

        #creating unique ID per client request
        self.corr_id = str(uuid.uuid4())

        #setting up queue for return message
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=file_data)

        while self.response is None:
            self.connection.process_data_events()

        #creating list out of data for easier processing
        self.response = self.response.decode("utf-8").split(",")
        return self.response



# path = r'C:\Users\royhe\OneDrive\Desktop\home_exercise\invoices_2013.csv' #insert path
# file_type = 'csv' # insert file type
# table = 'invoices' # insert destination table in database
# rpc = RpcClient()
# response = rpc.call(f'{path},{file_type},{table}')
# print(response)

