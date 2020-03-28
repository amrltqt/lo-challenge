# Temperature Server

This is a simple temperature server made of django features in combination with graphene. This has been done for a challenge that have been proposed during an interview process. 

Before this challenge, I was not aware about graphql or graphene in general. It tooks some hours to adapt and understand the way it's mean to work. I was initially confident about my skills around websocket, it was worth to take a huge 

The most challenging thing is to adapt the technology for the subscription part of the protocol as it's not necessarily well handled by the package available actually (tested the latest graphene).

## Technologies

- Websocket 
- GraphQL protocol
- Django
- Python 

## Getting started

```powershell
$ env\Scripts\activate
$ pip install -r requirements.txt
$ python .\manage.py runserver
```

## Dependencies 

Django
Channels
Graphene
Graphene Django
Graphene Subscription

Subscription is kind of hard to handle out of the box with django
The best library to  https://github.com/jaydenwindle/graphene-subscriptions to be challenged with this one https://github.com/graphql-python/graphql-ws 