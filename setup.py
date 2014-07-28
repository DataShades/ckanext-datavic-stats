from setuptools import setup, find_packages

version = '0.1'

setup(
	name='ckanext-datavic-stats',
	version=version,
	description='Extension for customising CKAN Statistics for data.gov.au',
	long_description='',
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Alex Sadleir',
	author_email='alex.sadleir@linkdigital.com.au',
	url='',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.datavic_stats'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[],
	entry_points=\
	"""
        [ckan.plugins]
        datavic_stats=ckanext.datavic_stats.plugin:StatsPlugin
	""",
)
