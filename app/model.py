from pydantic import BaseModel, Field


class ExmoAttribute(BaseModel):
	ask: str = Field(alias='buy_price')
	bid: str = Field(alias='sell_price')
	cryptocurrency = 'Exmo Coin'


class ExmoCoin(BaseModel):
	ETH_BTC: ExmoAttribute
	DASH_BTC: ExmoAttribute
	DCR_BTC: ExmoAttribute
	DOGE_BTC: ExmoAttribute
	XRP_BTC: ExmoAttribute


class PoloniexAttribute(BaseModel):
	ask: str = Field(alias='lowestAsk')
	bid: str = Field(alias='highestBid')
	cryptocurrency = 'Poloniex Coin'


class PoloniexCoin(BaseModel):
	BTC_ETH: PoloniexAttribute
	BTC_DASH: PoloniexAttribute
	BTC_DCR: PoloniexAttribute
	BTC_DOGE: PoloniexAttribute
	BTC_XRP: PoloniexAttribute


class HitbtcAttribute(BaseModel):
	ask: str
	bid: str
	cryptocurrency = 'HITBTC Coin'


class HitBtcCoin(BaseModel):
	ETHBTC: HitbtcAttribute
	DASHBTC: HitbtcAttribute
	DCRBTC: HitbtcAttribute
	DOGEBTC: HitbtcAttribute
	XRPBTC: HitbtcAttribute
