from django.conf.urls import url

from . import views

app_name = 'downloader'
urlpatterns =[
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^exportcsv/$', views.ExportCsvView.as_view(), name='exportcsv'),
]
