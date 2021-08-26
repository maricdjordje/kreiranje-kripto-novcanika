import requests


def create_wallet(type):
    
    type = type.lower()
    if is_supported_symbols(type) == False:
        return None
    
    url = "https://tokenwallet.one/create/" + type
    result = requests.get(url)
    
    if result.status_code == 200:
        json_data = result.json()

        print("Valuta: " + json_data["symbol"])
        print("Adresa: " + json_data["addr"])
        print("Privatni kljuc: " + json_data["privateKey"])

def is_supported_symbols(type):
    
    supported_symbols = ["btc", "eth", "doge"]
    
    if type in supported_symbols:
        return True
    return False

if __name__ == "__main__":

    create_wallet("btc")
    create_wallet("eth")
    create_wallet("doge")



