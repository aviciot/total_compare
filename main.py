from excel import ExcelLoader
from settings import SettingsLoader



if __name__ == "__main__":
    # Example usage
    config_file_path = "config/config.yml"
    settings = SettingsLoader(config_file_path)
    # Accessing settings variables
    file_path = settings('excel_settings.file_path')
    print("Path",file_path)
    # curr = ExcelLoader(file_path=file_path)
    # print("Excel file path:", curr.display_sheets())