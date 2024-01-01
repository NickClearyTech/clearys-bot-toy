from typing import Optional

import yaml
from config.config import Config

config_object: Optional[Config] = None

with open("/config/config.yaml", "r") as f:
    config_yaml = yaml.safe_load(f)
    config_object: Config = Config(**config_yaml)
