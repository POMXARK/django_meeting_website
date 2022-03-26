from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Person
from .serealizers import PersonSerializer
from .serealizers import OnlyPersonSerializer
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from django_filters import rest_framework as filters


class PersonList(generics.ListAPIView):
    serializer_class = OnlyPersonSerializer
    queryset = Person.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('gender','first_name','last_name')


# Equivalent FilterSet:
class PersonFilter(filters.FilterSet):
    class Meta:
        model = Person
        fields = ('gender','first_name','last_name')

class TestClass(APIView):
    """Вывод"""

    filter_backends = (DjangoFilterBackend,)
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

class ModelPersonFilter(TestClass):
    pass

class Category1Details(APIView):
    #permission_classes = [IsAuthenticated]
    def get(self,request,id):
        sympathy_id = request.GET['id']
        members = Person.objects.filter(user=sympathy_id)
        serializer = OnlyPersonSerializer(members, many=True)
        data = list(serializer.data[0].items())
        is_sympathy = data[-1][-1]
        first_name = data[3][-1]
        last_name = data[4][-1]
        email = data[-2][-1]

        members_ = Person.objects.filter(user=id)
        serializer_ = OnlyPersonSerializer(members_, many=True)
        data_ = list(serializer_.data[0].items())
        first_name_ = data_[3][-1]
        last_name_ = data_[4][-1]
        email_ = data_[-2][-1]


        if id in is_sympathy:
            send_mail(
                'Subject here',
                f'«Вы понравились {first_name} {last_name}! Почта участника: {email}»',
                'from@example.com',
                [email_],
                fail_silently=False,
            )
            send_mail(
                'Subject here',
                f'«Вы понравились {first_name_} {last_name_}! Почта участника: {email_}»',
                'from@example.com',
                [email],
                fail_silently=False,
            )
            return Response({"email": email})
        else:
            return Response(status=404)

    def post(self, request,id):
        serializer = OnlyPersonSerializer(data=request.data)
        if serializer.is_valid():
            try:
                if serializer.data['sympathy']:

                    return Response(serializer.data, status=201)
            except KeyError:
                return Response(serializer.errors, status=404)
        else:
            return Response(serializer.errors, status=404)