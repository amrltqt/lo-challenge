import graphene
import datetime
import random

random.seed(42)


class Temperature(graphene.ObjectType):
    unit = graphene.String()
    value = graphene.Float()
    timestamp = graphene.DateTime()


class Query(graphene.ObjectType):
    current_temperature = graphene.Field(Temperature)

    @staticmethod
    def resolve_current_temperature(root, info):
        return {
            "value": random.randrange(100, 300) / 10,
            "timestamp": datetime.datetime.now(),
            "unit": "C"
        }


schema = graphene.Schema(query=Query)
