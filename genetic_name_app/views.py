from django.shortcuts import render
from django.http import JsonResponse
from genetic_name_app.genetic import predict

# Create your views here.
def index(request):
    target = request.GET['s']
    prediction = predict(target)
    names = [prediction[i][0] for i in range(len(prediction))]
    return JsonResponse({'predictions': names})
