from django.shortcuts import render

# Create your views here.
from django.db import models
from django.http import HttpResponse
from django.views import generic
from django.views.generic import View
from uploader.models import TrafficData, DeviceData

import csv

class IndexView(generic.ListView):
    template_name = 'downloader/index.html'
    context_object_name = 'device'

    def get_queryset(self):
        """GPS COORD."""
        return DeviceData.objects.all()


class Echo(object):
    """An object that implements just the write method of the file-like interface.
    """

    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value


class ExportCsvView(View):
    def get(self, request, *args, **kwargs):
        traffic = TrafficData.objects.all()  # Assume 50,000 objects inside

        response = HttpResponse(content_type="text/csv")
        response['Content-Disposition'] = 'attachment; filename="traffic.csv"'

        model = traffic.model
        model_fields = model._meta.fields + model._meta.many_to_many
        headers = [field.name for field in model_fields]  # Create CSV headers

        def get_row(obj):
            rows = []
            for field in model_fields:
                if type(field) == models.ForeignKey:
                    val = getattr(obj, field.name)
                    if val:
                        val = val.__unicode__()
                elif type(field) == models.ManyToManyField:
                    val = u', '.join([item.__unicode__() for item in getattr(obj, field.name).all()])
                else:
                    val = getattr(obj, field.name)
                rows.append(unicode(val).encode("utf-8"))
            return rows

        def stream(headers, data):  # Helper function to inject headers
            if headers:
                yield headers
            for obj in data:
                yield get_row(obj)
        # streaming http?
        # pseudo_buffer = Echo()
        writer = csv.writer(response)
        for row in stream(headers, traffic):
            writer.writerow(row)

        return response
