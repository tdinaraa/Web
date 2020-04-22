import json
from django.shortcuts import render
from django.http.response import JsonResponse
from api.models import Company, Vacancy

from django.views.decorators.csrf import csrf_exempt
from api.serializers import  CompanySerializer, CompanySerializer2

@csrf_exempt
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer2(companies, many=True)
        return JsonResponse(serializer.data, safe=False)


    elif request.method == 'POST':
        request_body = json.loads(request.body)

        serializer = CompanySerializer2(data=request_body)
        if serializer.is_valid():  # Check all fields
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error': serializer.errors})


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
        serializer = CompanySerializer2(instance=company, data=request_body) #want to updtae this info by that data
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error': serializer.errors})



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