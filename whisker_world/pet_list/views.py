from django.shortcuts import render

def pet_list(request):
    return render(request, 'pet_list.html')