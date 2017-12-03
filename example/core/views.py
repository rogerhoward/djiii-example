
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.views.generic import View, TemplateView, DetailView, ListView

from .models import Asset


# --------------------------------------------------
# Core.Asset
# --------------------------------------------------

class AssetListView(ListView):
    model = Asset

class AssetDetailView(DetailView):
    queryset = Asset.objects.all()
