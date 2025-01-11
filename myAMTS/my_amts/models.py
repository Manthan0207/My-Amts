from django.db import models

# Create your models here.
class Bus(models.Model):
    bus_number = models.CharField(max_length=10, unique=True)
    
    stops = models.JSONField()

    def __str__(self):
        return self.bus_number
    
# import json
# import os
# import django

# # Set up Django environment
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rolex.settings')
# django.setup()

# from my_amts.models import Bus

# def load_bus_data():
#     # Load the JSON file
#     with open('.\insert_bus_data.json', 'r') as file:
#         bus_data = json.load(file)

#     for bus in bus_data:
#         # Create or update Bus entry
#         Bus.objects.update_or_create(
#             bus_number=bus['bus_number'],
#             defaults={'stops': bus['stops']}
#         )
#     print("Bus data inserted successfully!")

# if __name__ == "__main__":
#     load_bus_data()