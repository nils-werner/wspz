from lektor.pluginsystem import Plugin


class FiltersPlugin(Plugin):
    name = u'filters'
    description = u'A few template filters.'

    def on_setup_env(self, **extra):
        self.env.jinja_env.filters['id'] = id
