import yaml
import os

directory = os.path.dirname(os.path.realpath(__file__))

DEFAULT_CONFIG_FILE_PATH = os.path.join(directory, '../config.yaml')

def load_config(file_path=DEFAULT_CONFIG_FILE_PATH):
    config = {}
    with open(file_path, "r") as conf_file:
        try:
            config = yaml.safe_load(conf_file)
        except yaml.YAMLError as exc:
            print(exc)

    return config

def write_config(conf: dict, file_path=DEFAULT_CONFIG_FILE_PATH):
    with open(file_path, 'w') as file:
        yaml.dump(conf, file)

config_template = {
    'raspi_ip': None,
    'raspi_port': None,
    'unity_ip': None,
    'unity_port': None
}
