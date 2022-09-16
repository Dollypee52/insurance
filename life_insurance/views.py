from django.http import HttpResponseRedirect
from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
from django.urls import reverse

from life_insurance.models import Policy_Bond


def index(request):
    return render(request,'life_insurance/index.html')

def about(request):
    return render(request, 'life_insurance/about.html')

def redirect(request):
    return HttpResponseRedirect(reverse('life_insurance:index'))

def policy_details(request,pk):
    policy = Policy_Bond.objects.get(pk=pk)
    return render(request, 'life_insurance/policy_details.html',{'policy':policy})

def policy_list(request):
    policy = Policy_Bond.objects.all()
    return render(request, 'life_insurance/policy_list.html', {'policy':policy})

