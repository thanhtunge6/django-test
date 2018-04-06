from django.http import HttpResponse
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_503_SERVICE_UNAVAILABLE)

class MyView(APIView):
    def _check_post_data_format(self, data):
        schema = {
            'type': 'object',
            'properties': {
                'description': {'type': 'string'}
            },
            'required': [
                'description'
            ],
        }

        try:
            validate(data, schema)
        except ValidationError as validation_error:
            return validation_error

    def post(self, request):
        err = self._check_post_data_format(request.data)
        if err:
            return Response(str(err), status=HTTP_400_BAD_REQUEST)
        try:
            response = {'Output': request.data["description"]}
        except TypeError:
            return Response("Models not ready yet", status=HTTP_503_SERVICE_UNAVAILABLE)
        return Response(response)

    def get(self, request):
        return HttpResponse("Hello, World!")