import asyncio
import aiohttp
from datetime import datetime

from view import ResultConstructor
from settings import LIST_COIN_AND_LINKS, delay


rc = ResultConstructor()

async def prepare_result(data, coin):
	rc.add_df(coin.parse_obj(data).json())
	rc.view_result(rc.join_coin())
	rc.clear_result()


async def fetch_connect(url, session, coin):
	async with session.get(url) as response:
		data = await response.json()
		await prepare_result(data, coin)


async def main(array):
	tasks = []
	async with aiohttp.ClientSession() as session:
		for coin, url in array.items():
			task = asyncio.create_task(fetch_connect(url, session, coin))
			tasks.append(task)
		await asyncio.gather(*tasks, return_exceptions=True)
	await asyncio.sleep(delay)



if __name__ == '__main__':
	while True:
		print('*' * 50)
		print('Start {}'.format(datetime.now()))
		print('*' * 50)
		loop = asyncio.get_event_loop()
		loop.run_until_complete(main(LIST_COIN_AND_LINKS))
