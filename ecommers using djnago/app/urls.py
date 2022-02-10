from django.urls import path
from . import views

app_name='app'

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('review/<id>',views.review,name='review'),
    path('comment/<id>',views.post_review,name='comment'),
]
