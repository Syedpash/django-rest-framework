from django.urls import path
from .views import SnippetDetail, SnippetList, UserList, UserDetail
# from .views import snippet_detail, snippet_list
from rest_framework.urlpatterns import format_suffix_patterns
from .couch import get_result
urlpatterns = [
    path('snippets/', SnippetList.as_view()),
    path('snippets/<int:pk>/', SnippetDetail.as_view()),
    path('couchdata/', get_result),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]

# by using format_suffix_patterns you can use the links as .api or .json
# example:  http://127.0.0.1:8000/snippets.api
urlpatterns = format_suffix_patterns(urlpatterns)