import boto3

qname = input("what is the queue name: ")
message = input("message: ")

# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName=qname)

# Create a new message
response = queue.send_message(MessageBody=message)

# The response is NOT a resource, but gives you a message ID and MD5
print(response.get('MessageId'))
print(response.get('MD5OfMessageBody'))