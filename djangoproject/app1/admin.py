from django.contrib import admin
from app1.models import Worker
from app1.models import User
from app1.models import News
from app1.models import Product
from app1.models import Chat
from app1.models import Message


# Register your models here.


admin.site.register(Worker)
admin.site.register(User)
admin.site.register(Product)
admin.site.register(News)
admin.site.register(Message)
admin.site.register(Chat)
