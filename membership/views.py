from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from membership.forms import LoginForm, SignupForm

# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        # return redirect("/posts/feeds/")
        return redirect("/visitor/list/")

    if request.method == "POST":
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                # return redirect("/posts/feeds/")
                return redirect("/visitor/list/")
            else:
                form.add_error(None, "입력한 자격증명에 해당하는 사용자가 없습니다")

        context = {
            "form": form,
        }
        return render(request, "membership/login.html", context)
    else:
        form = LoginForm()
        context = {"form": form}
        return render(request, "membership/login.html", context)

def logout_view(request):
    logout(request)
    return redirect("/membership/login/")

def signup(request):
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
    form = SignupForm()

    context = {"form": form}
    return render(request, "membership/signup.html", context)

def delete(request):
    return render(request, "membership/delete.html")

def my_page(request):
    return render(request, "membership/my_page.html")
