from django.test import TestCase
from models import Round
# Create your tests here.


# Create a new record using the model's constructor.
# record = Round(num_players=6, non_exclusions="1,2")
# record = Round(id=0)
records = Round.objects.all()

for r in records:
    print(r.id)
    print(r.num_players)

# Save the object into the database.
# record.save()


# Access model field values using Python attributes.
# print(record.id) # should return 1 for the first record.
# print(record.my_field_name) # should print 'Instance #1'

# Change record by modifying the fields, then calling save().
# record.my_field_name = "New Instance Name"
# record.save()




# https://www.geeksforgeeks.org/textfield-django-models/?ref=lbp
# importing the model
# from geeks app
from geeks.models import GeeksModel

# creating a instance of 
# GeeksModel
geek_object = GeeksModel.objects.create(geeks_field ="GfG is the best")
geek_object.save()