import graphene
import datetime
import random

from rx import Observable


random.seed(42)


class Temperature(graphene.ObjectType):
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
    current_temperature = graphene.Field(Temperature)

    def resolve_current_temperature(root, info):
        return Temperature()


class TemperatureSubscription(graphene.ObjectType):
    temperature = graphene.Field(Temperature)

    def resolve_temperature(root, info):
        return Temperature()


class Subscription(graphene.ObjectType):
    current_temperature_subscribe = graphene.Field(TemperatureSubscription)

    def resolve_current_temperature_subscribe(root, info):
        return Observable.interval(3000).map(lambda _: TemperatureSubscription())


schema = graphene.Schema(query=Query, subscription=Subscription)
