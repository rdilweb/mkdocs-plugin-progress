"""
    Copyright (c) 2020-current year Reece Dunham

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       https://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from mkdocs.plugins import BasePlugin


class Progress(BasePlugin):
    config_scheme = ()

    def on_config(self, *args, **kwargs):
        _info("Loaded configuration.")

    def on_env(self, *args, **kwargs):
        _info("Created templating engine contexts.")
        return kwargs["env"]

    def on_post_build(self):
        _info("Finishing up...")

    def on_template_context(self, *args, **kwargs):
        _info("Contextualized {}.".format(kwargs["template_name"]))
        return kwargs["context"]

    def on_page_read_source(self, *args, **kwargs):
        _info("Processing page \"{}\"...".format(kwargs["page"].file.src_path))
        return None


def _info(data):
    print("INFO    -  {}".format(data))
