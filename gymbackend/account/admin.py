from django.contrib import admin, messages
from django.contrib.admin.helpers import ACTION_CHECKBOX_NAME  # ✅ NEW
from datetime import timedelta
from django import forms
from django.shortcuts import render, redirect
from .models import GymMember


class ExtendMembershipForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    extra_days = forms.IntegerField(label="Enter number of days to extend", min_value=1)


@admin.register(GymMember)
class GymMemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'sex', 'phone', 'membership_duration', 'join_date', 'expiry_date')
    search_fields = ('user__username', 'phone')
    actions = ['extend_membership']

    def extend_membership(self, request, queryset):
        if 'apply' in request.POST:
            form = ExtendMembershipForm(request.POST)
            if form.is_valid():
                extra_days = form.cleaned_data['extra_days']
                updated = 0
                for member in queryset:
                    member.expiry_date += timedelta(days=extra_days)
                    member.save()
                    updated += 1
                self.message_user(
                    request,
                    f"Successfully extended {updated} membership(s) by {extra_days} days.",
                    messages.SUCCESS,
                )
                return redirect(request.get_full_path())
        else:
            form = ExtendMembershipForm(
                initial={'_selected_action': request.POST.getlist(ACTION_CHECKBOX_NAME)}
            )

        return render(request, 'admin/extend_membership.html', {
            'members': queryset,
            'form': form,
            'title': 'Extend Membership Duration',
        })

    extend_membership.short_description = "Extend selected members by custom days"
