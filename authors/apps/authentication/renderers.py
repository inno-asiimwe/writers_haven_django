import json

from rest_framework.renderers import JSONRenderer


class UserJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        # If the view throws an error (such as the user can't be authenticated
        # or something similar), `data` will contain an `errors` key. We want
        # the default JSONRenderer to handle rendering errors, so we need to
        # check for this case.

        token = data.get('token', None)
        errors = data.get('errors', None)

        if token and isinstance(token, bytes):
            data['token'] = data.decode(self.charset)

        if errors is not None:
            # As mentioned about, we will let the default JSONRenderer handle
            # rendering errors.
            return super(UserJSONRenderer, self).render(data)


        # Finally, we can render our data under the "user" namespace.
        return json.dumps({
            'user': data
        })
