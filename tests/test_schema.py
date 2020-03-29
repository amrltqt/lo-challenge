from server.schema import schema


def test_simple_query():
    """ Test if the nominal case with query is working well """
    import random
    random.seed(42)
    
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
    assert result.data["currentTemperature"]["value"] == 26.3


def test_value_only():
    """ Test if the selection the request of only one value provide effectively one value - meaning that graphene resolver are well configured"""
    import random
    random.seed(42)

    query = """
        query {
            currentTemperature {
                value
            }
        }
    """
    result = schema.execute(query)
    assert result.data["currentTemperature"]["value"] == 26.3
    assert list(result.data["currentTemperature"].keys()) == ["value"]


def test_bad_query():
    """ Errors should be provided when there is an issue in the query"""
    query = """
        query {
            temperature {
                value
                timestamp
                unit
            }
        }
    """
    result = schema.execute(query)
    assert len(result.errors) != 0
