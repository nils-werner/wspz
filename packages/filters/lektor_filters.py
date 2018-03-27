import os
import pytz
import datetime
import functools
from lektor.pluginsystem import Plugin


def env_override(value, key):
    return os.getenv(key, value)


class FiltersPlugin(Plugin):
    name = u'filters'
    description = u'A few template filters.'

    def on_setup_env(self, **extra):
        tz = pytz.timezone('Europe/Berlin')
        self.env.jinja_env.globals['now'] = functools.partial(datetime.datetime.now, tz)
        self.env.jinja_env.globals['is_production'] = lambda: os.getenv('CONTEXT') is not None
        self.env.jinja_env.filters['strftime'] = datetime.datetime.strftime
        self.env.jinja_env.filters['id'] = id
        self.env.jinja_env.filters['env_override'] = env_override
