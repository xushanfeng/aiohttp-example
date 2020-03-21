import os
import pathlib
import yaml

BASE_DIR = pathlib.Path(__file__).parent.parent


def get_config():
    env = os.environ.get('env') if 'env' in os.environ else 'dev'
    config_path = os.path.join(BASE_DIR, 'config', env + '.yml')
    with open(config_path) as f:
        my_config = yaml.load(f)
    return my_config


config = get_config()
