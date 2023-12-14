from model.ConfigModel import ConfigModel
from dataclasses import asdict
import json
import os

HOME_PATH = os.path.expanduser('~')
CONFIG_DIRECTORY = ".eInkImageConverter"
CONFIG_FILENAME = "config.json"
FILE_NAME = f"{HOME_PATH}/{CONFIG_DIRECTORY}/{CONFIG_FILENAME}"


class ConfigMapper:
    def __init__(self) -> None:
        os.makedirs(f"{HOME_PATH}/{CONFIG_DIRECTORY}", exist_ok=True)

        self.config = ConfigModel()
        if not os.path.isfile(FILE_NAME):
            print("Creating new config")
            self.__writeToFile()
        else:
            print("Reading existing config")
            try:
                with open(FILE_NAME, "r") as file:
                    jsonConfig = json.load(file)
                    self.config = ConfigModel(**jsonConfig)
                    print("Config loaded")
            except:
                print(f"Error while loading data from {FILE_NAME}")

    def update(self, updatedModel: any) -> None:
        self.config = self.config.model_copy(update=updatedModel)
        self.__writeToFile()

    def __writeToFile(self) -> None:
        try:
            with open(FILE_NAME, "w") as file:
                file.write(self.config.model_dump_json(indent=4))
                print(f"{FILE_NAME} updated")
        except:
            print(f"Error while creating {FILE_NAME}")
