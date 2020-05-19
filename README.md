# Temperature Server

This is a simple temperature server made of django features in combination with graphene. This has been done for a challenge that have been proposed during an interview process. 

Before this challenge, I was not aware about graphql or graphene in general. It tooks some hours to adapt and understand the way it's mean to work. I was initially confident about my skills around websocket, it was worth to take the time to refresh how it works with Django and Channels (the consumer API is really nice to use).

The most challenging thing is to adapt the technology for the subscription part of the protocol as it's not necessarily well handled by the packages available actually on pypi. Most of the implementation are really recent and I spend some time in the dependency hell around subscription. The subscription part of this app is something that deserve a stronger investment in the choice of the libs to use (or to develop, seriously, I really want to try to develop my own little package following https://github.com/apollographql/subscriptions-transport-ws/blob/master/PROTOCOL.md).

Graphene to build the query engine is not so complex, it takes some time to understand the resolve chain but when it's ok everything become quite simple. 


## Getting started


Clone the repo on your local environment then, use docker-compose to launch the app and make it available on your http://localhost:8000

```powershell
docker-compose build
docker-compose up -d
```

You can access to http://localhost:8000/graphql try a first sample with the nice graphiql client! Use the following query!

```graphql
query
{
    currentTemperature
    {
        timestamp
        value
        unit
    }
}
```

If you don't want to use docker, mhh'ok. 

```powershell
virtualenv env 
env\Scripts\activate
pip install -r requirements.txt
python .\manage.py runserver
```

To launch the test, think about building the server package in edit mode. 

```powershell
$ pip install -e .
$ pytest
```

If you want to test the subscription, build an apollo client in JS for example and try it out by reaching ws://localhost:8000/ws/graphql
The awaited kind of query is: 

```graphql
subscription
{
    currentTemperatureSubscribe
    {
        temperature
        {
            timestamp
            value
            unit
        }
    }
}
```

## How it works

The Django app serves two endpoints - one for http the other for websocket: 

* http://localhost/graphql
* ws://localhost/ws/graphql


To stick to Django's recommandations I use a `routing.py` & a `url.py` files instead of just one routing with everything inside (leaving the responsibility to the configuration in fact) and from this route the app adress simply the schema write down into `schema.py`. This schema contains the resolvers that will be used to produce the temperature data. As it's a random value, a seed is positionned in the script (to keep same data for demo purpose) and the creation of the sample is leave to the `Temperature` class.

The `setup.py` is only means to be used to build a work-in-progress package used by pytest. 

## Dependencies 

Django
Graphene
Graphene Django
Graphene Subscription

Subscription is not mature in the current stable graphene version so while the latest is not release, the best choice seems to be  https://github.com/jaydenwindle/graphene-subscriptions

