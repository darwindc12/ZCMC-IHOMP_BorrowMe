from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import Department, Category, Peripheral, Borrow
from .forms import BorrowerForm

# Home page that pulls together departments, categories, and peripherals for the user to browse
class OverviewPageView(ListView):
    template_name = 'index.html'
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departments'] = Department.objects.all()
        context['categories'] = Category.objects.all()
        context['peripherals'] = Peripheral.objects.all()
        return context

# Handling the borrowing form submission process
def handle_borrow_request(request):
    form = BorrowerForm()

    if request.method == 'POST':
        form = BorrowerForm(request.POST)
        if form.is_valid():
            borrow = form.save(commit=False)
            selected_peripheral = Peripheral.objects.get(id=borrow.peripheral.id)
            selected_peripheral.status = 2  # Assuming '2' means borrowed
            selected_peripheral.save()
            borrow.save()

            # Giving feedback to the user
            messages.success(request, 'Device successfully borrowed!')
            return redirect('homepage')

    return render(request, 'borrow_form.html', {'form': form})

# Dynamically updating peripherals based on selected category
def fetch_peripherals(request):
    category_id = request.GET.get('category_id')
    peripherals = Peripheral.objects.filter(category_id=category_id, status=1)  # Assuming '1' means available
    peripherals_list = list(peripherals.values('id', 'name'))
    return JsonResponse(peripherals_list, safe=False)

# Providing unique numbers associated with a selected peripheral
def get_peripheral_unique_numbers(request):
    peripheral_id = request.GET.get('peripheral_id')
    unique_numbers = []
    try:
        peripheral = Peripheral.objects.get(id=peripheral_id)
        unique_numbers = list(peripheral.unique_numbers.values('number'))
    except Peripheral.DoesNotExist:
        pass  # If no peripheral is found, return an empty list

    return JsonResponse(unique_numbers, safe=False)
