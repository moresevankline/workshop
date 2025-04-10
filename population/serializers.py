from rest_framework.serializers import ModelSerializer
from .models import CleanedPopulation


class CleanedPopulationSerializers(ModelSerializer):
    class Meta:
        model = CleanedPopulation
        fields = ["country_territory"]


class CountrySerializers(ModelSerializer):
    class Meta:
        model = CleanedPopulation
        fields = [
            "country_territory",
            "number_2020_population",
            "growth_rate",
            "number_2010_population",
        ]
