# Python-NS-API
Wrapper for the NS API written in Python

## Installation
To install the library simply clone the repository and install the dependencies with `pip`.

    git clone git@github.com:Paradoxis/Python-NS-API.git
    pip install lxml

## Using the library
To use the library simply import the base class and initialize it using `NS.initialize()`.<br />
API keys must be requested form the official [NS website](http://www.ns.nl/en/travel-information/ns-api).

    # Import library
    from ns import NS
    from ns.stations import Stations
    
    # Initialize the library
    NS.initialize(username="user@domain.com", password="YOUR-SECRET-API-KEY")
    
    # Get a list of all stations
    sations = Stations().get_all()

## Documentation
Documentation of the API can be found here:

* [Prices](http://www.ns.nl/en/travel-information/ns-api/documentation-prices.html)
* [Departure times](http://www.ns.nl/en/travel-information/ns-api/documentation-up-to-date-departure-times.html)
* [Disruptions / Maintentance](http://www.ns.nl/en/travel-information/ns-api/documentation-disruptions-and-maintenance-work.html)
* [Station list](http://www.ns.nl/en/travel-information/ns-api/documentation-station-list.html)
* [Travel reccomendations](http://www.ns.nl/en/travel-information/ns-api/documentation-travel-recommendations.html)

## License
Copyright (c) 2016 - Luke Paris (Paradoxis)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
