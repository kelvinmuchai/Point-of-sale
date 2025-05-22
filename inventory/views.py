from django.shortcuts import render
from .models import Products,Category
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView
from .forms import ProductsUpdateForm
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.




def ProductsSearch(request):
    if request.method == 'GET':
         searched = request.GET['q']
         #returned search results
         products = Products.objects.filter(Q(p_name__contains=searched)|Q(p_description__icontains=searched))
         return render(request,'inventory/search.html',{'searched':searched,'products':products})
  
    return render(request,'inventory/search.html',{})



class ProductsListView(LoginRequiredMixin,ListView):
    model = Products

    template_name = 'inventory/home.html'
    context_object_name = 'products'
    
    #To add extra context to a classbasedview
    '''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add custom context here
        context['extra_info'] = 'This is some extra info'
        return context
  '''

def product_detail(request, pk):
    product = get_object_or_404(Products, pk=pk)
    related_products = Products.objects.filter(p_category=product.p_category).exclude(pk=product.pk)

    return render(request, 'inventory/products_detail.html', {
        'product': product,
        'products': related_products
    })




class ProductsCreateView(CreateView):
    model = Products
    fields = ['p_name','p_description','p_image','p_price','p_costprice','p_category']

    #success_url = reverse_lazy('home-page')

    
    #adding messages
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Product created successfully!")
        return response


class ProductsUpdateView(UpdateView):
    model = Products
    fields = ['p_name','p_description','p_image','p_price','p_costprice','p_category']

    #success_url = reverse_lazy('home-page')

    
    #adding messages
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Product created successfully!")
        return response


class ProductDeleteView(DeleteView):
    model = Products

    success_url = reverse_lazy('home-page')


class CategoryListView(ListView):
    model = Category
   
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.prefetch_related('products').all()

class CategoryCreateView(CreateView):
    model = Category
    fields = '__all__'





    #image format
    #saving images
    #saving categories