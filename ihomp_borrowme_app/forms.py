from django import forms

# Form that handles borrowing a device
class BorrowDeviceForm(forms.Form):
    borrower_name = forms.CharField(max_length=80, help_text="Enter the borrower's name.")
    department = forms.CharField(max_length=80, help_text="Enter the department's name.")
    category = forms.CharField(max_length=80, help_text="Select the device category.")
    peripheral = forms.CharField(max_length=80, help_text="Select the specific peripheral.")
    unique_number = forms.CharField(max_length=80, help_text="Enter the device's unique ID.")
