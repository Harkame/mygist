from yaml import Loader, load, dump
from random import seed, randint


def get_config(config_file_path):
    config_file = open(config_file_path, "r")

    config = load(config_file, Loader=Loader)

    config_file.close()

    return config


if __name__ == "__main__":
    config = get_config("./update.yml")

    for game in config["games"]:
        version = str(game["version"])

        new_version = str(randint(0, 3)) + "." + str(randint(0, 30))

        if version != new_version:
            print("update")
            print("download...")
            game["version"] = new_version
            print(game["version"])

            stream = open("./update.yml", "w")
            dump(config, stream)
            print(dump(config))
