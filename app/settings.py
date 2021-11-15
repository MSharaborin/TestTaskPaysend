from model import PoloniexCoin, ExmoCoin, HitBtcCoin

delay = 120

LIST_COIN_AND_LINKS = {
	PoloniexCoin: 'https://poloniex.com/public?command=returnTicker',
	ExmoCoin: 'https://api.exmo.com/v1.1/ticker/',
	HitBtcCoin: 'https://api.hitbtc.com/api/3/public/ticker',
}

CURRENCY_PAIRS = [
	['ETH_BTC', 'BTC_ETH', 'ETHBTC'],
	['DASH_BTC', 'BTC_DASH', 'DASHBTC'],
	['DCR_BTC', 'BTC_DCR', 'DCRBTC'],
	['DOGE_BTC', 'BTC_DOGE', 'DOGE_BTC'],
	['XRP_BTC', 'BTC_XRP', 'XRPBTC']
]