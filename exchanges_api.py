import requests

def gate(token: str):
    token = token + '_USDT'
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    url = '/futures/usdt/tickers'
    r = requests.get(host + prefix + url, headers=headers)

    if r.status_code != 200:
        print(f"Error: {r.status_code}")
        return

    data = r.json()
    filtered = next((item for item in data if item['contract'] == token), None)
    
    return float(filtered['funding_rate'])*100
