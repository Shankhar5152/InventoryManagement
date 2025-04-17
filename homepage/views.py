from django.shortcuts import render
from django.views.generic import View, TemplateView
from inventory.models import Stock
from transactions.models import SaleBill, PurchaseBill


class HomeView(View):
    template_name = "home.html"
    
    def get(self, request):        
        labels = []
        data = []        
        # Query for Stock items, only non-deleted, ordered by quantity
        stockqueryset = Stock.objects.filter(is_deleted=False).order_by('-quantity')
        
        # Loop through the queryset to create data for the chart
        for item in stockqueryset:
            labels.append(item.name)
            data.append(item.quantity)
        
        # Fetch the latest 3 SaleBill and PurchaseBill records
        sales = SaleBill.objects.order_by('-time')[:3]
        purchases = PurchaseBill.objects.order_by('-time')[:3]
        
        # Context to pass to the template
        context = {
            'labels': labels,
            'data': data,
            'sales': sales,
            'purchases': purchases
        }
        
        return render(request, self.template_name, context)


class AboutView(TemplateView):
    template_name = "about.html"  # This is fine as it's just a static page
