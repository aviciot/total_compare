from excel import ExcelFileReader
from settings import Settings



if __name__ == "__main__":
    # Example usage
    config_file_path = "config/config.yml"
    settings = Settings(config_file_path)
    # Accessing settings variables
    file_path = settings['excel_settings.file_path']
    print("Excel file path:", file_path)