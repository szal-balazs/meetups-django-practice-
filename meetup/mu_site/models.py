from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} ({self.address})'
    

class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.name} ({self.email})'
    

class Organizer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Meetup(models.Model):
    title = models.CharField(max_length=200)
    location = models.ForeignKey(Location, null=False, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="images")
    slug = models.SlugField(unique=True)
    participant = models.ManyToManyField(Participant, blank=True)
    date = models.DateField()
    organizer = models.ForeignKey(Organizer, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title