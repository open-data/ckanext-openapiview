ckanext-openapiview
===================

Overview
========
A CKAN extension to add [Swagger 3](https://swagger.io/specification/) views to JSON resources.

By creating a resource and uploading a Swagger JSON file to it, you will be allowed to create an "Open API" view, which will display the generated Swagger documentaion generated from the uploaded JSON file.

Installation
============

To install ``ckanext-openapiview``:

1. Install CKAN >=2.8.

1. Activate your CKAN virtual environment, eg:

    ```
    . /usr/lib/ckan/default/bin/activate
    ```

1. Install the extension into your virtual environment:

    ```
    pip install -e 'git+https://github.com/open-data/ckanext-openapiview.git#egg=ckanext-openapiview'
    ```

1. Add ``openapi_view`` to the ``ckan.plugins`` setting in
your CKAN config file (by default the config file is located at
``/etc/ckan/default/production.ini``).

1. Restart CKAN. Eg if you've deployed CKAN with Apache on Ubuntu:

    ```
    sudo service apache2 reload
    ```
