import pandas as pd

from settings import CURRENCY_PAIRS


class ResultConstructor:

	def __init__(self):
		self._data_frames = []
		pd.set_option('display.max_rows', None)
		pd.set_option('display.max_columns', None)
		pd.set_option('display.max_colwidth', None)

	def add_df(self, json):
		df = pd.DataFrame(eval(json))
		self._data_frames.append(df)

	def join_coin(self):
		join_result = [df for df in self._data_frames]
		return pd.concat(join_result, axis=1)

	def clear_result(self):
		self._data_frames.clear()

	def _sort_result(self, result):
		return f"Sorted ASK:\n {result.transpose().sort_values(by='ask')}\n" \
		       f"Sorted BID:\n {result.transpose().sort_values(by='bid')}\n"

	def view_result(self, df):
		for cur_pair in CURRENCY_PAIRS:
			print(self._sort_result(df[cur_pair]))
