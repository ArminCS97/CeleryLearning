from django.urls import path
from .views import EmailCreatorViewSet
urlpatterns = [
    path('' , EmailCreatorViewSet.as_view)
]