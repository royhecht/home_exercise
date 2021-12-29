import pika


#creating connection to RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

#opening Channel
channel = connection.channel()

#declaring queue
channel.queue_declare(queue='rpc_queue')

#callback
def on_request(ch, method, props, body):

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = props.correlation_id),
                     body=body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


#runs callback when request is received
channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

channel.start_consuming()





