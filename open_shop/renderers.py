from rest_framework.renderers import JSONRenderer


class DataWrapperJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        # response = value_if_true IF condition ELSE value_if_false
        response = renderer_context.get(
            "response") if renderer_context else None

        if response and response.status_code >= 400:
            return super().render(data, accepted_media_type, renderer_context)

        return super().render({"products": data}, accepted_media_type,
                              renderer_context)
