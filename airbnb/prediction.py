from airbnb.models import countries


def predict():
    print("In prediction")
    countriesList = countries.objects.all()
    print(countriesList)
