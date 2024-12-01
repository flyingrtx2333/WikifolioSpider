import requests


def get_tickers():
    """get the timestamp and price value"""
    url = f"https://www.wikifolio.com/api/chart/be2b8159-d9e7-4ab0-94af-efceb63706ad/wikifolioindex?country=de&language=de"

    response = requests.get(
        url=url,
        headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
        }
    )
    data = response.json()
    timestamps = data['timestamps']
    values = data['values']
    print(len(timestamps), len(values))


if __name__ == '__main__':
    get_tickers()
