from django.urls import path

from . import views
from .views import VbRoundCreate

app_name = 'vbcourtassign'

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
    path('', VbRoundCreate.as_view(), name='vb'),
    path('results/', views.ResultsView, name='results'),
    # path('assignment/', views.court_assign, name='index'),
    path('assignment/', views.court_assign, name="court_assign"),
]
