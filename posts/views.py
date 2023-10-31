from django.shortcuts import render, redirect

# Create your views here.
def feeds(request):
    # user = request.user
    # is_authenticated = user.is_authenticated
    #
    # print("user", user)
    # print("is_authenticated", is_authenticated)

    if not request.user.is_authenticated:
        return redirect("/membership/login/")
    return render(request, "posts/feeds.html")