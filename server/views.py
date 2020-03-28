from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from server.schema import schema

@csrf_exempt
def index(request):
    result = schema.execute(request.body)
    return HttpResponse(result.data)