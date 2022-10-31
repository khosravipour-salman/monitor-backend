from rest_framework import serializers

from accounting.models import User, InternProxy


class InternRegisterSerializer(serializers.Serializer):
	phone_number = serializers.CharField(required=True, write_only=True)
	password = serializers.CharField(required=True, write_only=True)
	first_name = serializers.CharField()
	last_name = serializers.CharField()
	national_code = serializers.CharField()
	birth_date = serializers.DateTimeField()
	personality_type = serializers.CharField()
	intern_code = serializers.CharField()
	picture = serializers.ImageField()

	def validate_national_code(self, value):
		# user national code validation here!
		pass

	def create(self, validated_data):
		phone_number, password = validated_data.pop('phone_number'), validated_data.pop('password')
		user = User.objects.create_intern(phone_number=phone_number, password=password)
		intern_obj = InternProxy.objects.create(user, **validated_data)

		return intern_obj



