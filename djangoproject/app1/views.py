from django.shortcuts import render
from app1.models import Worker
from app1.models import User
from app1.models import News
from app1.models import Product
from app1.models import Chat
from app1.models import Message
from app1.models import getToken
from django.http import JsonResponse
import datetime


def index_page(request):
    #  new_worker = Worker(firstNM='Sidor', secondNM='Fedorovich', salary=300)
    #  new_worker.save()

    worker_to_change = Worker.objects.get(id=5)
    worker_to_change.secondNM = 'NewSecondName'
    worker_to_change.save()
    print(worker_to_change)

    all_workers = Worker.objects.all()
    filter_workers = Worker.objects.filter(salary=123)

    print("All: ", all_workers)
    print("Filter: ", filter_workers)

    workArr = []
    for item in all_workers:
        print(f'ID: {item.id}  '
              f'Фамилия: {item.firstNM} '
              f'Имя: {item.secondNM} '
              f'ЗП:{item.salary}')
        workArr.append([item.id, item.firstNM, item.secondNM, item.salary])

    return render(request, 'index.html', {'data': 5, 'dataArr': workArr})


def index_form(request):
    if request.method == 'POST':
        login = request.POST['user']
        password = request.POST['pass']
        flag = User.objects.filter(login=login,
                                   password=password)
        if len(flag) == 0:
            return JsonResponse({"name": login,
                                 "flag": False,
                                 "token": 0})
        elif len(flag) == 1:
            user = User.objects.get(login=login)
            user.token = getToken(login)
            user.save()
            return JsonResponse({"name": login,
                                 "flag": True,
                                 "token": getToken(login)})
    return render(request, 'form/index.html')


def index_news(request):
    if request.method == 'POST':
        if request.POST['type'] == "add":
            news = News(name=request.POST['name'],
                        photoLink=request.POST['photoLink'],
                        description=request.POST['description'],
                        date=str(datetime.datetime.now())[:19],  # request.POST['date']
                        type=int(request.POST['newsType']),
                        userId=int(request.POST['userid']))
            news.save()
            return JsonResponse({"newsName": news.name, "date": news.date})
        elif request.POST['type'] == "get":
            newsId = -1
            if request.POST['newsId'] != "":
                newsId = int(request.POST['newsId'])
            newsName = request.POST['name']
            if News.objects.filter(id=newsId):
                newsObject = News.objects.get(id=newsId)
                newsObject.save()
                return JsonResponse({"name": newsObject.name,
                                     "photoLink": newsObject.photoLink,
                                     "date": newsObject.date,
                                     "type": newsObject.type,
                                     "userId": newsObject.userId})
            else:
                newsObject = News.objects.get(name=newsName)
                newsObject.save()
                return JsonResponse({"name": newsObject.name,
                                     "photoLink": newsObject.photoLink,
                                     "date": newsObject.date,
                                     "type": newsObject.type,
                                     "userId": newsObject.userId})
    return render(request, 'news/index.html')


def index_product(request):
    if request.method == 'POST':
        if request.POST['type'] == "add":
            product = Product(name=request.POST['name'],
                              photoLink=request.POST['photoLink'],
                              speed=request.POST['speed'],
                              description=request.POST['description'],
                              userId=int(request.POST['userId']),
                              price=int(request.POST['price']),
                              articleNumber=int(request.POST['articleNumber']),
                              flightTime=int(request.POST['flightTime']),
                              range=int(request.POST['range']),
                              weight=int(request.POST['weight']),
                              maxWind=int(request.POST['maxWind']),
                              maxAltitude=int(request.POST['maxAltitude']),
                              minAltitude=int(request.POST['minAltitude']),
                              motorsNumber=int(request.POST['motorsNumber']))
            product.save()
            return JsonResponse({"productName": product.name,
                                 "price": product.price})
        elif request.POST['type'] == "get":
            productId = -1
            if request.POST['productId'] != "":
                productId = int(request.POST['productId'])
            productName = request.POST['name']
            if Product.objects.filter(id=productId):
                productObject = Product.objects.get(id=productId)
                productObject.save()
                return JsonResponse({"name": productObject.name,
                                     "photoLink": productObject.photoLink,
                                     "price": productObject.price,
                                     "range": productObject.range,
                                     "speed": productObject.speed})
            else:
                productObject = Product.objects.get(name=productName)
                productObject.save()
                return JsonResponse({"name": productObject.name,
                                     "photoLink": productObject.photoLink,
                                     "date": productObject.date,
                                     "type": productObject.type,
                                     "userId": productObject.userId})
    return render(request, 'product/index.html')


def index_register(request):
    if request.method == 'POST':
        login = request.POST['log']
        password = request.POST['pass']
        role = request.POST['role']

        if len(User.objects.filter(login=login)) == 0:
            new_user = User(login=login,
                            password=password,
                            userRole=role,
                            token=getToken(login))
            new_user.save()
            print(f"New User: {login}")
            return JsonResponse({"name": login,
                                 "flag": True,
                                 "token": getToken(login)})
        else:
            print(f"User in the DB: {login}")
            return JsonResponse({"result": 'Error',
                                 "type": 'User already exists'})
    return render(request, 'register/index.html')


def index_chat(request):
    if request.method == 'POST':
        actionType = request.POST['actionType']
        firstUserLogin = request.POST['firstUserLogin']
        token = request.POST['token']
        flag = len(User.objects.filter(token=token))
        print(User.objects.filter(token=token))
        print(flag, firstUserLogin, token)
        if flag == 1:
            if actionType == "createChat":
                secondUserLogin = request.POST['secondUserLogin']
                chatTitle = request.POST['chatTitle']
                status = int(request.POST['status'])
                fun = User.objects.get(login=firstUserLogin).firstNM
                sun = User.objects.get(login=secondUserLogin).firstNM
                new_chat = Chat(firstUserLogin=firstUserLogin,
                                secondUserLogin=secondUserLogin,
                                status=status,
                                chatTitle=chatTitle,
                                firstUserName=fun,
                                secondUserName=sun,
                                chatName=fun+sun)
                new_chat.save()
                return JsonResponse({"opponentName": new_chat.secondUserName,
                                     "Id": new_chat.id})
            elif actionType == "getChats":
                res = Chat.objects.filter(firstUserLogin=firstUserLogin)
                ans = {}
                for chat in res:
                    ans[chat.chatName] = {"chatName": chat.chatName,
                                          "firstUserLogin": chat.firstUserLogin,
                                          "secondUserLogin": chat.secondUserLogin,
                                          "chatTitle": chat.chatTitle,
                                          "status": chat.status}
                return JsonResponse(ans)
            elif actionType == "getChatMessages":
                chatName = request.POST['chatName']
                res = Message.objects.filter(chatName=chatName)
                ans = {}
                for i in range(len(res)):
                    message = res[i]
                    ans[message.chatName + "_" + str(i)] = {
                        "text": message.text,
                        "date": message.date,
                        "userLogin": message.userLogin}
                return JsonResponse(ans)
            elif actionType == "sendMessage":
                chatName = request.POST['chatName']
                text = request.POST['text']
                date = str(datetime.datetime.now())[:19]
                message = Message(text=text,
                                  date=date,
                                  chatName=chatName,
                                  userLogin=firstUserLogin)
                message.save()
                return JsonResponse({"text": text,
                                     "date": date})
        else:
            return JsonResponse({"result": 'Error',
                                 "type": 'Chat append error'})
    return render(request, 'message/index.html')
