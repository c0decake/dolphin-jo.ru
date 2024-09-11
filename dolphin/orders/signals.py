from datetime import date, time

from asgiref.sync import async_to_sync
from asgiref.sync import sync_to_async
from channels.layers import get_channel_layer
from django.db.models import F
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Orders


@sync_to_async
def get_actual_orders():
    orders = Orders.objects.annotate(address=F('shop__address'),
                                     district=F('shop__district__name'),
                                     city=F('shop__district__city__name'),
                                     post_name=F('post__name')).values()
    orders_data = [
        {
            k: v.strftime("%d.%m.%Y") if isinstance(v, date) else v.strftime("%H:%M") if isinstance(v, time) else v
            for k, v in order.items()
        } for order in orders
    ]
    return orders_data


@receiver([post_save, post_delete], sender=Orders)
def send_order_update(sender, instance, **kwargs):
    orders = async_to_sync(get_actual_orders)()
    async_to_sync(get_channel_layer().group_send)(
        'orders_group',
        {
            'type': 'send_orders',
            'orders': orders
        }
    )
