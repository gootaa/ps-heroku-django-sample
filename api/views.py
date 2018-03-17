import coreapi

from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView

class RiverViewSet(APIView):
    """
    API endpoint that shows river data.
    """
    renderer_classes = (JSONRenderer, )

    def get(self, request, format=None):
        return JsonResponse(coreapi.Client().get('http://riverbrain.com/api/v1/rivers'), safe=False)

def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        print("returning FORWARDED_FOR")
        ip = x_forwarded_for.split(',')[-1].strip()
    elif request.META.get('HTTP_X_REAL_IP'):
        print("returning REAL_IP")
        ip = request.META.get('HTTP_X_REAL_IP')
    else:
        print("returning REMOTE_ADDR")
        ip = request.META.get('REMOTE_ADDR')
    print(ip)
    return HttpResponse(str(ip))
