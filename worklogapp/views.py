from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import TimeSheet


# ✅ HOME PAGE (FIX YOUR ERROR)
@login_required
def home(request):
    timesheets = TimeSheet.objects.filter(user=request.user).order_by("-date")
    return render(request, "home.html", {"timesheets": timesheets})


# ✅ CREATE TIMESHEET
@login_required
def create_timesheet(request):
    if request.method == "POST":

        dates = request.POST.getlist("date")
        hours = request.POST.getlist("hours")
        descriptions = request.POST.getlist("description")

        for i in range(len(dates)):
            if dates[i] and hours[i]:
                TimeSheet.objects.create(
                    date=dates[i],
                    hours=float(hours[i]),
                    description=descriptions[i] if descriptions[i] else "",
                    user=request.user
                )

        return redirect("home")

    return render(request, "create_timesheet.html")


# ✅ DELETE TIMESHEET
@login_required
def delete_timesheet(request, id):
    obj = get_object_or_404(TimeSheet, id=id, user=request.user)
    obj.delete()
    return redirect("home")
