from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Book)
admin.site.register(models.LibraryCard)
admin.site.register(models.Borrowing)
admin.site.register(models.DownloadHistory)


