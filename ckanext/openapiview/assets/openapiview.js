ckan.module('openapi_view', function (jQuery) {
  return {
    options: {
      parameters: {
        json: {
          contentType: 'application/json',
          dataType: 'json',
          dataConverter: function (data) { return JSON.stringify(data, null, 2); },
          language: 'json'
        }
      }
    },
    initialize: function () {
      const ui = SwaggerUIBundle({
          url: resource_url,
          dom_id: '#swagger-ui',
          deepLinking: true,
          presets: [
              SwaggerUIBundle.presets.apis,
              SwaggerUIBundle.SwaggerUIStandalonePreset
          ],
          plugins: [
              SwaggerUIBundle.plugins.DownloadUrl
          ],
      })
      window.ui = ui
    }
  };
});
