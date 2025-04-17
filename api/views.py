from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class AllViews(APIView):

    def get(self, request):

        return Response('All Thins Are Fine', status=status.HTTP_200_OK)