# encoding: utf-8
import logging

from typing import Any, Dict
from ckan.types import DataDict, Context

from ckan.common import CKANConfig
import ckan.plugins as p


log = logging.getLogger(__name__)


class OpenAPIViewPlugin(p.SingletonPlugin):
    '''This extension previews JSON(P).'''

    p.implements(p.IConfigurer, inherit=True)
    p.implements(p.IConfigurable, inherit=True)
    p.implements(p.IResourceView, inherit=True)

    def update_config(self, config: 'CKANConfig'):
        if not p.toolkit.check_ckan_version('2.9'):
            p.toolkit.add_template_directory(config, '2.8_templates')
        p.toolkit.add_template_directory(config, 'templates')
        p.toolkit.add_resource('assets', 'ckanext-openapiview')

    def info(self) -> Dict[str, Any]:
        return {'name': 'openapi_view',
                'title': p.toolkit._('OpenAPI'),
                'icon': 'file-text-o',
                'default_title': p.toolkit._('OpenAPI')}

    def can_view(self, data_dict: DataDict) -> bool:
        resource = data_dict['resource']
        format_lower = resource.get('format', '').lower()
        return format_lower == 'json'

    def view_template(self, context: Context, data_dict: DataDict) -> str:
        return 'openapiview/openapi_view.html'

    def form_template(self, context: Context, data_dict: DataDict) -> str:
        return 'openapiview/openapi_form.html'
