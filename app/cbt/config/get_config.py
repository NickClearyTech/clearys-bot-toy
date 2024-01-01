import yaml
from config.config import Config

def get_config():
    with open('/config.yaml', 'r') as f:
        config_yaml = yaml.safe_load(f)
        config_object: Config = Config(**config_yaml)

