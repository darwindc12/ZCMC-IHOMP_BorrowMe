from django.db import models


class Category(models.Model):
    """
    Model representing a category of peripherals.
    """
    category_id = models.AutoField(primary_key=True)
    category_description = models.CharField(max_length=2000, help_text="Descriptive of the category.")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "categories"
    def __str__(self):
        """
        String representation of the Category model, returning the description.
        """
        return self.category_description


class Status(models.Model):
    """
    Model representing the status of a peripheral or a borrow action.
    """
    status_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, help_text="Name of the status.")

    def __str__(self):
        """
        String representation of the Status model, returning the status name.
        """
        return self.name


class Peripheral(models.Model):
    """
    Model representing a peripheral device.
    """
    peripheral_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=2000, help_text="Description of peripheral.")
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='peripherals',
        help_text="Category to witch peripheral belongs."
    )
    unique_number = models.CharField(max_length=2000, unique=True, help_text="Unique identifier for the peripheral.")
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        default=1,
        help_text="Current status of the peripheral."
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        String representation of the Peripheral model, returning the description.
        """
        return self.description


class Department(models.Model):
    """
    Model representing a department within an organization.
    """
    department_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=2000, help_text="Description of the department.")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        String representation of the department model, returning the description.
        """
        return self.description

class Borrow(models.Model):
    """
    Model representing a borrow action, where a peripheral is borrowed by a department.
    """
    borrow_id = models.AutoField(primary_key=True)
    borrower_name = models.CharField(
        max_length=2000,
        help_text="Name of the person or department borrowing the peripheral."
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        help_text="Department from witch the peripheral is borrowed."
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        help_text="Category of the borrowed peripheral."
    )
    peripheral = models.ForeignKey(
        Peripheral,
        on_delete=models.PROTECT,
        help_text="The specific peripheral being borrowed."
    )
    unique_number = models.CharField(
        max_length=2000,
        blank=True,
        help_text="Unique identifier for the borrow action, if applicable."
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        default=2,
        help_text="Current status of the borrow action."
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        String representation of the Borrow model, returning the borrower's name.
        """
        return self.borrower_name
