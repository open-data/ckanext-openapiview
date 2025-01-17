from setuptools import setup, find_packages

version = '0.0.1'

setup(
    name='ckanext-openapiview',
    version=version,
    description="View plugin for OpenAPI (swagger) resources",
    long_description="",
    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[],
    keywords='ckan',
    author='Ian Ward',
    author_email='ian@excess.org',
    url='https://github.com/open-data/ckanext-openapiview',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    entry_points="""
    [ckan.plugins]
    openapi_view=ckanext.openapiview.plugin:OpenAPIViewPlugin
    """,
)
