from ns import NS
from urllib import quote


class Delays(NS):
    """
    Wrapper for the delays API of the Nederlandse Spoorwegen (NS)
    Docs: http://www.ns.nl/en/travel-information/ns-api/documentation-disruptions-and-maintenance-work.html

    Copyright (c) 2014 - 2016 | Paradoxis
    """

    def get_at(self, city, actual = True, unplanned = True):
        """
        Get all delays at a given city
        :param city: string
        :return: objectify.ObjectifiedElement
        """
        url = "http://webservices.ns.nl/ns-api-storingen?station={city}&actual={actual}&unplanned={unplanned}"
        url = url.format(
            city = quote(city),
            actual = ("true" if actual else "false"),
            unplanned = ("true" if unplanned else "false"))

        return self.get(url)

    def get_unplanned_at(self, city, actual = True):
        """
        Get all unplanned delays at a given city
        :param city: string
        :param actual: boolean
        :return: void
        """
        return self.get_at(city, actual, unplanned = True)["Ongepland"]

    def get_planned_at(self, city, actual = True):
        """
        Get all planned delays at a given city
        :param city: string
        :param actual: boolean
        :return: void
        """
        return self.get_at(city, actual, unplanned = False)["Gepland"]