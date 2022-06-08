from django.urls import path
from . import views

app_name = 'crm'

urlpatterns = [
    path('',
         views.crm_main,
         name='crm_main'),

    path('leads/',
         views.CrmLeadList.as_view(),
         name='crm_lead_list'),
    path('leads/create',
         views.CrmLeadCreate.as_view(),
         name='crm_lead_create'),
    path('leads/settings/source/',
         views.CrmLeadSourceCreate.as_view(),
         name='crm_lead_source'),
    path('leads/<int:pk>',
         views.CrmLeadDetail.as_view(),
         name='crm_lead_detail'),
    path('leads/<int:pk>/edit',
         views.CrmLeadUpdate.as_view(),
         name='crm_lead_update'),

    path('tasks/',
         views.CrmTaskList.as_view(),
         name='crm_task_list'),
    path('tasks/<int:pk>',
         views.CrmTaskDetail.as_view(),
         name='crm_task_detail'),
    path('tasks/<slug:type_class>/<int:pk>/create/',
         views.CrmTaskCreate.as_view(),
         name='crm_task_create'),
    path('tasks/settings/type/',
         views.CrmTaskTypeCreate.as_view(),
         name='crm_task_type'),

    path('order/',
         views.CrmOrderList.as_view(),
         name='crm_order_list'),
    path('order/create',
         views.CrmOrderCreate.as_view(),
         name='crm_order_create'),
    path('order/settings/status/',
         views.CrmOrderSourceCreate.as_view(),
         name='crm_order_status'),
    path('order/<int:pk>',
         views.CrmOrderDetail.as_view(),
         name='crm_order_detail'),
    path('order/<int:pk>/edit',
         views.CrmOrderUpdate.as_view(),
         name='crm_order_update'),

    path('customer/',
         views.CrmCustomerList.as_view(),
         name='crm_customer_list'),
    path('customer/create',
         views.CrmCustomerCreate.as_view(),
         name='crm_customer_create'),
    path('customer/<int:pk>',
         views.CrmCustomerDetail.as_view(),
         name='crm_customer_detail'),
    path('customer/<int:pk>/edit',
         views.CrmCustomerUpdate.as_view(),
         name='crm_customer_update'),

    path('deal/',
         views.CrmDealList.as_view(),
         name='crm_deal_list'),
    path('deal/create',
         views.CrmDealCreate.as_view(),
         name='crm_deal_create'),
    path('deal/<int:pk>',
         views.CrmDealDetail.as_view(),
         name='crm_deal_detail'),
    path('deal/<int:pk>/edit',
         views.CrmDealUpdate.as_view(),
         name='crm_deal_update'),

    path('vk/',
         views.vk),
]
