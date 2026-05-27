from django.shortcuts import get_object_or_404, redirect

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('/')
