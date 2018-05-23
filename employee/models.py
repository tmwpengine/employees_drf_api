from django.db import models


class Company(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=50)
	location = models.CharField(max_length=50)

	def __str__(self):
		return self.name_and_location()

	def name_and_location(self):
		return '{name} in {location}'.format(name=self.name, location=self.location)


class Employee(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	full_time = models.BooleanField()
	age = models.IntegerField()
	gender = models.CharField(max_length=10, blank=True, null=True)
	address = models.TextField(blank=True, null=True)
	company = models.ForeignKey(Company, on_delete=models.CASCADE)

	class Meta:
		ordering = ('created', )

	def __str__(self):
		return self.full_name()

	def full_name(self):
		return '{first_name} {last_name}'.format(
			first_name=self.first_name,
			last_name=self.last_name
		)

	def old_as_fuck(self):
		return True if self.age >= 30 else False
