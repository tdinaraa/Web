from rest_framework import serializers
from api.models import Company, Vacancy

class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    city = serializers.CharField()
    address = serializers.CharField()

    def create(self, validated_data):
        company = Company.objects.create(name=validated_data.get('name'), description=validated_data.get('description'), city=validated_data.get('city'), address=validated_data.get('address'))
        return company
    #should be written all fields, but will change only that were indicated
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

#Authomatically creates "create", "update" functions
class CompanySerializer2(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=200) -> such that we may rewrite

    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'city', 'address',)

class VacancySerializer(serializers.ModelSerializer):
    # Nested Serializers
    # company = CompanySerializer2(read_only=True) #wants to read all fields of company
    company_id = serializers.IntegerField(write_only=True) #wants to write an integer

    class Meta:
        model = Vacancy
        fields = ('id', 'name', 'description', 'salary', 'company_id')


class CompanyWithVacanciesSerializer(serializers.ModelSerializer):
    # vacancies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # vacancies = serializers.StringRelatedField(many=True, read_only=True)
    vacancies = VacancySerializer(many=True, read_only=True) #to show list of vacancies in one company

    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'city', 'address', 'vacancies',)

