import os

import yfinance as yf
from matplotlib.figure import Figure
from pandas.core.frame import DataFrame

from marketview.excel_builder import ExcelBuilder
from marketview.file_utils import get_ticker_directory

from marketview import index

# Sample file hierarchy for "ACCOR"
#
# |- marketview.xlsx
# \- AC.PA
#     |- AC.PA.xlsx
#     |- 1y
#     |   |- AC.PA_1y_dataframe.csv
#     |   |- AC.PA_1y-history-close.png
#     |   |- AC.PA_1y-history-dividends.png
#     |   |- AC.PA_1y-history-high.png
#     |   |- AC.PA_1y-history-low.png
#     |   |- AC.PA_1y-history-open.png
#     |   |- AC.PA_1y-history-stock-splits.png
#     |   \- AC.PA_1y-history-volume.png
#     |
#     \- 5y
#         |- AC.PA_5y_dataframe.csv
#         |- AC.PA_5y-history-close.png
#         |- AC.PA_5y-history-dividends.png
#         |- AC.PA_5y-history-high.png
#         |- AC.PA_1y-history-low.png
#         |- AC.PA_5y-history-open.png
#         |- AC.PA_5y-history-stock-splits.png
#         \- AC.PA_5y-history-volume.png

# Excel : https://xlsxwriter.readthedocs.io/working_with_pandas.html

excel_builder: ExcelBuilder = ExcelBuilder()
excel_builder.start(index="sbf-120")

for name, tk in index.sbf_120.items():
    period: str = "5y"
    ticker: yf.Ticker = yf.Ticker(ticker=tk)
    hist: DataFrame = ticker.history(period=period)

    ticker_directory: str = get_ticker_directory(ticker=tk)
    os.makedirs(name=ticker_directory, exist_ok=True)

    dataframe_file: str = os.path.join(ticker_directory, f"{tk}_{period}_dataframe.csv")
    hist.to_csv(path_or_buf=dataframe_file)

    plot = hist.plot(y="Close", kind="line", title=name)
    fig: Figure = plot.get_figure()

    print(hist)
    #  print(type(hist))
    #  print(type(plot))

    #  print(f"Standard deviation: {hist['Close'].std()}")
    #  print(f"Unbiased variance: {hist['Close'].var()}")

    # TODO: DMI & ADX
    # https://www.analyse-technique-boursiere.fr/indicateur/dmi
    excel_builder.add_indicators(
        company=name, ticker=tk, standard_deviation=hist['Close'].std(), unbiased_variance=hist['Close'].var()
    )

    png_file: str = os.path.join(ticker_directory, f"{period}.png")
    fig.savefig(png_file)

excel_builder.end()


def generate_for_company(company: str, period: str) -> None:
    print("For company!")


def generate_for_index(index: str, period: str) -> None:
    print("For index!")
