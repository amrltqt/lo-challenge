from django.test import TestCase
from server.schema import schema

class QueryTestCase(TestCase):

    def test_simple_query(self):
        query = """
            query {
                currentTemperature {
                    value
                    timestamp
                    unit
                }
            }
        """
        result = schema.execute(query)
        assert result.data["currentTemperature"]["unit"] == "C"
        assert result.data["currentTemperature"]["value"] == 28.8


    def test_subscribe_query(self):
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
        result = schema.execute(subscription)
        print(result.data)