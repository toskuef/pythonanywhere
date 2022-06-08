from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from .forms import CrmLeadForm, CrmTaskForm, CrmOrderForm, CrmCustomerForm, \
    CrmDealForm
from .models import *


def crm_main(request):
    template = 'crm/crm_main.html'
    return render(request, template)


class CrmLeadList(ListView):
    model = CrmLead
    template_name = 'crm/lead/crm_lead_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_list'] = CrmLeadStatus.objects.all()
        return context


class CrmLeadCreate(CreateView):
    form_class = CrmLeadForm
    template_name = 'crm/lead/crm_lead_create.html'


class CrmLeadDetail(DetailView):
    model = CrmLead
    template_name = 'crm/lead/crm_lead_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_list'] = CrmTask.objects.filter(lead=kwargs['object'])
        context['task_status_list'] = CrmTaskStatus.objects.all()
        return context


class CrmLeadUpdate(UpdateView):
    model = CrmLead
    template_name = 'crm/lead/crm_lead_upd.html'
    fields = ['title', 'status']


class CrmLeadSourceCreate(CreateView):
    model = CrmLeadSource
    template_name = 'crm/settings/crm_lead_source.html'
    fields = ['source', 'color']


class CrmTaskList(ListView):
    model = CrmTask
    template_name = 'crm/task/crm_task_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_list'] = CrmTaskStatus.objects.all()
        return context


class CrmTaskDetail(DetailView):
    model = CrmTask
    template_name = 'crm/task/crm_task_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_list'] = CrmTask.objects.filter(task=kwargs['object'])
        context['task_status_list'] = CrmTaskStatus.objects.all()
        return context


class CrmTaskCreate(CreateView):
    form_class = CrmTaskForm
    template_name = 'crm/task/crm_task_create.html'

    def get(self, request, *args, **kwargs):
        self.initial = {self.kwargs['type_class']: self.kwargs['pk']}
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.kwargs)
        return context


class CrmTaskTypeCreate(CreateView):
    model = CrmTaskType
    template_name = 'crm/settings/crm_task_type.html'
    fields = ['type_task']


class CrmOrderList(ListView):
    model = CrmOrder
    template_name = 'crm/order/crm_order_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_list'] = CrmOrderStatus.objects.all()
        return context


class CrmOrderDetail(DetailView):
    model = CrmOrder
    template_name = 'crm/order/crm_order_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_list'] = CrmTask.objects.filter(order=kwargs['object'])
        context['task_status_list'] = CrmTaskStatus.objects.all()
        return context


class CrmOrderCreate(CreateView):
    form_class = CrmOrderForm
    template_name = 'crm/order/crm_order_create.html'


class CrmOrderUpdate(UpdateView):
    model = CrmOrder
    template_name = 'crm/order/crm_order_upd.html'
    fields = ['title', 'status']


class CrmOrderSourceCreate(CreateView):
    model = CrmOrderStatus
    template_name = 'crm/settings/crm_order_status.html'
    fields = ['status', 'color']


class CrmCustomerList(ListView):
    model = CrmCustomer
    template_name = 'crm/customer/crm_customer_list.html'


class CrmCustomerDetail(DetailView):
    model = CrmCustomer
    template_name = 'crm/customer/crm_customer_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_list'] = CrmTask.objects.filter(customer=kwargs['object'])
        context['task_status_list'] = CrmTaskStatus.objects.all()
        return context


class CrmCustomerCreate(CreateView):
    form_class = CrmCustomerForm
    template_name = 'crm/customer/crm_customer_create.html'


class CrmCustomerUpdate(UpdateView):
    model = CrmCustomer
    template_name = 'crm/customer/crm_customer_upd.html'
    fields = ['sur_name', 'first_name', 'mid_name', 'status']


class CrmDealList(ListView):
    model = CrmDeal
    template_name = 'crm/deal/crm_deal_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_list'] = CrmDealStatus.objects.all()
        return context


class CrmDealDetail(DetailView):
    model = CrmDeal
    template_name = 'crm/deal/crm_deal_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_list'] = CrmTask.objects.filter(deal=kwargs['object'])
        context['task_status_list'] = CrmTaskStatus.objects.all()
        return context


class CrmDealCreate(CreateView):
    form_class = CrmDealForm
    template_name = 'crm/deal/crm_deal_create.html'


class CrmDealUpdate(UpdateView):
    model = CrmDeal
    template_name = 'crm/deal/crm_deal_upd.html'
    fields = ['title', 'status']
