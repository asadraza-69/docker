from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('media', MediaViewSet, basename = 'media')


urlpatterns = [
    path("", include(router.urls)),
    # path('/media', MediaViewSet.as_view(), name='job_post'),

]