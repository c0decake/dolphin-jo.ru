import json

from channels.generic.websocket import AsyncWebsocketConsumer

from .signals import get_actual_orders


class AllOrderConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add('orders_group', self.channel_name)
        await self.send(text_data=json.dumps({
            'type': 'status',
            'status': "Соединение установлено"
        }))

        await self.send_orders({
            'type': 'orders',
            'orders': await get_actual_orders()
        })

    async def disconnect(self, code):
        await self.channel_layer.group_discard('orders_group', self.channel_name)

    async def send_orders(self, event):
        await self.send(text_data=json.dumps({
            'type': 'orders',
            'orders': event['orders']
        }))
