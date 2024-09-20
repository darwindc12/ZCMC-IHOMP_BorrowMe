from django.db import models

# Model to represent different categories of devices
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_description = models.CharField(max_length=2000, help_text="Brief description of the category.")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category_description  # Shows the category description when this object is printed

# Model for status types (like available or borrowed)
class Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, help_text="Status name (e.g., Available, Borrowed).")

    def __str__(self):
        return self.name  # Displays the status name

# Model for individual peripheral devices
class Peripheral(models.Model):
    peripheral_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=2000, help_text="Brief description of the peripheral.")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='peripherals',
                                 help_text="The category this peripheral belongs to.")
    unique_number = models.CharField(max_length=2000, unique=True, help_text="Unique ID for the peripheral.")
    status = models.ForeignKey(Status, on_delete=models.PROTECT, default=1,
                               help_text="Current status of the peripheral (e.g., available, in use).")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description  # Shows the peripheral's description when printed

# Model for different departments within an organization
class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=2000, help_text="Brief description of the department.")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description  # Displays the department description

# Model to record borrow actions (who borrowed what)
class Borrow(models.Model):
    borrow_id = models.AutoField(primary_key=True)
    borrower_name = models.CharField(max_length=2000, help_text="Name of the person or department borrowing the item.")
    department = models.ForeignKey(Department, on_delete=models.PROTECT, help_text="Department borrowing the device.")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, help_text="Category of the borrowed peripheral.")
    peripheral = models.ForeignKey(Peripheral, on_delete=models.PROTECT, help_text="Specific peripheral being borrowed.")
    unique_number = models.CharField(max_length=2000, blank=True, help_text="Unique identifier for this borrow action.")
    status = models.ForeignKey(Status, on_delete=models.PROTECT, default=2,
                               help_text="Current status of the borrow action (e.g., Borrowed).")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.borrower_name  # Displays the name of the borrower
