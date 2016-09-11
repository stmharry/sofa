from django.conf.urls import include, url
from documents.views import ElectronicView, PaperView, CreateView, FileView

urlpatterns = [
    url(r'^electronic/', ElectronicView.as_view()),
    url(r'^paper/', PaperView.as_view()),
    url(r'^create/', CreateView.as_view()),
    url(r'^file/', FileView.as_view()),
]
