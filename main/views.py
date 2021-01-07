from django.core.exceptions import ValidationError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from .models import Recruit
from .serializers import BulkUpdateListSerializer, RecruitSerializer, RecruiterSerializer
from rest_framework.parsers import JSONParser
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

class RecruitList(APIView):
    """Lists all recruits"""
    #authentication_classes = []
    #permission_classes = []
    #authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = RecruitSerializer


    def get(self,request):
        recruit = Recruit.objects.all().order_by('order_id')
        recruit_serializer = RecruitSerializer(recruit, many=True)
        return Response(recruit_serializer.data)



class RecruitDetail(APIView):
    serializer_class = RecruiterSerializer
    permission_classes = ()

    def get_object(self, pk):
        try:
            return Recruit.objects.get(pk=pk)
        except Recruit.DoesNotExist:
            raise Http404


    def get(self,request, pk):
        recruit = self.get_object(pk)
        serializer = RecruiterSerializer(recruit)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        recruit = self.get_object(pk)
        serializer = RecruiterSerializer(recruit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class NewRecruit(APIView):
    serializer_class = RecruiterSerializer
    permission_classes = ()
    authentication_classes = []

    def post(self, request):
        serializer = RecruiterSerializer(data=request.data)
        if serializer.is_valid():
            next_count = Recruit.objects.count()+1
            #serializer.object.order_id = next_count
            serializer.save(order_id=next_count)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecruitListUpdate(generics.UpdateAPIView):
    """
    # Update Recruit list
    """
    authentication_classes = []
    permission_classes = []

    serializer_class = RecruitSerializer


    def get_queryset(self, ids=None):
        if ids:
            return Recruit.objects.filter( id__in=ids,
            )

        return Recruit.objects.filter(id=None)



    def update(self, request, *args, **kwargs):
        ids = validate_ids(request.data)
        instances = self.get_queryset(ids=ids)
        serializer = RecruitSerializer(
            instances, data=request.data, partial=False, many=True
        )
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)

        return Response(serializer.data, status=status.HTTP_200_OK)



def validate_ids(data, field="id", unique=True):
    if isinstance(data, list):
        id_list = [int(x[field]) for x in data]

        if unique and len(id_list) != len(set(id_list)):
            raise ValidationError("Multiple updates to a single {} found".format(field))

        return id_list

    return [data]