from django.conf.urls import url
from views import SearchView, RangeSearchView, ImpSearchView, SentimentSearchView

urlpatterns = [
    url(r'^search/', SearchView.as_view()),
    url(r'^rangeSearch/', RangeSearchView.as_view()),
    url(r'^impSearch/', ImpSearchView.as_view()),
    url(r'^sentiSearch/', SentimentSearchView.as_view())
]