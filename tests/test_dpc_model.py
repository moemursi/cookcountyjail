from datetime import datetime
from random import randint
from flask.json import dumps
from ccj.models.daily_population_changes \
    import DailyPopulationChanges as DPC
import os


class Test_DailyPopulationChanges_Model:

    def setup_method(self, method):
        self.dpc = DPC('test.json')

    def teardown_method(self, method):
        self.dpc.clear()
        os.remove(self.dpc._path)

    def test_no_data_should_return_empty_array(self):
        assert self.dpc.query() == []

    def test_one_data_should_return_array_with_data(self):
        expected = [{
            'Date': '2013-10-18',
            'Booked': {
                'Males': {'AS': randint(0, 101)}
            }
        }]
        data = self._format(expected)
        self.dpc.store(data)
        assert self.dpc.query() == expected

    def test_one_data_should_match_json(self):
        expected = [{
            'Date': '2013-10-18',
            'Booked': {
                'Males': {'AS': randint(0, 101)}
            }
        }]
        data = self._format(expected)
        self.dpc.store(data)
        assert self.dpc.to_json == dumps(expected)

    def _format(self, expected):
        return [(d['Date'], d['Booked']['Males']['AS']) for d in expected]

