from channels.routing import ProtocolTypeRouter
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path


from graphene_subscriptions.consumers import GraphqlSubscriptionConsumer

application = ProtocolTypeRouter({
    'websocket': URLRouter([
        re_path(r'ws/graphql/$', GraphqlSubscriptionConsumer)
    ]),
})