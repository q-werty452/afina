from django.shortcuts import render
from .models import *

def index(request):
    context = {
        'banners': Banner.objects.all(),
        'categories': Category.objects.all(),
        'features': FeatureProduct.objects.all(),
        'testimonials': Testimonial.objects.all(),
        'posts': BlogPost.objects.all(),
    }
    return render(request, 'index.html', context)