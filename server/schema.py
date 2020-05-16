import graphene
import datetime
import random

from rx import Observable


class Temperature(graphene.ObjectType):
    """ 
    Temperature value is resolved randomly
    value - float : a random value between 10 & 30 with one decimal (ex: 23.3)
    timestamp - float : unix timestamp of the generation
    unit - constant value representing the unit

    Those values are generated independently and there is no relationship except
    the interesting representation of getting them all together
    """
    value = graphene.Float()
    timestamp = graphene.Float()
    unit = graphene.String()

    def resolve_value(root, info):
        return random.randrange(100, 300) / 10

    def resolve_timestamp(root, info):
        return datetime.datetime.now().timestamp()

    def resolve_unit(root, info):
        return "C"


class Query(graphene.ObjectType):
    """ Wrap the resolution of the temperature to expose the query following the schema: 
    An instance of this class is one of the entrypoint exposed by the schema graphene API
    
    ````graphql
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
    """
    current_temperature = graphene.Field(Temperature)

    def resolve_current_temperature(root, info):
        return Temperature()


class TemperatureSubscription(graphene.ObjectType):
    temperature = graphene.Field(Temperature)

    def resolve_temperature(root, info):
        return Temperature()


class Subscription(graphene.ObjectType):
    """ 
    Subscription made available a temperature resolution at the the currentTemperatureSubscribe key.
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
    
    """
    current_temperature_subscribe = graphene.Field(TemperatureSubscription)

    def resolve_current_temperature_subscribe(root, info):
        return Observable.interval(3000).map(lambda _: TemperatureSubscription())


schema = graphene.Schema(query=Query, subscription=Subscription)
