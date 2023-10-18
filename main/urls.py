from django.urls import path, include
from .views import check_formula_view, RequestLogList


urlpatterns = [
    path('math-formula/', check_formula_view),
    path('get_request_log/', RequestLogList.as_view())

]