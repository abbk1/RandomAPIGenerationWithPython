from django.http import HttpResponse
from django.shortcuts import render
import requests
import csv

def index(request):
  response = requests.get('https://dog.ceo/api/breeds/image/random')
  data = response.json()
  image = data['message']
  status = response.status_code
  if request.method == 'POST':
    # Get data from the form
    name = request.POST.get("name")
    email = request.POST.get("email")
    age = request.POST.get("age")
    address = request.POST.get("address")
    # Save to a CSV file
    with open("biodata.csv", "a", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, email, age, address])

    return render(request, "template/thank_you.html")
    
  return render(request, 'template/index.html', {'image': image})