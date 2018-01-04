from django.conf.urls import url
from snippets import views

urlpatterns = [
    url(r'^snippet/$', views.snippet_list),
    url(r'^snippet/(?P<pk>[0-9]+)/$', views.snippet_detail),
]
