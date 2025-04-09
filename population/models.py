# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class RawPopulation(models.Model):
    rank = models.BigIntegerField(blank=True, null=True)
    cca3 = models.TextField(blank=True, null=True)
    country_territory = models.TextField(
        db_column="country/territory", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    capital = models.TextField(blank=True, null=True)
    continent = models.TextField(blank=True, null=True)
    number_2022_population = models.BigIntegerField(
        db_column="2022_population", blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_2020_population = models.BigIntegerField(
        db_column="2020_population", blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_2015_population = models.BigIntegerField(
        db_column="2015_population", blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_2010_population = models.BigIntegerField(
        db_column="2010_population", blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_2000_population = models.BigIntegerField(
        db_column="2000_population", blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_1990_population = models.BigIntegerField(
        db_column="1990_population", blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_1980_population = models.BigIntegerField(
        db_column="1980_population", blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_1970_population = models.BigIntegerField(
        db_column="1970_population", blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    area_km_squared = models.BigIntegerField(blank=True, null=True)
    density_per_km_squared = models.FloatField(blank=True, null=True)
    growth_rate = models.FloatField(blank=True, null=True)
    world_population_percentage = models.FloatField(blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = "raw_population"


class CleanedPopulation(models.Model):
    rank = models.BigIntegerField(blank=True, null=True)
    cca3 = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    capital = models.TextField(blank=True, null=True)
    continent = models.TextField(blank=True, null=True)
    number_2022_population = models.BigIntegerField(
        db_column="2022_population", blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_2020_population = models.BigIntegerField(
        db_column="2020_population", blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_2015_population = models.BigIntegerField(
        db_column="2015_population", blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_2010_population = models.BigIntegerField(
        db_column="2010_population", blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_2000_population = models.BigIntegerField(
        db_column="2000_population", blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_1990_population = models.BigIntegerField(
        db_column="1990_population", blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_1980_population = models.BigIntegerField(
        db_column="1980_population", blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    number_1970_population = models.BigIntegerField(
        db_column="1970_population", blank=True, null=True
    )  # Field renamed because it wasn't a valid Python identifier.
    area_km_squared = models.BigIntegerField(blank=True, null=True)
    density_per_km_squared = models.FloatField(blank=True, null=True)
    growth_rate = models.FloatField(blank=True, null=True)
    world_population_percentage = models.FloatField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = "cleaned_population"
