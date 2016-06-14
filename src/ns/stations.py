from ns import NS
from ns import NSException


class Stations(NS):
    """
    Wrapper for the stations API of the Nederlandse Spoorwegen (NS)
    Docs: http://www.ns.nl/en/travel-information/ns-api/documentation-station-list.html

    Copyright (c) 2014 - 2016 | Paradoxis
    """
    API_V1 = 1
    API_V2 = 2

    def get_all(self, api_version = API_V2):
        """
        Fetch price information about a trip from a city to a given destination
        :param api_version: int
        :return: objectify.ObjectifiedElement
        """
        if api_version == Stations.API_V1:
            return self.get("http://webservices.ns.nl/ns-api-stations")

        if api_version == Stations.API_V2:
            return self.get("http://webservices.ns.nl/ns-api-stations-v2")

        raise NSException("Invalid API version '%s', accepted values are `int(1)` or `int(2)`" % (api_version))

