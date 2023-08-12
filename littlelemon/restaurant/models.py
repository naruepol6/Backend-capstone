from django.db import models

# Create your models here.
class Booking(models.Model):
  name = models.CharField(max_length=255)
  no_of_guests = models.SmallIntegerField()
  booking_date = models.DateField()

  def __str__(self) -> str: 
    return f'{self.name} for {self.number_of_guests} guests on {self.booking_date}'


# Add code to create Menu model
class Menu(models.Model):
  title = models.CharField(max_length=255) 
  price = models.DecimalField(max_digits=10, decimal_places=2)
  inventory = models.IntegerField()

  def __str__(self) -> str:
    return f'{self.title} : {str(self.price)}'