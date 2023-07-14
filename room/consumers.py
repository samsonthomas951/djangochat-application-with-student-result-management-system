import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Message, Room
from django.contrib.auth.models import User
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name=self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = "chat_%s" % self.room_name

        await self.channel_layer.group_add(
           self.room_group_name,
           self.channel_name 
        )

        await self.accept()
        
    async def disconnect(self,code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    async def receive(self, text_data):
        data= json.loads(text_data)
        message=data['message']
        username=data['username']
        room=data['room']
        self.user_id = self.scope['user'].id

        await self.save_message(username,room,message)
        
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'room':room,
                'user_id': self.user_id
            }
        )
    async def chat_message(self,event):
        message=event['message']
        username=event['username']
        room=event['room']
        user_id = event['user_id']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'room':room,
            'user_id': user_id
        }))
    @sync_to_async
    def save_message(self,username,room,message):
        user = User.objects.get(username=username)
        room = Room.objects.get(slug=room)
        Message.objects.create(user=user, room=room, content=message)
