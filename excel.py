import pandas as pd

class ExcelLoader:
    def __init__(self, file_name):
        self.file_name = file_name
        self.xls = None
        self.sheet_names = []

    def read_excel_file(self):
        try:
            # Read the Excel file
            self.xls = pd.ExcelFile(self.file_name)

            # Get the sheet names dynamically
            self.sheet_names = self.xls.sheet_names

        except FileNotFoundError:
            print(f"File '{self.file_name}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def read_and_display_selected_sheets_info(self, selected_sheets):
        # Read and display information for the specified sheets
        for sheet_name in selected_sheets:
            try:
                sheet_data = pd.read_excel(self.file_name, sheet_name)

                # Display sheet information
                print(f"\nSheet '{sheet_name}':")
                print(f"Number of rows: {len(sheet_data)}")
                print(f"Number of columns: {len(sheet_data.columns)}")

            except pd.errors.ParserError:
                print(f"Error reading sheet '{sheet_name}'. Check if the sheet exists.")

    def display_all_sheets_info(self):
        # Print the number of sheets
        print(f"Number of sheets in '{self.file_name}': {len(self.sheet_names)}")

        # Print the names of sheets
        print("Sheet names:")
        for sheet_name in self.sheet_names:
            print(f"- {sheet_name}")

# Example usage
file_name = "qatool.xlsx"
excel_reader = ExcelLoader(file_name)
excel_reader.read_excel_file()

# Specify the sheets you want to read
sheets_to_read = ["counts", "checks", "connections"]

# Display information for the specified sheets
excel_reader.read_and_display_selected_sheets_info(sheets_to_read)
excel_reader.display_all_sheets_info()
