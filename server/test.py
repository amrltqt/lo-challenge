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
