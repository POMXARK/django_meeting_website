
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
import haversine as hs





class PersonFilter(filters.FilterSet):
    distance = filters.NumberFilter(method='filter_distance')

    def filter_distance(self, queryset, name, value):
        dict_distance = {}
        end_list = []
        filter_distance = []
        distance = float(self.request.query_params.get('distance'))
        latitude = queryset.values_list('latitude')
        longitude = queryset.values_list('latitude')
        user = self.request.user.pk
        for idx, el in enumerate(queryset):
            if user == el.user_id:
                coord_1 = (latitude[idx][0], longitude[idx][0])
                dict_distance.update({"start_coordinates": {"pk": el.user_id, "coordinates": coord_1}})
            else:
                coord_2 = (latitude[idx][0], longitude[idx][0])
                end_list.append({"pk": el.user_id, "coordinates": coord_2})
                dict_distance.update({"end_coordinates": end_list})
        for idx, el in enumerate(dict_distance['end_coordinates']):
            coord_1 = dict_distance['start_coordinates']['coordinates']
            coord_2 = el['coordinates']
            x = hs.haversine(coord_1, coord_2)
            if x < distance and user != el["pk"]:
                filter_distance.append(el["pk"])
        return queryset.filter(pk__in=filter_distance)

    class Meta:
        model = Person
        fields = ('gender', 'first_name', 'last_name', 'distance')


class PersonList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OnlyPersonSerializer
    queryset = Person.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = PersonFilter


class Members(APIView):
    """Вывод"""

    filter_backends = (DjangoFilterBackend,)

    def get(self, request):
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


class SympathyCheck(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        # sympathy_id = request.GET['id']
        print(f'id {id}')
        members = Person.objects.filter(user_id=id)
        serializer = OnlyPersonSerializer(members, many=True)
        qs = serializer.data[0]
        print(qs['user'])
        members_ = Person.objects.filter(user_id__in=qs['sympathy'])
        serializer_ = OnlyPersonSerializer(members_, many=True)
        qs_ = serializer_.data[0]
        print(qs_['sympathy'])
        if id in qs_['sympathy']:
            send_mail(
                'Subject here',
                f'«Вы понравились {qs["first_name"]} {qs["last_name"]}! Почта участника: {qs["email"]}»',
                'from@example.com',
                [qs_["email"]],
                fail_silently=False,
            )
            send_mail(
                'Subject here',
                f'«Вы понравились {qs_["first_name"]} {qs_["last_name"]}! Почта участника: {qs_["email"]}»',
                'from@example.com',
                [qs["email"]],
                fail_silently=False,
            )
            return Response({"email": qs["email"]})
        else:
            return Response(status=404)

    def post(self, request, id):
        serializer = OnlyPersonSerializer(data=request.data)
        if serializer.is_valid():
            try:
                if serializer.data['sympathy']:
                    return Response(serializer.data, status=201)
            except KeyError:
                return Response(serializer.errors, status=404)
        else:
            return Response(serializer.errors, status=404)
