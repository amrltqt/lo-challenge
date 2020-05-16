import pytest
import json
import asyncio
import random

from channels.testing import WebsocketCommunicator
from graphene_subscriptions.consumers import GraphqlSubscriptionConsumer


async def websocket():
    """
    This test extract two temperature samples from the temperature subscription.
    """ 
    random.seed(42)

    communicator = WebsocketCommunicator(GraphqlSubscriptionConsumer, "ws/graphql/")
    connected, subprotocol = await communicator.connect()

    assert connected
    
    subscription = """
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
    """

    await communicator.send_to(text_data=json.dumps(
        {
            "type": "start",
            "payload": {
                "query": subscription
            }
        }))

    # Message is sent every 3 seconds, set the timeout to 4. 
    resp = await communicator.receive_from(timeout=4)
    data = json.loads(resp)
    assert data["payload"]["errors"] is None
    assert data["payload"]["data"]["currentTemperatureSubscribe"]["temperature"]["value"] == 23.9
    
    resp = await communicator.receive_from(timeout=4)
    data = json.loads(resp)
    assert data["payload"]["errors"] is None
    assert data["payload"]["data"]["currentTemperatureSubscribe"]["temperature"]["value"] == 12.2


def test_subscription():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(websocket())