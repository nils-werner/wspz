from setuptools import setup

setup(
    name='lektor-filters',
    version='0.1',
    author=u'Nils Werner',
    author_email='nils.werner@gmail.com',
    license='MIT',
    py_modules=['lektor_filters'],
    entry_points={
        'lektor.plugins': [
            'filters = lektor_filters:FiltersPlugin',
        ]
    }
)
