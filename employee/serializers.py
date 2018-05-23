from rest_framework import serializers
from employee.models import Employee, Company


class EmployeeSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	first_name = serializers.CharField(required=False, allow_blank=True, max_length=100)
	lastname = serializers.CharField(required=False, allow_blank=True, max_length=100)
	full_time = serializers.BooleanField(required=False)
	age = serializers.IntegerField()
	gender = serializers.CharField(required=False, allow_blank=True, max_length=100)
	address = serializers.CharField(required=False, allow_blank=True, max_length=100)
	company = serializers.CharField(required=False, allow_blank=True, max_length=100)
	#company = serializers.HyperlinkedIdentityField(view_name='employee_detail', lookup_field='id')

	def create(self, validated_data):
		return Employee.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.first_name = validated_data.get('first_name', instance.first_name)
		instance.last_name = validated_data.get('last_name', instance.last_name)
		instance.full_time = validated_data.get('linenos', instance.full_time)
		instance.age = validated_data.get('age', instance.age)
		instance.gender = validated_data.get('gender', instance.gender)
		instance.address = validated_data.get('address', instance.address)

		instance.save()

		return instance


class CompanySerializer(serializers.ModelSerializer):
	class Meta:
		model = Company
		fields = ('name', 'location')
