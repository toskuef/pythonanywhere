from django.db import models
from django.urls import reverse


class CrmLead(models.Model):
    """Модель таблицы с лидами"""
    title = models.CharField(verbose_name='название', max_length=150)
    phone = models.CharField(verbose_name='номер телефона',
                             max_length=12, blank=True)
    email = models.EmailField(verbose_name='электронная почта', blank=True)
    customer = models.OneToOneField(
        'CrmCustomer',
        on_delete=models.PROTECT,
        related_name='lead',
        verbose_name='клиент',
        blank=True,
        null=True,
    )

    source = models.ForeignKey(
        'CrmLeadSource',
        on_delete=models.SET_NULL,
        related_name='leads',
        verbose_name='источник',
        blank=True,
        null=True,
    )
    status = models.ForeignKey(
        'CrmLeadStatus',
        on_delete=models.PROTECT,
        related_name='leads',
        verbose_name='статус',
        default=1,
    )

    class Meta:
        verbose_name = 'лид'
        verbose_name_plural = 'лиды'

    def get_absolute_url(self):
        return reverse('crm:crm_lead_list')

    def __str__(self):
        return self.title


class CrmLeadStatus(models.Model):
    """Модель таблицы со статусами лида"""
    status = models.CharField(verbose_name='название статуса', max_length=100)
    color = models.ForeignKey(
        'CrmColor',
        on_delete=models.SET_NULL,
        verbose_name='цвет',
        related_name='lead_statuses',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'статус лида'
        verbose_name_plural = 'статусы лидов'

    def __str__(self):
        return self.status


class CrmLeadSource(models.Model):
    """Модель таблицы со списком источников лида"""
    source = models.CharField(verbose_name='название источника',
                              max_length=100)
    color = models.ForeignKey(
        'CrmColor',
        on_delete=models.SET_NULL,
        verbose_name='цвет',
        related_name='lead_sources',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'источник лида'
        verbose_name_plural = 'источники лидов'

    def __str__(self):
        return self.source

    def get_absolute_url(self):
        return reverse('crm:crm_lead_create')


class CrmCustomer(models.Model):
    """Модель таблицы с клиентами"""
    sur_name = models.CharField(verbose_name='фамилия', max_length=100)
    first_name = models.CharField(verbose_name='имя', max_length=100)
    mid_name = models.CharField(verbose_name='отчество', max_length=100)
    phone = models.CharField(verbose_name='номер телефона', max_length=12)
    email = models.EmailField(verbose_name='электронная почта', blank=True)
    status = models.ForeignKey(
        'CrmCustomerStatus',
        on_delete=models.PROTECT,
        verbose_name='юридический статус',
        related_name='customers',
        default=1,
    )
    address = models.ManyToManyField(
        'CrmCustomerAddress',
        verbose_name='адреса клиента',
        related_name='customers',
        blank=True,
    )

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'

    def get_absolute_url(self):
        return reverse('crm:crm_customer_list')

    def __str__(self):
        return self.sur_name


class CrmCustomerStatus(models.Model):
    """Модель с юридическими статусами клиента"""
    status = models.CharField(verbose_name='название статуса', max_length=100)
    color = models.ForeignKey(
        'CrmColor',
        on_delete=models.SET_NULL,
        verbose_name='цвет',
        related_name='customer_statuses',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'статус клиента'
        verbose_name_plural = 'статусы клиентов'

    def __str__(self):
        return self.status


class CrmCustomerAddress(models.Model):
    """Модель с адресами клиентов"""
    country = models.ForeignKey(
        'CrmAddressCountry',
        on_delete=models.PROTECT,
        related_name='addresses',
        verbose_name='страна',
    )
    area = models.ForeignKey(
        'CrmAddressArea',
        on_delete=models.PROTECT,
        related_name='addresses',
        verbose_name='область',
    )
    region = models.ForeignKey(
        'CrmAddressRegion',
        on_delete=models.PROTECT,
        related_name='addresses',
        verbose_name='район',
    )
    town = models.ForeignKey(
        'CrmAddressTown',
        on_delete=models.PROTECT,
        related_name='addresses',
        verbose_name='город',
    )
    street = models.ForeignKey(
        'CrmAddressStreet',
        on_delete=models.PROTECT,
        related_name='addresses',
        verbose_name='улица',
    )
    num_house = models.IntegerField(verbose_name='номер дома', blank=True)
    num_housing = models.IntegerField(verbose_name='номер корпуса', blank=True)
    num_door = models.IntegerField(verbose_name='номер подъезда', blank=True)
    num_level = models.IntegerField(verbose_name='номер этажа', blank=True)
    num_flat = models.IntegerField(verbose_name='номер квартиры', blank=True)

    class Meta:
        verbose_name = 'адрес'
        verbose_name_plural = 'адреса'

    def __str__(self):
        return (f'{self.country}, {self.area}, {self.region}, {self.town}, '
                f'{self.street}, {self.num_house}, {self.num_housing}, '
                f'{self.num_door}, {self.num_level}, {self.num_flat}')


class CrmTask(models.Model):
    """Модель с задачами"""
    type_task = models.ForeignKey(
        'CrmTaskType',
        on_delete=models.PROTECT,
        verbose_name='тип задачи',
        related_name='tasks',
    )
    text = models.TextField(verbose_name='описание')
    status = models.ForeignKey(
        'CrmTaskStatus',
        on_delete=models.PROTECT,
        verbose_name='статус задачи',
        related_name='tasks',
        default=1
    )
    lead = models.ForeignKey(
        'CrmLead',
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name='лид',
        blank=True,
        null=True,
    )
    customer = models.ForeignKey(
        'CrmCustomer',
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name='клиент',
        blank=True,
        null=True,
    )
    order = models.ForeignKey(
        'CrmOrder',
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name='заказ',
        blank=True,
        null=True,
    )
    deal = models.ForeignKey(
        'CrmDeal',
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name='сделка',
        blank=True,
        null=True,
    )
    task = models.ForeignKey(
        'CrmTask',
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name='задача',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'

    def __str__(self):
        return self.type_task.type_task

    def get_absolute_url(self):
        return reverse('crm:crm_task_detail', kwargs={'pk': self.pk})


class CrmTaskStatus(models.Model):
    """Модель со статусами задачи"""
    status = models.CharField(verbose_name='название статуса', max_length=100)
    color = models.ForeignKey(
        'CrmColor',
        on_delete=models.SET_NULL,
        verbose_name='цвет',
        related_name='task_statuses',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'статус задачи'
        verbose_name_plural = 'статусы задач'

    def __str__(self):
        return self.status


class CrmTaskType(models.Model):
    """Модель с типами задачи"""
    type_task = models.CharField(verbose_name='название типа',
                                 max_length=100)
    color = models.ForeignKey(
        'CrmColor',
        on_delete=models.SET_NULL,
        verbose_name='цвет',
        related_name='task_types',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'тип задачи'
        verbose_name_plural = 'типы задач'

    def __str__(self):
        return self.type_task


class CrmDeal(models.Model):
    """Модель со сделками"""
    title = models.CharField(verbose_name='название', max_length=100)
    customer = models.ForeignKey(
        'CrmCustomer',
        on_delete=models.PROTECT,
        verbose_name='клиент',
        related_name='deals',
    )
    status = models.ForeignKey(
        'CrmDealStatus',
        on_delete=models.PROTECT,
        verbose_name='статус',
        related_name='deals',
    )

    class Meta:
        verbose_name = 'сделка'
        verbose_name_plural = 'сделки'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('crm:crm_deal_list')


class CrmDealStatus(models.Model):
    """Модель со статусами сделки"""
    status = models.CharField(verbose_name='название статуса', max_length=100)
    color = models.ForeignKey(
        'CrmColor',
        on_delete=models.SET_NULL,
        verbose_name='цвет',
        related_name='deal_status',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'статус сделки'
        verbose_name_plural = 'статусы сделок'

    def __str__(self):
        return self.status


class CrmOrder(models.Model):
    """Модель с заказами"""
    title = models.CharField(verbose_name='название', max_length=150)
    customer = models.ForeignKey(
        'CrmCustomer',
        on_delete=models.PROTECT,
        verbose_name='клиент',
        related_name='orders',
        blank=True,
        null=True,
    )
    status = models.ForeignKey(
        'CrmOrderStatus',
        on_delete=models.PROTECT,
        verbose_name='статус',
        related_name='orders',
        default=1,
    )

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('crm:crm_order_list')


class CrmOrderStatus(models.Model):
    """Модель со статусами заказа"""
    status = models.CharField(verbose_name='название статуса', max_length=100)
    color = models.ForeignKey(
        'CrmColor',
        on_delete=models.SET_NULL,
        verbose_name='цвет',
        related_name='order_status',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'статус заказа'
        verbose_name_plural = 'статусы заказов'

    def __str__(self):
        return self.status


class CrmColor(models.Model):
    """Цвета используемые в моделях модуля CRM"""
    title = models.CharField(verbose_name='название цвета', max_length=50)
    code_color = models.CharField(verbose_name='код цвета', max_length=100)

    class Meta:
        verbose_name = 'цвет в моделях'
        verbose_name_plural = 'цвета в моделях'

    def __str__(self):
        return self.title


class CrmAddressCountry(models.Model):
    title = models.CharField(verbose_name='назавние страны', max_length=100)

    class Meta:
        verbose_name = 'страна'
        verbose_name_plural = 'страны'

    def __str__(self):
        return self.title


class CrmAddressArea(models.Model):
    title = models.CharField(verbose_name='назавние области', max_length=100)

    class Meta:
        verbose_name = 'область'
        verbose_name_plural = 'области'

    def __str__(self):
        return self.title


class CrmAddressRegion(models.Model):
    title = models.CharField(verbose_name='название района', max_length=100)

    class Meta:
        verbose_name = 'район'
        verbose_name_plural = 'районы'

    def __str__(self):
        return self.title


class CrmAddressTown(models.Model):
    title = models.CharField(verbose_name='название города', max_length=100)

    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'города'

    def __str__(self):
        return self.title


class CrmAddressStreet(models.Model):
    title = models.CharField(verbose_name='название улицы', max_length=100)

    class Meta:
        verbose_name = 'улица'
        verbose_name_plural = 'улицы'

    def __str__(self):
        return self.title
