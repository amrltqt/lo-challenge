# Temperature Server

This is a simple temperature server made of django features in combination with graphene. This has been done for a challenge that have been proposed during an interview process. 

Before this challenge, I was not aware about graphql or graphene in general. It tooks some hours to adapt and understand the way it's mean to work. I was initially confident about my skills around websocket, it was worth to take a huge 

The most challenging thing is to adapt the technology for the subscription part of the protocol as it's not necessarily well handled by the packages available actually on pypi. Most of the implementation are really recent and I spend some time in the dependency hell around subscription. The subscription part of this app is something that deserve a stronger investment in the choice of the libs to use (or to develop, seriously, I really want to try to develop my own little package following https://github.com/apollographql/subscriptions-transport-ws/blob/master/PROTOCOL.md).

Graphene to build the query engine is not so complex, it takes some time to understand the resolve chain but when it's ok everything become quite simple. 

## Technologies

- Websocket 
- GraphQL protocol
- Django
- Python 

## Getting started

Use docker-compose to launch the app on the port 8000, launching http://localhost:8000/graphql will gives you access to this really nice graphiql viewer configured. 

```powershell
docker-compose build
docker-compose up -d
```

To develop locally on this app, just clone the repo and you can start with:

```powershell
$ env\Scripts\activate
$ pip install -r requirements.txt
$ python .\manage.py runserver
```

To launch the test, think about building the server package in edit mode. 
```powershell
$ pip install -e .
$ pytest
```

## Dependencies 

Django
Graphene
Graphene Django
Graphene Subscription

Subscription is kind of hard to handle out of the box with django
The best library to  https://github.com/jaydenwindle/graphene-subscriptions to be challenged with this one https://github.com/graphql-python/graphql-ws 

## Docker 

To deploy the app, to be frank it will be locally for test purpose, so I will not mimic all the hardening phase dedicated to the production. 
I chose to build a simple Dockerfile and a docker-compose.yml to help reviewers to launch easily the app. 


## To be continued

- Testing on subscription, actually I'm missing some understanding on the way Observable are served and it make me a bit confused on the best way to test it. 