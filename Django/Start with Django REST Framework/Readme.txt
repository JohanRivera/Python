Initially, is neccessary create the virtual environment of python. It created with the objective of 
isolating resources such as libraries and execution environments from the main system or from other 
virtual environments.
    Searching the page: https://medium.com/@m.monroyc22/configurar-entorno-virtual-python-a860e820aace

Active the environment with the comand: source nombre_entorno_virtual/bin/activate

Install DJango: pip install Django

Create the project Django: django-admin.py startproject name_project

Move into the project created: cd name_project (2)

Write the command: python manage.py startapp name_app(1)

Now, to create a database you must write the command: python manage.py migrate

And is neccessary create a superuser to this database, write the command: python manage-py createuser
To project Antares the user is: innovacion, pass: smartboxtsg, email:innovacion@tsg.net.co

Is neccessary create the table to database in models.py but in the folder name_app(1)
example: class Sensors(models.Model):
            temperature = models.CharField(max_length=50)
            humedity = models.CharField(max_length=50)
            front_door = models.CharField(max_length=50)
            back_door = models.CharField(max_length=50)
            enclosure_door = models.CharField(max_length=50)
            panic_button = models.CharField(max_length=50)
            smoke_sensor = models.CharField(max_length=50)

And write the command: python manage.py makemigrations but in the folder name_project(2)
                       python manage.py migrate in the same folder
To end the creating of the table in the file admin.py in the folder (1), you must import the model create and
register it, write the command in the file: from .models import model_create
                                            admin.site.register(model_create)

write the commands: pip install djangorestframework
                    pip install django-cors-headers

In the file settings on INSTALLED_APPS, we must add:
    name_app(1)
    rest_framework
    corsheaders

We must create a file named serializers.py on the folder of the name_app(1) and adding this:
                from rest_framework import serializers
                from .models import model_create

                class model_createSerializer(serializers.ModelSerializer):
                    class Meta:
                        model = model_create #Model to serializer
                        fields = '__all__' #Specific that all the attributes of model must be serializers

We must edit the dile views in the folder name_project(2):
        from rest_framework import viewsets
        from .models import sensor
        from .serializers import sensorSerializer
        # Create your views here.

        class sensorViewSet(viewsets.ModelViewSet):
            serializer_class = sensorSerializer #We spectific the class serializer
            queryset = sensor.objects.all() #Bring all items of the model
    


We must edit the file urls.py in the folder name_project(2):

            from rest_framework.routers import DefaultRouter
            from data.views import sensorViewSet

            router = DefaultRouter()
            router.register(r'name_app(1)',sensorViewSet)

            urlpatterns = router.urls
            
            urlpatterns += [
                ....
            ]


And to Initially the server Django, you must:
    -Add the Gateway of the connection with the raspberry x.x.x.1 in the file settings.py ALLOWED_HOSTS['GATEWAY','LOCALHOST','127.0.0.1']
    -write the command: ./magane.py runserver 0.0.0.0:8000
If you want changed the port of server is with the command:  ./magane.py runserver 0.0.0.0:'otherport'


And to open the API write 127.0.0.1:8000/data. The ip change depend of the project
