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

    Exit.objects.create(
        visitor_id=id,
        visitor_exit=vExitTime,
    )

    # if request.method == "GET":
    #     exit_visitor = request.GET(visitor=vExit)
    #     exit_visitor.save()

    context = {
        "carNumber": vCarNumber,
        "id": id,
        # "exit": vExitTime,
        "exit": Exit.objects.filter(visitor_id=id),
    }

    # vExit = Visitor.objects.get(id=id)
    #
    # if request.method == "POST":
    #     vExit.exit_time = timezone.now()  # 현재 시간으로 출차 시간 설정
    #     vExit.save()
    #     return redirect('your_redirect_view_name')  # 출차 후 리다이렉트할 뷰 이름으로 변경하세요
    #
    # context = {
    #     "visitor": vExit,
    # }
    return render(request, "visitor_exit.html", context)