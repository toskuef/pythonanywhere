from django.contrib import admin
from .models import *


admin.site.register(CrmLead)
admin.site.register(CrmLeadStatus)
admin.site.register(CrmLeadSource)
admin.site.register(CrmCustomer)
admin.site.register(CrmCustomerAddress)
admin.site.register(CrmCustomerStatus)
admin.site.register(CrmTask)
admin.site.register(CrmTaskType)
admin.site.register(CrmTaskStatus)
admin.site.register(CrmDeal)
admin.site.register(CrmDealStatus)
admin.site.register(CrmOrder)
admin.site.register(CrmOrderStatus)
admin.site.register(CrmColor)
admin.site.register(CrmAddressCountry)
admin.site.register(CrmAddressArea)
admin.site.register(CrmAddressRegion)
admin.site.register(CrmAddressTown)
admin.site.register(CrmAddressStreet)

