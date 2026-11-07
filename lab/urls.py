from django.urls import path
from . import views
urlpatterns=[
 path('',views.dashboard,name='dashboard'),
 path('robots.txt',views.robots),
 path('hidden/backups/ops.txt',views.robot_secret),
 path('directory/',views.directory,name='directory'),
 path('directory/<int:employee_id>/',views.employee,name='employee'),
 path('archive/',views.archive,name='archive'),
 path('greeting/',views.greeting,name='greeting'),
 path('guestbook/',views.guestbook,name='guestbook'),
 path('staff/',views.staff,name='staff'),
 path('profile/',views.profile,name='profile'),
 path('vip/',views.vip,name='vip'),
 path('reset/',views.reset,name='reset'),
 path('api/profile/',views.profile_api),
 path('api/xss-proof/',views.xss_proof),
 path('api/submit/',views.submit_flag),
 path('api/progress/reset/',views.reset_progress),
]
