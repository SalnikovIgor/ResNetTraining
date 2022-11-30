import json
import PIL
from pathlib import Path


class Utils:
    @staticmethod
    def import_json(path: str):
        with open(Path(path)) as file:
            json_file = file.read()
        return json.loads(json_file)

    @staticmethod
    def import_image(path: str):
        return PIL.Image.open(Path(path))
