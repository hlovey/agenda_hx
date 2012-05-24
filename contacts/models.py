from django.db import models

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Phone(models.Model):
    person = models.ForeignKey(Person)

    description = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)


class Address(models.Model):
    person = models.ForeignKey(Person)

    description = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=8)

    address = models.CharField(max_length=30)

