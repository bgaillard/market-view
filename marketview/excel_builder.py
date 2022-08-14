import os
from typing import Optional

import pandas as pd
from pandas.io.excel._xlsxwriter import XlsxWriter

from xlsxwriter.format import Format
from xlsxwriter.workbook import Workbook
from xlsxwriter.worksheet import Worksheet

from marketview.file_utils import get_app_directory


class ExcelBuilder:

    def add_indicators(self, company: str, ticker: str, standard_deviation: float, unbiased_variance: float) -> None:
        row_number: int = self.indicators_added + 2
        self.indicators_worksheet.write(f'A{row_number}', company)
        self.indicators_worksheet.write(f'B{row_number}', ticker)
        self.indicators_worksheet.write(f'C{row_number}', standard_deviation)
        self.indicators_worksheet.write(f'D{row_number}', unbiased_variance)

        self.indicators_added = self.indicators_added + 1

    def end(self) -> None:
        self.get_workbook().close()

    def get_workbook(self) -> Workbook:
        if not self.workbook:
            raise ValueError("Excel workbook not initialized!")

        return self.workbook

    def start(self, index: str) -> None:
        app_directory: str = get_app_directory()
        os.makedirs(name=app_directory, exist_ok=True)
        excel_file: str = os.path.join(get_app_directory(), f"{index}.xlsx")

        self.workbook: Workbook = Workbook(excel_file)

        self.header_format: Format = self.workbook.add_format(
            {
                'bg_color': 'blue',
                'bold': True,
                'font_color': 'white'
            }
        )

        # Create the 'indicators' sheet
        self.indicators_added: int = 0
        self.indicators_worksheet = self.workbook.add_worksheet('Indicators')
        self.indicators_worksheet.write('A1', 'Company', self.header_format)
        self.indicators_worksheet.write('B1', 'Ticker', self.header_format)
        self.indicators_worksheet.write('C1', 'Standard deviation', self.header_format)
        self.indicators_worksheet.write('D1', 'Unbiased variance', self.header_format)
