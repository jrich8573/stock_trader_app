import requests

API_KEY = '<<API Key Store>>'

def get_sp500_data():
    try:
        endpoint = 'https://www.alphavantage.co/query'
        params = {
        'function':'TIME_SERIES_DAILY_ADJUSTED',
        'symbol':'SPY', #spy is the etf the tracks the sp
        'apikey': API_KEY,
        }
        response = requests.get(endpoint, params = params)
        response.raise_for_status()
        
        data = response.json()
    
        time_series = data.get('Time Series(Daily)', {})
        sp500_data = {}
    
        for data, values in time_series.items():
            sp500_data[data] = {
                'open': float(values['1. Open']),
                'high': float(values['2. High']),
                'low': float(values['3. Low']),
                'close': float(values['4. Close']),
                'volume': float(values['5. Volume']),
            }
        return sp500_data
    
    except requests.exceptions.RequestException as e:
        print(f"Error making Alpha Vantage API RequestL {e}")
        return {}
    except ValueError as e:
        print(f"Error parsing JSON response: {e}")
        return {}
    
if __name__ == "__main__":
    sp500_data = get_sp500_data()
    print(sp500_data)