import yaml
import sys
import os
import argparse

class Config():

    def __init__(self):
        #Sets the file location as root location
        os.chdir(sys.path[0])

    def load_config(self):
        with open("data/config.yaml", 'r') as stream:
            return yaml.safe_load(stream)


    def setup_and_parse_flags(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-env", "--environment",
                            help="Environment to run (dev/prod)")
        return parser.parse_args()
