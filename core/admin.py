
from django.contrib import admin
from .models import User, Doctor, Specialty, Patient, Appointment, Notification, DoctorAvailability, Setting

# تخصيص عرض الأطباء في لوحة التحكم
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['user', 'specialty']
    search_fields = ['user__username', 'specialty__name']

# تخصيص عرض المرضى في لوحة التحكم
class PatientAdmin(admin.ModelAdmin):
    list_display = ['user', 'medical_history']
    search_fields = ['user__username']

# تخصيص عرض المستخدمين
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'role']
    search_fields = ['username', 'role']

admin.site.register(User, UserAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Specialty)
admin.site.register(Appointment)
admin.site.register(Notification)
admin.site.register(DoctorAvailability)
admin.site.register(Setting)
