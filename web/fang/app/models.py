from django.db import models

# Create your models here.

class Province_table(models.Model):
    province_name=models.CharField(max_length=20)
    class Meta:
        db_table="province_table"

class  City_table(models.Model):
    province_table=models.ForeignKey(Province_table,on_delete=models.CASCADE)
    city_name=models.CharField(max_length=100)
    city_url=models.CharField(max_length=500)
    class Meta:
        db_table="city_table"

class TypeOfHouse_table(models.Model):
    city_table=models.ForeignKey(City_table,on_delete=models.CASCADE)
    house_type=models.CharField(max_length=100)
    house_url=models.CharField(max_length=500)
    class Meta:
        db_table="typeofhouse_table"

class Area_table(models.Model):
    typeofhouse_table=models.ForeignKey(TypeOfHouse_table,on_delete=models.CASCADE)
    area_name=models.CharField(max_length=100)
    area_url=models.CharField(max_length=500)
    class Meta:
        db_table="area_table"


class NewHouseInfo_table(models.Model):
    area_table=models.ForeignKey(Area_table, on_delete=models.CASCADE)
    house_image=models.CharField(max_length=500)
    house_detail=models.CharField(max_length=200)
    house_name=models.CharField(max_length=100)
    house_descript=models.CharField(max_length=200)
    house_size=models.CharField(max_length=100)
    house_address=models.CharField(max_length=100)
    house_phone=models.CharField(max_length=500)
    house_price=models.CharField(max_length=50,default='0')
    house_label=models.CharField(max_length=200,default='无')
    class Meta:
        db_table="newhouseinfo_table"
