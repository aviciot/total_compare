import pandas as pd


class ExcelFileReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.sheet1_data = None
        self.sheet2_data = None

    def read_excel_file(self):
        # Read Excel file into DataFrames
        excel_data = pd.read_excel(self.file_path, sheet_name=None)
        self.sheet1_data = excel_data.get('Sheet1')
        self.sheet2_data = excel_data.get('Sheet2')

    def get_row_counts(self):
        # Get row counts for each sheet
        sheet1_rows = len(self.sheet1_data) if self.sheet1_data is not None else 0
        sheet2_rows = len(self.sheet2_data) if self.sheet2_data is not None else 0
        return {'Sheet1': sheet1_rows, 'Sheet2': sheet2_rows}

    def compare_sheets(self):
        # Compare sheet data
        if self.sheet1_data is not None and self.sheet2_data is not None:
            return self.sheet1_data.equals(self.sheet2_data)
        return False

    def establish_connections(self):
        # Establish connections between sheets
        if self.sheet1_data is not None and self.sheet2_data is not None:
            common_column = set(self.sheet1_data.columns) & set(self.sheet2_data.columns)
            return list(common_column)
        return []

