from ns import NS
from urllib import urlencode


class Recommendations(NS):
    """
    Wrapper for the travel recommendations API of the Nederlandse Spoorwegen (NS)
    Docs: http://www.ns.nl/en/travel-information/ns-api/documentation-travel-recommendations.html

    Copyright (c) 2014 - 2016 | Paradoxis
    """

    def endpoint(self, parameters):
        """
        Format the API endpoint
        :param parameters: dictionary
        :return: string
        """
        return "http://webservices.ns.nl/ns-api-treinplanner?" + urlencode(parameters, doseq=True)

    def get_from_to(self, city, destination):
        """
        Get a travel recommendation from a city to a given destination
        :param city: string
        :param destination: string
        :return: objectify.ObjectifiedElement
        """
        return self.get(self.endpoint({
            "fromStation": city,
            "toStation": destination
        }))

    def get_from_to_via(self, city, destination, via):
        """
        Get a travel recommendation from a city to a given destination via a given station
        :param city: string
        :param destination: string
        :param via: string
        :return: objectify.ObjectifiedElement
        """
        return self.get(self.endpoint({
            "fromStation": city,
            "toStation": destination,
            "viaStation": via
        }))