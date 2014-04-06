from datetime import datetime


class Ranker():
    def __init__(self, data, rank_methods=[], filter_methods=[], limit=50):
        self.rank_methods = rank_methods
        self.filter_methods = filter_methods

        self.data = data
        self.limit = limit

    def _prefilter_data(self):
        for method in self.rank_methods + self.filter_methods:
            self.data = self._perform_filter(method, self.data)

    def _perform_filter(self, method, data):
        name = method['name']
        if method.get('max'):
            data = data[data[name] <= method['max']]
        if method.get('min'):
            data = data[data[name] >= method['min']]

        return data

    def process(self):
        today = datetime.today()
        self._prefilter_data()

        ## Just get this years data
        this_years_data = self.data[str(today.year)]

        # Create an empty rank table filled with zeros
        this_years_data['total_rank'] = 0

        # Create the ranks and do the filtering on averaged values
        for method in self.rank_methods:
            # Average if requested
            if method.get('average') > 1:
                del(this_years_data[method['name']])

                this_years_data = this_years_data.join(
                    self.data.groupby(self.data.code)[method['name']].mean(),
                    on='code'
                )

                this_years_data = self._perform_filter(method, this_years_data)

            this_years_data['total_rank'] += (
                this_years_data[method['name']].rank(
                    ascending=method.get('ascending', False)
                )
            )

        return this_years_data.sort(['total_rank', 'code'])[:self.limit]
