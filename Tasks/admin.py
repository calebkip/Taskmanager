from django.contrib import admin
from .models import Ticket,Department,Category,Technician,Supervisor,Caller
from Core.admin import UserAdmin

# Register your models here.
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("description", "created", "owner")
@admin.register(Department)
class DepartmenttAdmin(admin.ModelAdmin):
    list_display = ("title","supervisor")
@admin.register(Technician)
class TechnicianAdmin(admin.ModelAdmin):
    list_display = ("user","department")
@admin.register(Caller)
class CallerAdmin(admin.ModelAdmin):
    list_display = ("user","department")
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
    # list_display = ("title")
@admin.register(Supervisor)
class SupervisorAdmin(admin.ModelAdmin):
    list_display = ("title","user")
    
