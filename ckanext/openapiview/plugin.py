# encoding: utf-8

import logging
from typing import Any

from ckan.common import CKANConfig, json
import ckan.plugins as p
import ckanext.resourceproxy.plugin as proxy
import ckan.lib.datapreview as datapreview

log = logging.getLogger(__name__)


class OpenAPIViewPlugin(p.SingletonPlugin):
    '''This extension previews JSON(P).'''

    p.implements(p.IConfigurer, inherit=True)
    p.implements(p.IConfigurable, inherit=True)
    p.implements(p.IResourceView, inherit=True)


    def update_config(self, config):
        if not p.toolkit.check_ckan_version('2.9'):
            p.toolkit.add_template_directory(config, '2.8_templates')
        p.toolkit.add_template_directory(config, 'templates')
        p.toolkit.add_resource('assets', 'ckanext-openapiview')

    def info(self):
        return {'name': 'openapi_view',
                'title': p.toolkit._('OpenAPI'),
                'icon': 'file-text-o',
                'default_title': p.toolkit._('OpenAPI'),
                }

    def can_view(self, data_dict):
        resource = data_dict['resource']
        format_lower = resource.get('format', '').lower()
        return format_lower == 'json'

    def view_template(self, context, data_dict):
        return 'openapiview/openapi_view.html'

    def form_template(self, context, data_dict):
        return 'openapiview/openapi_form.html'
