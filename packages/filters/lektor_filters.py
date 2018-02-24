import os
import datetime
from lektor.pluginsystem import Plugin


def env_override(value, key):
    return os.getenv(key, value)


class FiltersPlugin(Plugin):
    name = u'filters'
    description = u'A few template filters.'

    def on_setup_env(self, **extra):
        self.env.jinja_env.globals['now'] = datetime.datetime.utcnow
        self.env.jinja_env.filters['strftime'] = datetime.datetime.strftime
        self.env.jinja_env.filters['id'] = id
        self.env.jinja_env.filters['env_override'] = env_override
