from datetime import datetime, date, time
from django.shortcuts import render, get_object_or_404, reverse, redirect
from attendance.models import Status


# Create your views here.
def attend(request):
    status = Status.objects.order_by('-pk')[0]
    return render(request, 'attendance/attend.html', {'status': status})


def timecal(timedelt):
    if timedelt.days == -1:
        return (86400-timedelt.seconds)//60
    elif timedelt.days == 0:
        return -(timedelt.seconds//60 + 1)


def result(request, status_id):
    if request.method == 'POST':
        info = request.POST['name']
        status = get_object_or_404(Status, pk=status_id)

        at = datetime.now()
        ap = datetime.combine(date.today(), time(at.hour, at.minute))
        timed = status.status_time - ap

        status.comers_set.create(
            user_name=info,
            pub_date=ap,
            late_time=timecal(timed)
        )
        new_attend = status.comers_set.all
        return render(request, 'attendance/result.html', {'status': status, 'new_attend': new_attend})

    else:
        status = get_object_or_404(Status, pk=status_id)
        return render(request, 'attendance/result.html', {'status': status})


def state(request):
    if request.method == 'POST':
        name = request.POST['attend_name']
        times = time(int(request.POST['hour']), int(request.POST['minute']))
        new_status = Status(
            attend_name=name,
            status_time=datetime.combine(date.today(), times)
        )
        new_status.save()
        return redirect(reverse('attendance:result', kwargs={'status_id': new_status.id}))

    elif request.method == 'GET':
        return render(request, 'attendance/state.html')