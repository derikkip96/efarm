from django.shortcuts import render,get_object_or_404
from . models import Input,Category

# Create your views here.
def hireView(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    inputs = Input.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug )
        inputs = Input.objects.filter(category=category)
    return render(request,'hire/hire_list.html',{'category':category,
                                                 'categories':categories,
                                                 'inputs':inputs})

def input_detail(request,id, slug):
    input = get_object_or_404(Input,
                            id=id,
                            slug=slug
                            )
    return  render(request,'hire/hire_detail.html',{ 'input':input })