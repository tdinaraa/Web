import json
from django.shortcuts import render
from django.http.response import JsonResponse
from api.models import Company, Vacancy

from django.views.decorators.csrf import csrf_exempt
from api.serializers import CompanySerializer

@csrf_exempt
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return JsonResponse(serializer.data, safe=False)

        # companies_json = [company.to_json() for company in companies]
        # return JsonResponse(companies_json, safe=False)
    elif request.method == 'POST':
        request_body = json.loads(request.body)

        serializer = CompanySerializer(data=request_body) #we want to create absolutely new item
        if serializer.is_valid():  # Validate data from client (check all fields)
            serializer.save() #save calls the function create
            return JsonResponse(serializer.data)
        return JsonResponse({'error': serializer.errors})

        # data = json.loads(request.body)
        # company = Company.objects.create(name=data['name'], description=data['description'], city=data['city'], address=data['address'])
        # return JsonResponse(company.to_json())


@csrf_exempt
def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    #Get one object
    if request.method == 'GET':
        return JsonResponse(company.to_json())
    #Update selected oject
    elif request.method == 'PUT':
        request_body = json.loads(request.body)
        serializer = CompanySerializer(instance=company, data=request_body) #want to updtae this info by that data
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error': serializer.errors})



        # data = json.loads(request.body)
        # company.name = data['name']
        # company.description = data['description']
        # company.save()
        # return JsonResponse(company.to_json())

    #Delete selected object
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({'deleted': True})


def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(vacancy.to_json())


def company_vacancies(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    vacancies = company.vacancy_set.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]

    return JsonResponse(vacancies_json, safe=False)

def top_ten(request):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)