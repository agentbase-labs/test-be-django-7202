from django.http import JsonResponse
def home(request): return JsonResponse({'message': 'Django Works!'})
def health(request): return JsonResponse({'status': 'ok', 'framework': 'django'})
urlpatterns = []
from django.urls import path
urlpatterns = [path('', home), path('health', health)]