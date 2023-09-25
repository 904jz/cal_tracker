from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile
import requests
from datetime import datetime as dt
import json

API_KEY = 'wsSSUmN1a8/r1RIRzsd5pw==N28caiG941GVVz49'
api_url = 'https://api.calorieninjas.com/v1/nutrition?query='

# Create your views here.
def add_food(request):
    values = []
    context = {}
    cal_avg = 0
    if request.user.is_authenticated:
        user = Profile.objects.get(user=request.user)
        if request.method == 'POST':
            food_eaten = request.POST['food_eaten']
            query = food_eaten
            response = requests.get(api_url + query,headers={'X-Api-Key' : API_KEY})
            print(response.json())
            items = response.json().get('items')
            carbs = 0
            fat = 0
            protein = 0
            calories = 0
            for item in items:
                carbs += item['carbohydrates_total_g']
                fat += item['fat_total_g']
                protein += item['protein_g']
                calories += item['calories']
            
            total = carbs + protein + fat
            print(carbs/total)


            user = Profile.objects.get(user=request.user)
            user.carbs += carbs
            user.fat += fat
            user.protein += protein
            user.calories += calories
            if user.last_updated.day != dt.today:
                user.day_count += 1
            user.last_updated = dt.now()
            cal_avg = user.calories/user.day_count
            user.save()
            # print(user.carbs)
            # print(user.fat)
            # print(user.protein)

            

        values = [user.carbs,user.fat,user.protein]
        exp = json.dumps(values)
        context = {"nutrition":exp,"calorie":cal_avg}   



    return render(request,'home.html',context)