import yaml

class Settings:
    _instance = None  # Class variable to store the instance

    def __new__(cls, config_path):
        if cls._instance is None:
            cls._instance = super(Settings, cls).__new__(cls)
            cls._instance.config_path = config_path
            cls._instance.excel_settings = {}
            cls._instance.database_settings = {}
            cls._instance.data_sources = {}
            cls._instance._read_config()
        return cls._instance

    def _read_config(self):
        # Read configuration from YAML file
        with open(self.config_path, 'r') as config_file:
            config_data = yaml.safe_load(config_file)
            self.excel_settings = config_data.get('excel_settings')
            self.database_settings = config_data.get('databases', {})
            self.data_sources = config_data.get('data_sources', {})


    def __str__(self):
        return "\n".join(f"{key}: {value}" for key, value in vars(self).items())

# Example usage
