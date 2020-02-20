from mkdocs.plugins import BasePlugin


class Progress(BasePlugin):
    config_scheme = ()


def _info(data):
    print("INFO - {}".format(data))
