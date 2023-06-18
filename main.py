from full_fred.fred import Fred
import pandas as pd
import nasdaqdatalink
import requests
import datetime
import csv
import altair as alt
alt.renderers.enable('notebook')
from altair import Chart, Scale, Y
from dbnomics import fetch_series, fetch_series_by_api_link


fred = Fred('key.txt')
# # Consumer Price Index for All Urban Consumers: All Items in U.S. City Average
# # https://fred.stlouisfed.org/series/CPIAUCSL
# fred = Fred('key.txt')
# inflation_data = fred.get_series_df('CPIAUCSL')
# inflation_data.drop(['realtime_start', 'realtime_end'], axis=1, inplace=True)
# inflation_data['value'] = pd.to_numeric(inflation_data['value'])
# inflation_data['pct_change'] = inflation_data['value'].diff(periods=12)
# print(inflation_data)
#
# # Nominal Broad U.S. Dollar Index https://fred.stlouisfed.org/series/DTWEXBGS
# fx_data = fred.get_series_df('DTWEXBGS')
# fx_data.drop(['realtime_start', 'realtime_end'], axis=1, inplace=True)
# fx_data.replace('.', None, inplace=True)
# fx_data['value'] = pd.to_numeric(fx_data['value'])
# fx_data['pct_change'] = fx_data['value'].pct_change(periods=261)
# fx_data.dropna(inplace=True)
# print(fx_data)
#
# # Market Yield on U.S. Treasury Securities at 2-Year Constant Maturity, Quoted on an Investment Basis https://fred.stlouisfed.org/series/DGS2
# treasury_data = fred.get_series_df('DGS2')
# treasury_data.drop(['realtime_start', 'realtime_end'], axis=1, inplace=True)
# treasury_data.replace('.', None, inplace=True)
# treasury_data['value'] = pd.to_numeric(treasury_data['value'])
# treasury_data['yield_change'] = treasury_data['value'].diff(periods=258)
# treasury_data.dropna(inplace=True)
# print(treasury_data)
#
# S&P 500 Index https://fred.stlouisfed.org/series/SP500
# sandp_data = fred.get_series_df('SP500')
# sandp_data.drop(['realtime_start', 'realtime_end'], axis=1, inplace=True)
# sandp_data.replace('.', None, inplace=True)
# sandp_data['value'] = pd.to_numeric(sandp_data['value'])
# sandp_data['pct_change'] = sandp_data['value'].pct_change(periods=261)
# sandp_data.dropna(inplace=True)
# print(sandp_data)
#
# # US ISM PMI https://www.mql5.com/en/economic-calendar/united-states/ism-manufacturing-pmi
# pmi_data = pd.read_table("us_pmi.csv", sep="\t")
# pmi_data = pmi_data.iloc[::-1,:]
# pmi_data['ActualDiff'] = pmi_data['ActualValue'].diff(periods=12)
# print(pmi_data.tail(20))

# # Long-Term Government Bond Yields: 10-year: Main (Including Benchmark) for Japan
# # https://fred.stlouisfed.org/series/IRLTLT01JPM156N
# fred = Fred('key.txt')
# yields_jp = fred.get_series_df('IRLTLT01JPM156N')
# yields_jp.drop(['realtime_start', 'realtime_end'], axis=1, inplace=True)
# yields_jp['value'] = pd.to_numeric(yields_jp['value'])
# yields_jp['pct_change'] = yields_jp['value'].diff(periods=12)
# print(yields_jp)

# def fred_1y_diff(fred_ticker):
#     fred = Fred('key.txt')
#     variable = fred.get_series_df(fred_ticker)
#     variable.drop(['realtime_start', 'realtime_end'], axis=1, inplace=True)
#     variable['value'] = pd.to_numeric(variable['value'])
#     variable['pct_change'] = variable['value'].diff(periods=12)
#     return variable.iloc[-1, -1]
#
# def fred_1y_percent(fred_ticker):
# 	"""helps obtain percentage change from one year ago, for those data on FRED database.Used on indices"""
#     fred = Fred('key.txt')
# 	variable = fred.get_series_df(fred_ticker)
#     variable.drop(['realtime_start', 'realtime_end'], axis=1, inplace=True)
#     variable.replace('.', None, inplace=True)
#     variable['value'] = pd.to_numeric(variable['value'])
#     variable['pct_change'] = variable['value'].pct_change(periods=261)
#     variable.dropna(inplace=True)
#
#     return variable.iloc[-1]
#
# print(fred_1y_percent('SP500'))
#
# equity_markets = ['SP500', 'NIKKEI225']


# data = nasdaqdatalink.get('NSE/OIL') # nasdaq data link

# Open the CSV file containing index list
with open('index_tickers_list.csv', 'r') as file:
    csv_reader = csv.reader(file)
    row = next(csv_reader)

# Convert the row into a list
index_list = list(row)

url = "https://yahoo-finance127.p.rapidapi.com/historic/%5EMXX/1d/12mo"

headers = {
	"X-RapidAPI-Key": "872941abc9msh02f8c7a75bb508cp135f37jsndcc1ea627184",
	"X-RapidAPI-Host": "yahoo-finance127.p.rapidapi.com"
}

def yfinance_1y_diff(url, headers):
	response = requests.get(url, headers = headers)
	variable = dict(response.json())
	adjusted_close = variable["indicators"]['adjclose'][0]['adjclose']
	yr_change = (adjusted_close[-1] - adjusted_close[0]) / adjusted_close[0]

	# temporary
	# readable_time = []
	# for timestamp in variable['timestamp']:
	# 	# Convert Unix timestamp to datetime object
	# 	dt = datetime.datetime.fromtimestamp(timestamp)
	# 	# Convert datetime object to a readable string format
	# 	formatted_time = dt.strftime('%Y-%m-%d')
	# 	readable_time.append(formatted_time)
	return (yr_change)

# print(yfinance_1y_diff(url, headers))
# for index in index_list:
# 	if index.startswith("^"):
# 		modified_url = url.replace("%5EMXX", f"%5{index[1:]}")
# 	else:
# 		modified_url = url.replace("%5EMXX", index)
#
# 	print(modified_url)


one_year_equity_returns = {}
for index in index_list:
	if index.startswith("^"):
		modified_url = url.replace("%5EMXX", f"%5E{index[1:]}")
	else:
		modified_url = url.replace("%5EMXX", index)

	one_year_equity_returns[index] = yfinance_1y_diff(modified_url, headers)

#dkjdfksjdnfwjndn

print(one_year_equity_returns)


# def
# readable_time = []
# for timestamp in ftse['timestamp']:
# 	# Convert Unix timestamp to datetime object
# 	dt = datetime.datetime.fromtimestamp(timestamp)
# 	# Convert datetime object to a readable string format
# 	formatted_time = dt.strftime('%Y-%m-%d')
# 	readable_time.append(formatted_time)
#
# adjusted_close = ftse['adjclose']['adjclose']
#
#
# Create a dictionary from the lists
# ftsedata = {'Column1': list1, 'Column2': list2}
#
# Create a dataframe from the dictionary
# df = pd.DataFrame(data)
#
# print(df)
#
# print(readable_time)