from django.urls import path

from . import contentviews

urlpatterns = [
    path('what_is_docker', contentviews.WhatIsDockerView.as_view(), name=f'{contentviews.WhatIsDockerView.uid}_view'),
]
