import yaml

class Settings:
    _instance = None

    def __new__(cls, config_path):
        if cls._instance is None:
            cls._instance = super(Settings, cls).__new__(cls)
            cls._instance.config_path = config_path
            cls._instance.settings = {}
            cls._instance._read_config()
        return cls._instance

    def _read_config(self):
        with open(self.config_path, 'r') as config_file:
            config_data = yaml.safe_load(config_file)
            self.settings = config_data.get('settings', {})

    def get_settings(self):
        return vars(self)

    def print_parameter(self, parameter_name):
        print(f"{parameter_name.capitalize()} Settings:")
        parameter_value = getattr(self, parameter_name, {})
        self._print_nested_parameters(parameter_value)

    def _print_nested_parameters(self, parameters, indent=1):
        for key, value in parameters.items():
            if isinstance(value, dict):
                print(f"{' ' * indent * 2}{key}:")
                self._print_nested_parameters(value, indent + 1)
            else:
                print(f"{' ' * indent * 2}{key}: {value}")



# Example usage
if __name__ == "__main__":
    config_file_path = "config/config.yml"
    settings = Settings(config_file_path)

    # Accessing and printing each set of parameters
    settings.print_parameter('excel_settings')
    print("\n")  # Add a newline for separation
    settings.print_parameter('database_settings')
    print("\n")  # Add a newline for separation
    settings.print_parameter('data_sources')
    print("\n")  # Add a newline for separation
    settings.print_parameter('nonexistent_settings')