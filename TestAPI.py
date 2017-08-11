import quandl

quandl.ApiConfig.api_key = ""
data = quandl.get_table('ZACKS/FE', paginate=True)

data.to_csv('out.csv')
