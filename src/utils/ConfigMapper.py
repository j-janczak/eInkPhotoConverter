from model.ConfigModel import ConfigModel
import json
import os

HOME_PATH = os.path.expanduser('~')
CONFIG_DIRECTORY = ".eInkImageConverter"
CONFIG_FILENAME = "config.json"
FILE_NAME = f"{HOME_PATH}/{CONFIG_DIRECTORY}/{CONFIG_FILENAME}"

config = ConfigModel()


def __writeToFile() -> None:
    global config
    try:
        with open(FILE_NAME, "w") as file:
            file.write(config.model_dump_json(indent=4))
            print(f"{FILE_NAME} updated")
    except:
        print(f"Error while creating {FILE_NAME}")


def updateConfig(updatedModel: any) -> None:
    global config
    config = config.model_copy(update=updatedModel)
    __writeToFile()


os.makedirs(f"{HOME_PATH}/{CONFIG_DIRECTORY}", exist_ok=True)
if not os.path.isfile(FILE_NAME):
    print("Creating new config")
    __writeToFile()
else:
    print("Reading existing config")
    try:
        with open(FILE_NAME, "r") as file:
            jsonConfig = json.load(file)
            config = ConfigModel(**jsonConfig)
            print("Config loaded")
    except:
        print(f"Error while loading data from {FILE_NAME}")
