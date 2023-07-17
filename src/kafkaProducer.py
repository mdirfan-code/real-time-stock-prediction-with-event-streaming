import sys
sys.path.append('utilFunctions')
import stockMarketDataSimulator
from kafka import KafkaProducer
from json import dumps
import os
from dotenv import load_dotenv
from time import sleep

load_dotenv('.env')

dataSimul = stockMarketDataSimulator.stockDataSimulator().get_data('NYA')
producer = KafkaProducer(bootstrap_servers=[os.getenv('VM_IP')],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))


while True:
    try:
        producer.send('Topic_goes_here',next(dataSimul))
        # print(next(dataSimul))
        sleep(2)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        break



