import redis
import time

# Connect to the Redis server
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

# Define the stream name
stream_name = 'mystream'

# Publish messages to the stream
for i in range(5):
    message = f'Message {i + 1}'
    redis_client.xadd(stream_name, {'data': message})
    time.sleep(1)  # Add a delay to simulate real-time updates

# Read messages from the stream
consumer_group = 'mygroup'
consumer_name = 'myconsumer'
redis_client.xgroup_create(stream_name, consumer_group, id='0', mkstream=True)
while True:
    # Read messages from the stream
    messages = redis_client.xreadgroup(consumer_group, consumer_name, {stream_name: '>'}, count=10)
    
    if messages:
        for stream, message_data in messages:
            for message in message_data:
                message_id, data = message
                print(f"Received message {message_id} from stream {stream}: {data}")

                # Acknowledge the message
                redis_client.xack(stream_name, consumer_group, message_id)
    else:
        time.sleep(1)  # Add a delay if there are no messages

# Close the Redis connection
redis_client.close()
