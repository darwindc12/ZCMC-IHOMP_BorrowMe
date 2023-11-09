from django.views import generic
from .models import Peripheral, Category, Department


class CombinedListView(generic.ListView):
    model = Category
    # queryset = Category.objects.order_by("-date_created")
    template_name = "index.html"
    # context_object_name = 'category_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['department_list'] = Department.objects.all()
        context['category_list'] = Category.objects.all()
        context['peripheral_list'] = Peripheral.objects.all()
        return context