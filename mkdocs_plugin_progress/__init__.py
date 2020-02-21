from mkdocs.plugins import BasePlugin


class Progress(BasePlugin):
    config_scheme = ()

    def on_config(self, config):
        _info("Loaded configuration.")

    def on_pre_build(self, config):
        _info("Starting build...")

    def on_env(self, env, config, site_navigation):
        _info("Created templating engine contexts.")
        return env

    def on_post_build(self):
        _info("Finishing up...")

    def on_template_context(self, context, template_name, config):
        _info("Contextualized {}.".format(template_name))
        return context
    
    def on_pre_page(self, page, config, site_navigation):
        _info("Processing page \"{}\"...".format(page.name))
        return page


def _info(data):
    print("INFO - {}".format(data))
