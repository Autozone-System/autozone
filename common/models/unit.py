from django.db import models

class Make(models.Model):
    db_table = 'makes'
    
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    
    
    models = models.ManyToOneRel('common.Model', related_name='make', to='common.Model', field_name='make')
    
    
class Model(models.Model):
  
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    make = models.ForeignKey('common.Make', on_delete=models.CASCADE)
    
    units = models.ManyToOneRel('common.Unit', related_name='model', to='common.Unit', field_name='model')
    
    
    def __str__(self) -> str:
        return f"{self.make.name} {self.name}"
         

class Unit(models.Model):
  
  BODY_TYPES = (
    ('sedan', 'Sedan'),
    ('hatchback', 'Hatchback'),
    ('suv', 'SUV'),
    ('truck', 'Truck'),
    ('coupe', 'Coupe'),
    ('wagon', 'Wagon'),
    ('van', 'Van'),
  )
  
  
  TRANSMISSION = (
    ('manual', 'Manual'),
    ('automatic', 'Automatic'),
    ('cvt', 'CVT'),
    ('dsg', 'DSG'),
    ('smg', 'SMG')
  )
  
  
  FUEL = (
    ('petrol', 'Petrol'),
    ('diesel', 'Diesel'),
    ('ev', 'EV'),
    ('hybrid', 'Hybrid')
  )
  
  
  YEAR = (
    (2010, 2010),
    (2011, 2011),
    (2012, 2012),
    (2013, 2013),
    (2014, 2014),
    (2015, 2015),
    (2016, 2016),
    (2017, 2017),
    (2018, 2018),
    (2019, 2019),
    (2020, 2020),
    (2021, 2021),
    (2022, 2022),
    (2023, 2023),
    (2024, 2024),
    (2025, 2025),
    (2026, 2026),
    (2027, 2027),
    (2028, 2028),
    (2029, 2029),
    (2030, 2030)
  )
  
  
  # Model Attributes
  
  id = models.AutoField(primary_key=True)
  year = models.IntegerField(choices=YEAR)
  model = models.ForeignKey('common.Model', on_delete=models.SET_NULL, null=True)
  price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
  chassis = models.CharField(max_length=50, unique=True)
  engine = models.CharField(max_length=50)
  slug = models.SlugField(max_length=50, unique=True)
  body = models.CharField(max_length=50, choices=BODY_TYPES)
  model_code = models.CharField(max_length=50, null=True)
  color = models.CharField(max_length=50)
  fuel = models.CharField(max_length=50, choices=FUEL, null=True)
  seats = models.IntegerField(null=True)
  doors = models.IntegerField(null=True)
  drive = models.CharField(max_length=50, null=True)
  mileage = models.IntegerField(null=True)
  transmission = models.CharField(max_length=50, choices=TRANSMISSION, null=True)
  
  
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  

  # Relationships
  tags = models.ManyToManyField('common.Tag')
  
  
  