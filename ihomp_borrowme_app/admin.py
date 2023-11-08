from django.contrib import admin
from .models import Borrow, Department, Peripheral, Category, Status


class BorrowAdmin(admin.ModelAdmin):
    list_display = ("borrow_id", "borrower_name", "department", "category", "peripheral", "unique_number", "status")
    list_filter = ("status",)
    search_fields = ("borrower_name", "department__department_description")
    list_editable = ("status",)

    def save_model(self, request, obj, form, change):
        # Get the original status of the Borrow object before saving changes
        original_borrow = Borrow.objects.get(pk=obj.pk)

        # Save the updated Borrow object
        obj.save()

        # Check if the status has changed
        if original_borrow.status != obj.status:
            # Update the related Peripheral's status
            obj.peripheral.status = obj.status
            obj.peripheral.save()


admin.site.register(Borrow, BorrowAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("department_id", "department_description")
    search_fields = ("department_description",)


admin.site.register(Department, DepartmentAdmin)


class PeripheralAdmin(admin.ModelAdmin):
    list_display = ("peripheral_id", "peripheral_description", "unique_number","status")
    list_filter = ("status",)
    search_fields = ("peripheral_description", "unique_number")


admin.site.register(Peripheral, PeripheralAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_id", "category_description")
    search_fields = ("category_description",)

admin.site.register(Category, CategoryAdmin)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("status_id", "status_name")

admin.site.register(Status, StatusAdmin)

