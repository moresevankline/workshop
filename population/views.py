from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import CleanedPopulationSerializers, CountrySerializers
from .models import CleanedPopulation


# Create your views here.
class CountriesView(APIView):
    def get(self, request):
        country = CleanedPopulation.objects.all()
        serializer = CleanedPopulationSerializers(country, many=True)
        country = []
        for data in serializer.data:
            country.append(data["country_territory"])
        data = {"countries": country}
        return Response(data)


class CountryView(APIView):
    def get(self, request, country):
        country = CleanedPopulation.objects.all().filter(country_territory=country)
        serializer = CountrySerializers(country, many=True)
        return Response(serializer.data)


class PredictPopulation(APIView):
    def get(self, request, country):
        pass
