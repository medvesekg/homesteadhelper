import sys

class Config:

    required_config = [
        "hosts_file",
        "projects_folder",
        "remote_projects_folder",
        "address",
        "domain",
        "homestead_yaml",
    ]

    def __init__(self, config_file):
        self.config_file = config_file
        self.load_config()

    def load_config(self):

        try:
            file = open(self.config_file, "r")
        except:
            print("Could not open file %s" % self.config_file)
            sys.exit(5)

        config = self.parse_config_file(file)

        if self.validate_config(config):
            for item in config:
                setattr(self, item.lower(), config[item])
            self.add_trailing_slashes()



    def parse_config_file(self, file):
        lines = file.readlines()
        lines = [line for line in lines if line and line != "\n"]
        lines = [line.split("=") for line in lines]
        try:
            config = {line[0].strip(): line[1].strip() for line in lines}
        except:
            print("Config file improperly formated.")
            sys.exit(3)
        return config


    def validate_config(self, config):
        for item in self.required_config:
            if(item not in [key.lower() for key in config]):
                print("%s field is missing from config file" % item.upper())
                sys.exit(1)
        return True


    def add_trailing_slashes(self):
        if(not self.projects_folder.endswith("\\")):
            self.projects_folder += "\\"
        if(not self.remote_projects_folder.endswith("/")):
            self.remote_projects_folder += "/"
