import datetime

current_year = datetime.datetime.now().year

data = {
    'book_value':[
        '30.27', '21.27',  '20.27',  '19.27', '20.27',  '18.18',  '31.27',
        '21.45', '20.27', '19.27', '20.27', '18.18', '31.27', '21.45',
        '20.27', '19.27', '20.27', '18.18', '31.27', '21.45', '20.27',
        '19.27', '20.27', '18.18'], 
    'code': [
        'ANZ', 'ANZ',  'ANZ', 'ANZ', 'ANZ', 'ANZ',
        'CBA', 'CBA', 'CBA', 'CBA', 'CBA', 'CBA',
        'ARB', 'ARB', 'ARB', 'ARB', 'ARB', 'ARB',
        'SRX', 'SRX', 'SRX', 'SRX', 'SRX', 'SRX'],
    'date': [
        datetime.date(current_year, 6, 20), 
        datetime.date(current_year - 1, 6, 20),
        datetime.date(current_year - 2, 6, 20),
        datetime.date(current_year - 3, 6, 20),
        datetime.date(current_year - 4, 6, 20),
        datetime.date(current_year - 5, 6, 20),
        datetime.date(current_year, 6, 20), 
        datetime.date(current_year - 1, 6, 20),
        datetime.date(current_year - 2, 6, 20),
        datetime.date(current_year - 3, 6, 20),
        datetime.date(current_year - 4, 6, 20),
        datetime.date(current_year - 5, 6, 20),
        datetime.date(current_year, 6, 20), 
        datetime.date(current_year - 1, 6, 20),
        datetime.date(current_year - 2, 6, 20),
        datetime.date(current_year - 3, 6, 20),
        datetime.date(current_year - 4, 6, 20),
        datetime.date(current_year - 5, 6, 20),
        datetime.date(current_year, 6, 20), 
        datetime.date(current_year - 1, 6, 20),
        datetime.date(current_year - 2, 6, 20),
        datetime.date(current_year - 3, 6, 20),
        datetime.date(current_year - 4, 6, 20),
        datetime.date(current_year - 5, 6, 20),
    ], 
    'earnings': [
        '23.20', '21.20', '21.50', '20.50', '19.50', '18.20', '23.20', '15.70',
        '21.50', '20.50', '19.50', '18.20', '23.20', '15.70', '21.50', '20.50',
        '19.50', '18.20', '23.20', '15.70', '21.50', '20.50', '19.50', '18.20'
    ],
    'market_cap': [
        6400000, 6300000, 6100000, 6100000, 8100000, 7300000, 8500000, 6450000,
        6100000, 6100000, 8100000, 7300000, 8000000, 6450000, 6100000, 6100000,
        8100000, 7300000, 4000000, 6450000, 6100000, 6100000, 8100000, 7300000
    ],
    'pe': [
        '8.50', '8.40', '7.40', '6.40', '7.20', '6.90', '9.40', '8.90', '7.90',   '6.90',   '7.90',   '8.90',   '5.40',   '8.90',   '7.90',   '6.90',   '7.90',   '8.90',   '5.80',   '8.90',   '7.90',   '6.90',   '7.90',   '8.90'
    ],
    'roe': [
        '0.09',   '0.10',   '0.10',   '0.10',   '0.12',   '0.13',   '0.40',   '0.21',   '0.22',   '0.24',   '0.26',   '0.23',   '2.25',   '0.34',   '0.36',   '0.37',   '0.38',   '0.13',   '0.65',   '0.62',   '0.61',   '0.55',   '0.43',   '0.52'
    ],
    'shares_outstanding': [
        216100000,   216100000,   216100000,   216100000,   216100000,   216100000,   216100000,   216100000,   216100000,   216100000,   216100000,   216100000,   216100000,   216100000,   216100000,   216100000,   216100000,   216100000,   216100000,   216100000,   216100000,   216100000,   216100000,   216100000
    ]
}
