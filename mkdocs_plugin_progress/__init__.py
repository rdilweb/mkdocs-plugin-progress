from mkdocs.plugins import BasePlugin


class Progress(BasePlugin):
    pass


def _info(data):
    print("INFO - {}".format(data))
