from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Peripheral, Category, Department
from .forms import BorrowerForm
from django.contrib import messages
from .models import Borrow
from django.http import JsonResponse


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


def borrow_form(request):
    department_list = Department.objects.all()
    category_list = Category.objects.all()
    peripheral_list = []

    if request.method == 'POST':
        form = BorrowerForm(request.POST)
        if form.is_valid():
            borrower_name = form.cleaned_data['borrower_name']
            department_id = form.cleaned_data['department']
            category_id = form.cleaned_data['category']
            peripheral_id = form.cleaned_data['peripheral']
            unique_number = form.cleaned_data['unique_number']

            print(unique_number)

            # Get Department, Category, and Peripheral instances based on IDs
            department = get_object_or_404(Department, department_id=department_id)
            category = get_object_or_404(Category, category_id=category_id)
            peripheral = get_object_or_404(Peripheral, peripheral_id=peripheral_id)

            # Create the Borrow object with instances
            Borrow.objects.create(
                borrower_name=borrower_name,
                department=department,
                category=category,
                peripheral=peripheral,
                unique_number=unique_number
            )

            Peripheral.objects.filter(unique_number=unique_number).update(status=2)

            messages.success(request, 'Form submitted successfully!')

        # You should include the code to update peripheral_list based on the selected category here.
        if category_id:
            peripheral_list = Peripheral.objects.filter(category=category)

    return render(request, "borrower-form.html", {
        'department_list': department_list,
        'category_list': category_list,
        'peripheral_list': peripheral_list,
    })


def get_peripherals(request, category_id):
    peripherals = Peripheral.objects.filter(category_id=category_id, status=1)
    data = [{"peripheral_id": peripheral.peripheral_id, "peripheral_description": peripheral.peripheral_description} for peripheral in peripherals]
    print(data)
    return JsonResponse({"peripherals": data})


def get_unique_number(request, peripheral_id):
    try:
        peripheral = Peripheral.objects.get(pk=peripheral_id)
        unique_numbers = peripheral.unique_number.split(',') if peripheral.unique_number else []
        data = [{"unique_number_id": num, "unique_number_description": num} for num in unique_numbers]
        print(data)
    except Peripheral.DoesNotExist:
        data = []

    return JsonResponse({"uniqueNumbers": data})




