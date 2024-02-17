import yaml





class SettingsLoader:
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
        self.settings = self._load_settings()

    def _load_settings(self):
        with open(self.config_file_path, 'r') as config_file:
            return yaml.safe_load(config_file) or {}

    def __call__(self, parameter=None):
        if parameter is None:
            return self.settings
        return self._get_nested_setting(parameter)

    def _get_nested_setting(self, parameter):
        keys = parameter.split('.')
        current_dict = self.settings
        for key in keys:
            current_dict = current_dict.get(key, {})
        return current_dict

    def __str__(self):
        return "\n".join(f"{key}: {value}" for key, value in vars(self).items())



#
#
#
# class Settings:
#     _instance = None  # Class variable to store the instance
#
#     def __new__(cls, config_path):
#         if cls._instance is None:
#             cls._instance = super(Settings, cls).__new__(cls)
#             cls._instance.config_path = config_path
#             cls._instance.excel_settings = {}
#             cls._instance.database_settings = {}
#             cls._instance.data_sources = {}
#             cls._instance._read_config()
#         return cls._instance
#
#     def _read_config(self):
#         # Read configuration from YAML file
#         with open(self.config_path, 'r') as config_file:
#             config_data = yaml.safe_load(config_file)
#             self.excel_settings = config_data.get('excel_settings')
#             self.database_settings = config_data.get('databases', {})
#             self.data_sources = config_data.get('data_sources', {})
#
#     def get_settings(self, parameter=None):
#         if parameter is None:
#             return self.settings
#         return self._get_nested_setting(parameter)
#
#     def _get_nested_setting(self, parameter):
#         keys = parameter.split('.')
#         current_dict = self.settings
#         for key in keys:
#             current_dict = current_dict.get(key, {})
#         return current_dict
#
#     def __str__(self):
#         return "\n".join(f"{key}: {value}" for key, value in vars(self).items())



if __name__ == "__main__":
    # Example usage
    config_file_path = "config/config.yml"
    loader1 = SettingsLoader(config_file_path)


    # Accessing and printing nested settings using the __call__ method
    excel_file_path = loader1('excel_settings.file_path')
    print("Excel file path:", excel_file_path)

    # Creating another instance with the same config file path
    loader2 = SettingsLoader(config_file_path)

    # Check if they are the same instance using id()
    assert id(loader1) != id(loader2) ,"both id as SettingsLoader is singeltone"



    excel_sheets = loader2('excel_settings.sheets')
    print("Excel sheets:", excel_sheets)

    sqlite_table_name = loader2('databases.sqlite.table_name')
    print("SQLite table name:", sqlite_table_name)