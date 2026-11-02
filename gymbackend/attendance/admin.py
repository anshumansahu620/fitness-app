# attendance/admin.py
from django.contrib import admin
from .models import AttendanceModel

@admin.register(AttendanceModel)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'member', 'get_member_name', 'status', 'entry_time', 'date')
    search_fields = ('id', 'date', 'member__full_name')  # ✅ changed 'name' to 'full_name'

    def get_member_name(self, obj):
        return obj.member.full_name  # ✅ fixed wrong reference
    get_member_name.short_description = 'Member Name'


