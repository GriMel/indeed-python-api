# -*- coding: utf-8 -*-
import requests


class Indeed():
    """
    Indeed client
    """
    FORMAT = ("xml", "json")
    SORT = ("relevance", "date")
    RADIUS = 25
    SITE_TYPE = ("jobsite", "employer")
    JOB_TYPE = ("fulltime", "parttime", "contract", "internship", "temporary")
    START = 10
    LIMIT = 25
    FROMAGE = 0
    HIGHLIGHT = 0
    COUNTRIES = {"United states": "us",
                 "Argentina": "ar",
                 "Australia": "au",
                 "Austria": "at",
                 "Bahrain": "bh",
                 "Belgium": "be",
                 "Brazil": "br",
                 "Canada": "ca",
                 "Chile": "cl",
                 "China": "cn",
                 "Colombia": "co",
                 "Czhech Republic": "cz",
                 "Denmark": "dk",
                 "Finland": "fi",
                 "France": "fr",
                 "Germany": "de",
                 "Greece": "gr",
                 "Hong Kong": "hk",
                 "Hungary": "hu",
                 "India": "in",
                 "Indonesia": "id",
                 "Ireland": "ie",
                 "Israel": "il",
                 "Italy": "it",
                 "Japan": "jp",
                 "Korea": "kr",
                 "Kuwait": "kw",
                 "Luxemburg": "lu",
                 "Malaysia": "my",
                 "Mexico": "mx",
                 "Netherlands": "nl",
                 "New Zealand": "nz",
                 "Norway": "no",
                 "Oman": "om",
                 "Pakistan": "pk",
                 "Peru": "pe",
                 "Philippines": "ph",
                 "Poland": "pl",
                 "Portugal": "pt",
                 "Qatar": "qa",
                 "Romania": "ro",
                 "Russia": "ru",
                 "Saudi Arabia": "sa",
                 "Singapore": "sg",
                 "South Africa": "za",
                 "Spain": "es",
                 "Sweden": "se",
                 "Switzerland": "ch",
                 "Taiwan": "tw",
                 "Turkey": "tr",
                 "Ukraine": "ua",
                 "United Arab Emirates": "ae",
                 "United Kingdom": "gb",
                 "Venezuela": "ve"}

    def __init__(self, publisher, version=2):
        """
        Initialize Indeed with publisher ID
        """
        self.publisher = publisher
        self.version = version
        self.url = "http://api.indeed.com/ads/apisearch?publisher={publisher}"\
                   "&v={version}"\
                   "&format={format}"\
                   "&callback={callback}"\
                   "&q={query}"\
                   "&l={location}"\
                   "&sort={sort}"\
                   "&radius={radius}"\
                   "&st={st}"\
                   "&jt={jt}"\
                   "&start={start}"\
                   "&limit={limit}"\
                   "&fromage={fromage}"\
                   "&highlight={highlight}"\
                   "&filter={filter}"\
                   "&latlong={latlong}"\
                   "&co={country}"\
                   "&chnl={channel}"\
                   "&userip={userip}"\
                   "&useragent={useragent}"

    def search_jobs(self, format="xml", callback="", query, location,
                    state=None, ):
        """
        Main search function
        :format - "xml" and "json". Default - "xml"
        :callback - Callback. The name of a javascript function to use as a
                    callback to which the results of the search are passed.
                    This only applies when format=json.
                    For security reasons,
                    the callback name is restricted letters,
                    numbers, and the underscore character.
        :query - Query. By default terms are ANDed. To see what is possible,
                 use http://www.indeed.com/advanced_search
                 to perform a search and then
                 check the url for the q value
        :location - Location. Use a postal code or a "city,
                 state/province/region" combination.
        :state - State code of some countries.
                 Austria -  state (bundesland)
                 http://de.wikipedia.org/wiki/Bundesland_(%C3%96sterreich)

                 Australia -  state (territory)
                 http://en.wikipedia.org/wiki/ISO_3166-2:AU

                 Belgium -  province
                 http://en.wikipedia.org/wiki/ISO_3166-2:BE

                 Brazil - state (estado)
                 http://en.wikipedia.org/wiki/ISO_3166-2:BR

                 Canada - province (territory)
                 http://en.wikipedia.org/wiki/ISO_3166-2:CA

                 France - region
                 http://en.wikipedia.org/wiki/List_of_FIPS_region_codes_(D-F)#FR:_France

                 Germany - state (bundesland)
                 http://en.wikipedia.org/wiki/ISO_3166-2:DE

                 India - state
                 http://en.wikipedia.org/wiki/ISO_3166-2:IN

                 Ireland - county
                 http://en.wikipedia.org/wiki/ISO_3166-2:IE

                 Italy - region
                 http://it.wikipedia.org/wiki/Regioni_italiane#Sigle.5Bsenza.C2.A0fonte.5D

                 Mexico - state (estado)
                 http://en.wikipedia.org/wiki/ISO_3166-2:MX

                 Netherlands - province
                 http://en.wikipedia.org/wiki/ISO_3166-2:NL

                 Spain - provice
                 http://en.wikipedia.org/wiki/ISO_3166-2:ES

                 Switzerland - canton
                 http://en.wikipedia.org/wiki/ISO_3166-2:CH

                 United Kingdom - country
                 http://en.wikipedia.org/wiki/ISO_3166-2:GB

                 United States - state



        :sort - Sort by relevance or date. Default is relevance
        :radius - Distance from search location ("as the crow flies").
                  Default is 25.
        :st - Site type. To show only jobs from job board use "jobsite".
              For jobs from direct employer websites use "employer"
        :jt - Job type. Allowed values: "fulltime",
              "parttime", "contract", "internship", "temporary"
        :start - Start results as this results returned per query.
                 Default is 10.
        :limit - Maximum number of results returned per query.
                 Default is 25.
        :fromage - Number of days back to search.
        :highlight - Setting this value to 1 will bold terms in the snippet
                     that are also present in q. Default is 0.
        :filter - Filter duplicate results. 0 turns off duplicate job filtering
                  Default is 0.
        :latlong - If latlong=1, returns latitude and longtitude information
                   for each job result. Default is 0.
        :country - Search within country specified. Default is US.
                   Available coutries:
                   United States, Argentina, Australia, Austria, Bahrain,
                   Belgium, Brazil, Canada, Chile, China, Colombia,
                   Czech Republic, Denmark, Finland, France, Germany,
                   Greece, Hong Kong, Hungary, India, Indonesia, Ireland,
                   Israel, Italy, Japan, Korea, Kuwait, Luxembourg, Malaysia,
                   Mexico, Netherlands, New Zealand, Norway, Oman,
                   Pakistan, Peru, Philippines, Poland, Portugal,
                   Qatar, Romania, Russia, Saudi Arabia, Singapore,
                   South Africa, Spain, Sweden, Switzerland, Taiwan, Turkey,
                   United Arab Emirates, United Kingdom, Venezuela
        :chnl - Channel name: Group API requests to a specific channel
        :userip - The IP number of the end-user to whom the job results will be
                  displayed. This field is required
        :useragent - The User-Agent (browser) of the end-user to whom the job
                     results will be displayed. This can be obtained from the
                     "User-Agent" HTTP request header from the end-user.
                     This field is required.
        """



def main():
    """
    Main module
    """
    pass


if __name__ == '__main__':
    main()
