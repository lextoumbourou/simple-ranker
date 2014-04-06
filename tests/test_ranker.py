import unittest
import datetime

import pandas as pd

from simple_ranker import Ranker
from tests import stock_data

class RankerTest(unittest.TestCase):
    def setUp(self):
        self.current_year = datetime.datetime.now().year

    def test_rank_by_PE_returns_lowest_first(self):
        pe_rank = {
            'name': 'pe',
            'ascending': True
        }
        data = pd.DataFrame({
            'code': ['ANZ', 'CBA', 'NAB'],
            'pe': [3.0, 1.0, 2.0],
        }, index=pd.to_datetime(
            [datetime.date(self.current_year, 6, 20)] * 3), dtype=float
        )

        ranker = Ranker(data, [pe_rank], [], limit=50)
        results = ranker.process()

        self.assertTrue(results[0:1]['code'][0] == 'CBA')

    def test_rank_by_ROE_return_highest_first_after_filtering(self):
        roe_rank = {
            'name': 'roe',
            'max': 0.70,
            'ascending': False
        }
        data = pd.DataFrame({
            'code': ['ANZ', 'CBA', 'NAB'],
            'roe': [0.70, 0.71, 0.69]},
            index=pd.to_datetime(
                [datetime.date(self.current_year, 6, 20)] * 3
            ), dtype=float
        )

        ranker = Ranker(data, [roe_rank], [], limit=50)
        results = ranker.process()

        self.assertTrue(results[0:1]['code'][0] == 'ANZ')

    def test_rank_and_filter_removes_too_small_companies(self):
        market_cap_filter = {
            'name': 'market_cap',
            'min': 5000000
        }
        roe_rank = {
            'name': 'roe',
            'max': 0.70,
            'ascending': False
        }
        data = pd.DataFrame({
            'code': ['SMALL', 'ANZ', 'CBA', 'NAB'],
            'roe': [0.50, 0.40, 0.41, 0.39],
            'market_cap': [1000000] + [6000000] * 3},
            index=pd.to_datetime(
                [datetime.date(self.current_year, 6, 20)] * 4
            ), dtype=float
        )

        ranker = Ranker(data, [roe_rank], [market_cap_filter], limit=50)
        results = ranker.process()

        self.assertTrue(results[0:1]['code'][0] == 'CBA')

    def test_rank_ROE_and_PE_returns_correct_top(self):
        roe_rank = {
            'name': 'roe',
            'ascending': False
        }
        pe_rank = {
            'name': 'pe',
            'ascending': True
        }

        
        data = pd.DataFrame({
                'code': ['ANZ', 'CBA', 'NAB', 'WST'],
                'pe': [3, 4, 5, 6],
                'roe': [0.30, 0.50, 0.80, 0.70]
            },
            index=pd.to_datetime(
                [datetime.date(self.current_year, 6, 20)] * 4
            ), dtype=float
        )

        ranker = Ranker(data, [pe_rank, roe_rank], [], limit=50)
        results = ranker.process()

        # Output should look like this:
        # code  pe_rank  roe_rank  total_rank
        # ANZ    1         4        5       
        # CBA    2         3        5
        # NAB    3         1        4  -- first pick
        # WST    4         2        6  -- last pick
        self.assertTrue(results[0:1]['code'][0] == 'NAB')
        self.assertTrue(results[-1:]['code'][0] == 'WST')

    def test_rank_ROE_avg_3_returns_correct_top(self):
        roe_rank = {
            'name': 'roe',
            'max': 0.8,
            'average': 3,
            'ascending': False
        }

        # Push last 3 years into a list
        date_array = [datetime.date(self.current_year - i, 6, 20) for i in range(3)]

        data = pd.DataFrame({
            'code': ['ANZ'] * 3 + ['CBA'] * 3 + ['NAB'] * 3,
            'roe': [0.1, 0.2, 0.5] + [0.7, 0.1, 0.2] + [0.1, 0.2, 0.4]},
            index=pd.to_datetime(date_array * 3), dtype=float
        )

        ranker = Ranker(data, [roe_rank], [], limit=50)
        results = ranker.process()

        self.assertTrue(results[0:1]['code'][0] == 'CBA')
        self.assertTrue(results[-1:]['code'][0] == 'NAB')

if __name__ == '__main__':
    unittest.run()
