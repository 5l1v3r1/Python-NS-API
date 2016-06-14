from ns import NS
from urllib import quote


class Departures(NS):
    """
    Wrapper for the departures API of the Nederlandse Spoorwegen (NS)
    Docs: http://www.ns.nl/en/travel-information/ns-api/documentation-up-to-date-departure-times.html

    Copyright (c) 2014 - 2016 | Paradoxis
    """

    def get_from(self, city):
        """
        Get all departures from a city
        :param city: string
        :return: objectify.ObjectifiedElement
        """
        return self.get("http://webservices.ns.nl/ns-api-avt?station=" + quote(city))

    def get_from_to(self, city, destination):
        """
        Get all departures from a city to a specific destination
        :param city: string
        :param destination: string
        :return: objectify.ObjectifiedElement
        """
        filtered = []
        departures = self.get_from(city)

        for d in departures.iterchildren():

            if hasattr(d, "EindBestemming"):
                if destination in str(d.EindBestemming):
                    filtered.append(d)
                    continue

            if hasattr(d, "RouteTekst"):
                if destination in str(d.RouteTekst):
                    filtered.append(d)
                    continue

        return filtered

    def get_first_from_to(self, city, destination):
        """
        Get the first departure from a city to a specific destination
        :param city: string
        :param destination:  string
        :return: objectify.ObjectifiedElement
        """
        return self.get_from_to(city, destination)[-1:]
