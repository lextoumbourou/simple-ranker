# simple-ranker

[![Build Status](https://travis-ci.org/lextoumbourou/simple-ranker.svg?branch=master)](https://travis-ci.org/lextoumbourou/simple-ranker)

*An extremely simple, multi-value ranking module for [pandas](http://pandas.pydata.org) DataFrames.*


Based on the algorithm from The Little Book That Beats the Market, and the backbone behind [MagicRanker](http://www.magicranker.com).



## Usage

The Ranker class takes in a timeseries indexed pandas DataFrame and a list of rank and filter dicts. For example, let's say I have timeseries DataFrame that looks like this:

```
>>> df
            code  pe   roe
2014-06-20  ANZ   5  0.70
2014-06-20  CBA   4  0.25
2014-06-20  NAB  10  0.14

[3 rows x 3 columns]
```

Perhaps I wanted to simply rank it by roe? I would do so like this:

```
>>> from simple_ranker import Ranker
>>> roe_rank = {'name': 'roe'}
>>> r = Ranker(df, [roe_rank])
>>> print r.process()
           code  pe   roe  total_rank
2014-06-20  ANZ   5  0.70           1
2014-06-20  CBA   4  0.25           2
2014-06-20  NAB  10  0.14           3

[3 rows x 4 columns]
```

Now, what if we wanted to rank them by both roe and pe. We'd do this:

```
>>> roe_rank = {'name': 'roe'}
>>> pe_rank = {'name': 'pe', 'ascending': True}
>>> r = Ranker(df, [roe_rank, pe_rank])
>>> print r.process()
           code  pe   roe  total_rank
2014-06-20  ANZ   5  0.70           3
2014-06-20  NAB  10  0.14           4
2014-06-20  CBA   4  0.25           5

[3 rows x 4 columns]
```

Note that we add the ```ascending``` key to the ```pe_rank``` dict in order to rank from lowest to highest (descending is default).

Perhaps, I have timeseries data that spanned more than one year. I could choose to average the data over a timeframe before ranking:

```
>>> roe_rank = {'name': 'roe', 'average': 3}
>>> pe_rank = {'name': 'pe', 'ascending': True}
>>> r = Ranker(df, [roe_rank, pe_rank])
>>> print r.process()
```

Or I could filter out certain values by adding a max and min key to the rank dict

```
>>> roe_rank = {'name': 'roe', 'average': 3, 'max': 0.70}
>>> pe_rank = {'name': 'pe', 'ascending': True, 'min': 5}
>>> r = Ranker(df, [roe_rank, pe_rank])
>>> print r.process()
```

## Ranking algorithm

The ranking algorithm is extremely straight-forward:

1. Take the first column and rank.
2. Take the second column and rank.
3. Create a total rank by adding the ranks from the first column to the second column.

## Tests

Firstly, ensure the ```dev-requirements``` are installed (probably best to put it in a virtualenv):

```
> virtualenv env
> . env/bin/activate
(env)> pip install -r dev-requirements.txt
```

Run tests via [nose](https://pypi.python.org/pypi/nose), like so:

```
(env)> nosetests
```

Nose is configured to integrate with [coverage](https://pypi.python.org/pypi/coverage) (on the 100% test coverage tip).

## License

[MIT](./LICENSE)
