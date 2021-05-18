from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Snippet
from .serializers import SnippetSerializer
from .couch import finalobject
from rest_framework.views import APIView

from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics
# Create your views here.
# --------------class based views----------------------

class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        # return Response(serializer.data)
        return Response(finalobject)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
# --------------------------Function based views----------------


# # @api_view
# # making sure you recieve request instances in your view
# # add context to Response object
# # handles the responses and exceptions
# @api_view(['GET', 'POST'])
# def snippet_list(request, format=None):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         # Get all data from database
#         snippets = Snippet.objects.all()
#         # serialize the database data
#         serializer = SnippetSerializer(snippets, many=True) 
#         # send response data to rest using REsponse    
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         # get data passed through POST reqest
#         # ano need to parse data because we are using wrapper api_view
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             # after savng return response with status code
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         # get a single object(document) from database which match the id in url as pk
#         snippet = Snippet.objects.get(pk=pk)

#     except Snippet.DoesNotExist:
#         # if document not found return not found response
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         # In put request we get id of snippet and data that replaced with snippet
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




# ------------------------------------------------------------------------------------------------



# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from .models import Snippet
# from .serializers import SnippetSerializer
# # Create your views here.

# @csrf_exempt
# def snippet_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         # get all data stored in database
#         snippets = Snippet.objects.all()
#         # then serialize the data
#         serializer = SnippetSerializer(snippets, many=True)
#         # return the Json response
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         # get the data pass throuugh a POST request convert it to ditionary
#         data = JSONParser().parse(request)
#         # Serialize the data
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             # if it is valid save it to database
#             serializer.save()
#             # return response
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# # To get Single object from database as response
# @csrf_exempt
# def snippet_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)