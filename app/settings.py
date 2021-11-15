from model import PoloniexCoin, ExmoCoin, HitBtcCoin

delay = 120

polonex_api = 'https://poloniex.com/public?command=returnTicker'
exmo_api = 'https://api.exmo.com/v1.1/ticker/'
hitbtc_api = 'https://api.hitbtc.com/api/3/public/ticker'

LIST_COIN_AND_LINKS = {
	PoloniexCoin: polonex_api,
	ExmoCoin: exmo_api,
	HitBtcCoin: hitbtc_api,
}

CURRENCY_PAIRS = [
	['ETH_BTC', 'BTC_ETH', 'ETHBTC'],
	['DASH_BTC', 'BTC_DASH', 'DASHBTC'],
	['DCR_BTC', 'BTC_DCR', 'DCRBTC'],
	['DOGE_BTC', 'BTC_DOGE', 'DOGE_BTC'],
	['XRP_BTC', 'BTC_XRP', 'XRPBTC']
]