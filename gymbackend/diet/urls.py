from django.urls import path
from .views import DietEntryView, DietListView

urlpatterns = [
    path("diet/", DietEntryView.as_view(), name="enter_diet_details"),
    path("diet_list/", DietListView.as_view(), name="search_diet_by_date"),
]
 