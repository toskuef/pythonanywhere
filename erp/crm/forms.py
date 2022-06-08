from django import forms

from .models import *


class CrmLeadForm(forms.ModelForm):
    class Meta:
        model = CrmLead
        fields = '__all__'


class CrmTaskForm(forms.ModelForm):
    class Meta:
        model = CrmTask
        fields = '__all__'


class CrmOrderForm(forms.ModelForm):
    class Meta:
        model = CrmOrder
        fields = '__all__'


class CrmCustomerForm(forms.ModelForm):
    class Meta:
        model = CrmCustomer
        fields = '__all__'


class CrmDealForm(forms.ModelForm):
    class Meta:
        model = CrmDeal
        fields = '__all__'
