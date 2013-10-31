#
# Fetches the Daily Poulation values for a date
# and summarizes population changes for it.
#

import requests
from json import loads


class SummarizeDailyPopulationChanges:
    def _booked_males_as(self, response):
        return len(loads(response.text)['objects'])

    def date(self, date):
        race = 'AS'
        date = '2013-06-01'
        cook_county_url = 'http://cookcountyjail.recoveredfactory.net'
        county_inmate_api = '%s/api/1.0/countyinmate' % cook_county_url
        get_cmd = '%s?format=json&limit=0&race=%s&booking_date__exact=%s' % \
            (county_inmate_api, race, date)
        response = requests.get(get_cmd)
        daily_population_changes_url = \
            '%s/api/2.0/daily_population_changes' % cook_county_url
        requests.post(daily_population_changes_url,
                      data={'date': date,
                            'booked_males_as': self._booked_males_as(response)})
