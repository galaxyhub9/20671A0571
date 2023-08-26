from django.shortcuts import render
from django.http import JsonResponse
import requests
import time

def GetNumbers(request):
    urls = request.GET.getlist('url')
    merged_numbers = []

    for url in urls:
        try:
            response = requests.get(url, timeout=0.5)
            if response.status_code == 200:
                data = response.json()
                numbers = data.get('numbers', [])
                print(f"Numbers from {url}: {numbers}")  
                merged_numbers.extend(numbers)
            else:
                print(f"Request to {url} failed with status code: {response.status_code}")  # Debug print
                print(f"Response content: {response.content}")  
        except requests.Timeout:
            print(f"Request to {url} timed out") 
    merged_numbers = sorted(list(set(merged_numbers)))
    print(f"Merged Numbers: {merged_numbers}") 
    return JsonResponse({'numbers': merged_numbers})
