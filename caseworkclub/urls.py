from django.conf.urls import url
from caseworkclub.validators import membership_number_regex



from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'(?P<membership_number>'+membership_number_regex+r')',views.member,name='member'),
    url(r'^(?P<id>\d+)',views.caseview,name='caseview'),
    url(r'caseworker/(?P<pk>\d+)',views.CaseworkerView.as_view()),
]
