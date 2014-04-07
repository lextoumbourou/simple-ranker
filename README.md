# simple-ranker

simple-ranker is an extremely simple ranking module for pandas DataFrames. It is based on the algorithm from The Little Book That Beats the Market, it is the backbone behind [MagicRanker](http://www.magicranker.com).

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
>>> pe_rank = {'name': 'pe'}
>>> r = Ranker(df, [roe_rank, pe_rank])
>>> print r.process()
           code  pe   roe  total_rank
2014-06-20  ANZ   5  0.70           3
2014-06-20  NAB  10  0.14           4
2014-06-20  CBA   4  0.25           5

[3 rows x 4 columns]
```

Perhaps, I have timeseries data that spanned more than one year, I could choose to average the data over a timeframe before ranking:

```
>>> roe_rank = {'name': 'roe', 'average': 3}
>>> pe_rank = {'name': 'pe'}
>>> r = Ranker(df, [roe_rank, pe_rank])
>>> print r.process()
```

Or I could filter out certain values by adding a max and min key to the rank dict

```
>>> roe_rank = {'name': 'roe', 'average': 3, 'max': 0.70}
>>> pe_rank = {'name': 'pe', 'min': 5}
>>> r = Ranker(df, [roe_rank, pe_rank])
>>> print r.process()
```

## Ranking algorithm

The ranking algorithm is extremely straight-forward:

1. Take the first column and rank.
2. Take the second column and rank.
3. Create a total rank by adding the ranks from the first column to the second column.

## License

[MIT](./LICENSE)
