from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Timesheet


# =========================
# DASHBOARD (ROLE + TEAM FILTER)
# =========================
@login_required
def dashboard(request):

    team_filter = request.GET.get("team")

    if request.user.is_superuser:
        tasks = Timesheet.objects.all()

        # 👇 TEAM FILTER FOR MANAGER
        if team_filter:
            tasks = tasks.filter(team=team_filter)

    else:
        tasks = Timesheet.objects.filter(user=request.user)

    total_hours = sum(float(t.hours) for t in tasks)

    return render(request, 'dashboard.html', {
        'tasks': tasks,
        'total_hours': total_hours
    })


# =========================
# ADD TASK (TEAM ADDED FIX)
# =========================
@login_required
def add_task(request):
    if request.method == "POST":

        dates = request.POST.getlist('date')
        tasks = request.POST.getlist('task')
        start_times = request.POST.getlist('start_time')
        hours_list = request.POST.getlist('hours')
        comments_list = request.POST.getlist('comments')
        teams_list = request.POST.getlist('team')   # ✅ NEW

        for i in range(len(tasks)):
            if tasks[i]:

                start_time = start_times[i] if i < len(start_times) else None
                if start_time == "":
                    start_time = None

                Timesheet.objects.create(
                    user=request.user,
                    team=teams_list[i] if i < len(teams_list) else "HR",   # ✅ NEW
                    date=dates[i],
                    task=tasks[i],
                    start_time=start_time,
                    hours=hours_list[i] if hours_list[i] else 0,
                    comments=comments_list[i] if i < len(comments_list) else "",
                )

        return redirect('dashboard')

    return render(request, 'add_task.html')


# =========================
# DELETE TASK (SAFE)
# =========================
@login_required
def delete_task(request, task_id):

    task = get_object_or_404(Timesheet, id=task_id)

    # 👨‍💼 manager OR owner can delete
    if request.user.is_superuser or task.user == request.user:
        task.delete()

    return redirect('dashboard')


# =========================
# LOGOUT
# =========================
def logout_view(request):
    logout(request)
    return redirect('login')
