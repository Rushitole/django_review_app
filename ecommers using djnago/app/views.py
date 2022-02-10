from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from . models import Product,Review
from django.urls import reverse



# Create your views here.

def homepage(request):
    data=Product.objects.all()
    return render(request,'app/home.html',{"data1":data})

def review(request,id):
    product=Product.objects.get(id=id)
    review=Review.objects.filter(product=product)
    return render(request,'app/review.html',{"product":product,"reviews":review})

def post_review(request,id):
    rev_name=request.POST.get('reviewername')
    rev_rating=request.POST.get('reviewerrating')
    rev_body=request.POST.get('reviewbody')
    # rev_date=request.POST.get('reviewdate')
    product=Product.objects.get(id=id)
    obj=Review(product=product,Reviewer=rev_name,rating=rev_rating,comment=rev_body,)
    obj.save()
    return HttpResponseRedirect(reverse('app:review',args=(id)))