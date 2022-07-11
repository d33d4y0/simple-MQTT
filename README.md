# simple-MQTT
> This repository uses to store a network project for the CPE314 course at KMUTT
## Broker
- A Broker act as a server for receiving and passing data from publisher and subscriber
## Subscriber
- A Subscriber responsible for subscribing any topic and waiting for publisher sent data that have the same topic
## Publisher
- A Publisher responsible for publish any topic and data to a broker server
## How to use
Running a Broker
```
./broker.py 
```
Subscribe a topic
```
./subscriber.py -b [ip of broker] -t [topic]
```
Publish data
```
./publisher.py -b [ip of broker] -d [data] -t [topic]
```
## Example
At first terminal
```
./broker.py
```
At second terminal
```
./subscriber.py -b 127.0.0.1 -t test
```
At third terminal
```
./publisher.py -b 127.0.0.1 -t test -d message
```
