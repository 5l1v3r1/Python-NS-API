from requests import get
from lxml import objectify


class NS:
    """
    Base class for the API of the Nederlandse Spoorwegen (NS)
    Docs: http://www.ns.nl/en/travel-information/ns-api

    Copyright (c) 2014 - 2016 | Paradoxis
    """
    API_USERNAME = None
    API_PASSWORD = None

    def __init__(self):
        """
        Constructor
        :return: void
        """
        if NS.API_USERNAME is not None and NS.API_PASSWORD is not None:
            self.auth = (NS.API_USERNAME, NS.API_PASSWORD)
        else:
            raise NSException("API was not initialized, please use `NS.initialize(username, password)` first")

    def get(self, url):
        """
        Make an API call to an NS API endpoint
        :param url: string
        :return: objectify.ObjectifiedElement
        """
        response = objectify.fromstring(get(url, auth=self.auth).content)

        if hasattr(response, "message") is False:
            return response
        else:
            raise NSException(str(response["message"]))

    @staticmethod
    def initialize(username, password):
        """
        Initialize the NS API
        Simply a shorthand for `NS.API_* = value` for those who like one-liners
        :param username: string
        :param password: string
        :return: void
        """
        NS.API_USERNAME = username
        NS.API_PASSWORD = password


class NSException(Exception):
    """
    Custom exception thrown by the NS API
    Docs: http://www.ns.nl/en/travel-information/ns-api

    Copyright (c) 2014 - 2016 | Paradoxis
    """
    pass
