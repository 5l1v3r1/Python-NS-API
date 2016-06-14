from ns import NS
from urllib import urlencode


class Prices(NS):
    """
    Wrapper for the prices API of the Nederlandse Spoorwegen (NS)
    Docs: http://www.ns.nl/en/travel-information/ns-api/documentation-prices.html

    Copyright (c) 2014 - 2016 | Paradoxis
    """

    def endpoint(self, parameters):
        """
        Format the API endpoint
        :param parameters: dictionary
        :return: string
        """
        return "http://webservices.ns.nl/ns-api-prijzen-v3?" + urlencode(parameters, doseq=True)

    def get_from_to(self, city, destination):
        """
        Fetch price information about a trip from a city to a given destination
        :param city: string
        :param destination: string
        :return: objectify.ObjectifiedElement
        """
        return self.get(self.endpoint({
            "from": city,
            "to": destination
        }))

    def get_from_to_via(self, city, destination, via):
        """
        Fetch price information about a trip from a city to a given destination through a given city
        :param city: string
        :param destination: string
        :param via: string
        :return: objectify.ObjectifiedElement
        """
        return self.get(self.endpoint({
            "from": city,
            "to": destination,
            "via": via
        }))

    def get_from_to_on_date(self, city, destination, on_date):
        """
        Fetch price information about a trip from a city to a given destination on a given date
        :param city: string
        :param destination: string
        :param on_date: string (datetime)
        :return: objectify.ObjectifiedElement
        """
        return self.get(self.endpoint({
            "from": city,
            "to": destination,
            "dateTime": on_date
        }))

    def get_from_to_via_on_date(self, city, destination, via, on_date):
        """
        Fetch price information about a trip from a city to a given destination through a given city on a given date
        :param city: string
        :param destination: string
        :param via: string
        :param on_date: string (datetime)
        :return: objectify.ObjectifiedElement
        """
        return self.get(self.endpoint({
            "from": city,
            "to": destination,
            "via": via,
            "dateTime": on_date
        }))