from django.urls import include, path
from django.contrib import admin
from django.views.generic.dates import ArchiveIndexView
from .models import Round
# from .views import RoundWeekArchiveView

from . import views
# from .views import CreateRound, RoundListView

from lets_play.views import (
    index,
    round_create_view,
    round_detail_view,
    round_list_view,
    round_update_view,
    RoundView,
    RoundListView,
    RoundListViewLatest,
)

app_name = 'lets_play'

# urlpatterns = [
#     path('', views.index, name='polls'),

#     # ex: /polls/
#     path('', views.index, name='index'),
#     # ex: /polls/5/
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]

# urlpatterns = [
#     path('', views.IndexView.as_view(), name='index'),
#     # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
#     # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
#     # path('<int:question_id>/vote/', views.vote, name='vote'),
# ]

urlpatterns = [
    path('', index, name="index"),
    # path('', RoundCreate.as_view(), name='vb'),
    path('input/', RoundView.as_view(),),

    path('list/', round_list_view, name="list"),
    path('create/', round_create_view, name="create"),
    path('<int:id>/edit/', round_update_view, name="update"),
    path('<int:id>/', round_detail_view, name="detail"),

    path('latest/', RoundListViewLatest.get_latest,),
    # path('createround/', views.CreateRound.as_view(template_name="lets_play/create_round.html")),
    # path('round/add',
    #      views.CreateRound.create,
    #      name="create-round"),
    path('roundlist/', views.RoundListView.as_view(), name='roundlist'),
    # path('index', views.new_round.as_view(template_name="lets_play/ "))
    # path('members/', views.members, name='members'),
    path('members', include('members.urls')),
    path('admin/', admin.site.urls),
    # Example: /2012/week/23/
    # path('<int:year>/week/<int:week>/',
    #      RoundWeekArchiveView.as_view(),
    #      name="archive_week"),
    # path('results/', views.ResultsView, name='results'),
    # path('assignment/', views.court_assign, name='index'),
    # path('assignment/', , name="court_assign"),
]
