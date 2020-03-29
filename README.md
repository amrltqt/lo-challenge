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

The Django app serves two endpoints: 

* http://localhost:8000/graphql
* ws://localhost:8000/ws/graphql

This endpoints are served through the asgi protocol and django suggests to leverage daphne to connect to the http server you want. I didn't take the time to test it actually (https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/daphne/).

To stick to Django's recommandations I use a `routing.py` & a `url.py` files instead of just one routing with everything inside (leaving the responsibility to the configuration in fact) and from this route the app adress simply the schema write down into `schema.py`. This schema contains the resolvers that will be used to produce the temperature data. As it's a random value, a seed is positionned in the script (to keep same data for demo purpose) and the creation of the sample is leave to the `Temperature` class.

The `setup.py` is only means to be used to build a work-in-progress package used by pytest. 

I've separated the tests package from the server itself to avoid pushing tests in production in the future. 

It's quite simple in fact, even if it took me several hours to make it works!

## Dependencies 

Django
Graphene
Graphene Django
Graphene Subscription

Subscription is kind of hard to handle out of the box with django
The best library to  https://github.com/jaydenwindle/graphene-subscriptions to be challenged with this one https://github.com/graphql-python/graphql-ws 


## Design

- The responsibility of generating new data is leave to the resolvers. It's sufficient and there is no need to leverage Django models for that. 
- The resolution is done at the Temperature field level, it could have been done upper for performance reasons. There is no question of performance so I chose to make it in the most elegant way possible (for me)
- I didn't need a django app, I prefer stick to a simple project structure to avoid jumping on the code without added value. 
- There is two ways to adresse the schema, one using pure http request and the second one which should leverage a websocket. In case of using a gateway to adresse the API from the outside, both of the protocol need to be opened.


## Improvments

- On the deployment part, I don't know what are the security recommandation to adress a websocket. I need to learn about that and publish a correct Nginx example. 
- Testing on subscription, actually I'm missing some understanding on the way Observable are served and it make me a bit confused on the best way to test it. 