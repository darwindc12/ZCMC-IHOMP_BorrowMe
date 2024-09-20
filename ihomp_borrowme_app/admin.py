from django.contrib import admin
from .models import Borrow, Department, Peripheral, Category, Status

# Custom admin settings for the Borrow model
class BorrowAdmin(admin.ModelAdmin):
    list_display = ("borrow_id", "borrower_name", "department", "category", "peripheral", "unique_number", "status")
    list_filter = ("status",)
    search_fields = ("borrower_name", "department__description")
    list_editable = ("status",)

    def save_model(self, request, obj, form, change):
        # Check the original status of the borrow before saving the updated version
        original_borrow = Borrow.objects.get(pk=obj.pk)

        # Save the new information about the borrow
        obj.save()

        # If the status has changed, update the peripheral's status too
        if original_borrow.status != obj.status:
            obj.peripheral.status = obj.status
            obj.peripheral.save()

# Register the Borrow model in the admin interface
admin.site.register(Borrow, BorrowAdmin)

# Custom admin settings for the Department model
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("department_id", "description")
    search_fields = ("description",)

# Register the Department model in the admin interface
admin.site.register(Department, DepartmentAdmin)

# Custom admin settings for the Peripheral model
class PeripheralAdmin(admin.ModelAdmin):
    list_display = ("peripheral_id", "description", "unique_number", "status")
    list_filter = ("status",)
    search_fields = ("description", "unique_number")

# Register the Peripheral model in the admin interface
admin.site.register(Peripheral, PeripheralAdmin)

# Custom admin settings for the Category model
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_id", "description")
    search_fields = ("description",)

# Register the Category model in the admin interface
admin.site.register(Category, CategoryAdmin)

# Custom admin settings for the Status model
class StatusAdmin(admin.ModelAdmin):
    list_display = ("status_id", "name")

# Register the Status model in the admin interface
admin.site.register(Status, StatusAdmin)
