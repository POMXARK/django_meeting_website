from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Person
from .serealizers import PersonSerializer
from .serealizers import OnlyPersonSerializer

class TestClass(APIView):
    """Вывод"""
    def get(self,request):
        members = Person.objects.filter()
        serializer = PersonSerializer(members, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OnlyPersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=404)
