# from datetime import datetime
from datetime import timedelta

from django.shortcuts import render, redirect, get_object_or_404
from visitor.models import Visitor, Exit
from django.utils import timezone


# Create your views here.
def main(request):
    return render(request, "main.html")

def visitor_list(request):
    vList = Visitor.objects.all()
    # print("visitor-list:", vList)

    context = {
        "visitors": vList,
    }
    return render(request, "visitor_list.html", context)

def visitor_search(request):
    keyword = request.GET.get("keyword")

    if keyword is not None:
        vSearch = Visitor.objects.filter(carNumber__contains=keyword)

    else:
        vSearch = Visitor.objects.none()

    context = {
        "visitors": vSearch,
    }

    return render(request, "visitor_search.html", context)

def visitor_add(request):
    if request.method == "POST":
        carNumber = request.POST["carNumber"]
        name = request.POST["name"]
        address = request.POST["address"]
        phoneNumber = request.POST["phoneNumber"]
        # carIn = request.POST["carIn"]
        Visitor.objects.create(
            carNumber=carNumber,
            name=name,
            address=address,
            phoneNumber=phoneNumber,
            carIn=timezone.now(),
        )
        return redirect(f"/visitor/list/")

    else:
        print("method GET")
    return render(request, "visitor_add.html")

def visitor_detail(request, visitor_id):
    vDetail = Visitor.objects.get(id=visitor_id)
    vCarNumber = vDetail.carNumber
    vName = vDetail.name
    vAddress = vDetail.address
    vPhoneNumber = vDetail.phoneNumber
    vCarIn = vDetail.carIn
    # vCarExit = vDetail.visitor_exit

    context = {
        "id": visitor_id,
        "visitors": vDetail,
        "carNumber": vCarNumber,
        "name": vName,
        "address": vAddress,
        "phoneNumber": vPhoneNumber,
        "carIn": vCarIn,
        # "carExit": vCarExit,
    }

    return render(request, "visitor_detail.html", context)

def visitor_exit(request, id):
    # id = request.GET.get("keyword")
    print(f'========================>{id}')
    vExit = Visitor.objects.get(id=id)

    vCarNumber = vExit.carNumber
    vExitTime = timezone.now()
    vCarIn = vExit.carIn

    fee = fee_settlement(vCarIn, vExitTime)

    Exit.objects.create(
        visitor_id=id,
        visitor_exit=vExitTime,
    )

    context = {
        "carNumber": vCarNumber,
        "id": id,
        # "exit": vExitTime,
        "carIn": vCarIn,
        "exit": Exit.objects.filter(visitor_id=id),
        "fee": fee,
    }

    return render(request, "visitor_exit.html", context)

def fee_settlement(carIn, carExit):
    defult_fee = 10000
    defult_time = timedelta(minutes=30)
    ten_minutes = timedelta(minutes=10)
    ten_fee = 1500
    two_day = timedelta(days=2)

    if carExit:
        fee_time = carExit - carIn
        if fee_time == defult_time:
            fee = defult_fee
            return fee
        elif fee_time > defult_time:
            fee = ((fee_time - defult_time) / ten_minutes) * ten_fee + defult_fee
            if 20000 <= fee < 30000:
                fee = fee * 0.9
                return fee
            elif fee >= 30000:
                fee = 30000
            return fee
        else:
            return "Free"

    else:
        return "None"

