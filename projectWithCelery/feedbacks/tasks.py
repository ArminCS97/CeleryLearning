from celery.schedules import crontab
from celery.task import periodic_task
from django.http import HttpResponse


@periodic_task(run_every=(crontab(minute='*/1')), name="some_task", ignore_result=True)
def some_task( request ):
    return HttpResponse("I am here")
