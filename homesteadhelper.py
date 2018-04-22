import yaml
import sys
import os
from config import Config

class HomesteadHelper:

    def __init__(self, config_file):
        self.config = Config(config_file)


    def initialize_project(self, project_name):
        self.project_name = project_name
        self.project_folder = self.config.projects_folder + self.project_name + "\public"
        self.project_remote_folder = self.config.remote_projects_folder + self.project_name + "/public"

        self.create_project_folder()
        self.create_yaml_entries()
        self.create_hosts_entries()

    def create_project_folder(self):
        if not os.path.exists(self.project_folder):
            os.makedirs(self.project_folder)
            print(f"Created folder {self.project_folder}")

    def create_yaml_entries(self):

        try:
            file = open(self.config.homestead_yaml, 'r')
        except:
            print("Could not open file %s" % self.config.homestead_yaml)
            sys.exit(5)

        data = yaml.load(file)
        data['sites'].append(
            {
                'map': f'{self.project_name}.{self.config.domain}',
                'to': self.project_remote_folder
            }
        )
        file.close()

        with open(self.config.homestead_yaml, 'w') as file:
            yaml.dump(data, file, default_flow_style=False)
            print(f"{self.config.homestead_yaml} - wrote: 'map: {self.project_name}.{self.config.domain} to: {self.project_remote_folder}'")


    def create_hosts_entries(self):
        try:
            file = open(self.config.hosts_file, "a")
        except:
            print(f"Could not open hosts file at {self.config.hosts_file}. Check the file path and make sure you are executing the script with admin premissions")
            sys.exit(7)

        file.write(f"{self.config.address} {self.project_name}.{self.config.domain}")
        print(f"{self.config.hosts_file} - wrote : '{self.config.address} {self.project_name}.{self.config.domain}'")
        file.close()






if len(sys.argv) < 2:
    print("Missing argument - project_name. Usage: homesteadhelper project_name ")
    sys.exit(1)


homestead_helper = HomesteadHelper("config.txt")
homestead_helper.initialize_project(sys.argv[1])


