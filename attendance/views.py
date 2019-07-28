from datetime import datetime, timezone
from django.shortcuts import render, get_object_or_404
from attendance.models import Status
from django.utils.timesince import timesince


# Create your views here.
def attend(request):
    status = Status.objects.order_by('-pk')[0]
    return render(request, 'attendance/attend.html', {'status': status})


def result(request, status_id):
    info = request.POST['name']
    status = get_object_or_404(Status, pk=status_id)
    status.comers_set.create(user_name=info, pub_date=datetime.now())
    # gap = str(datetime.now() - status.status_time)
    new_attend = status.comers_set.all
    return render(request, 'attendance/result.html', {'status': status, 'new_attend': new_attend})