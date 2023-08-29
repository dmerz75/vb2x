# Create your views here.
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.http import Http404
from django.template import loader
from django.utils import timezone
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.views.generic.dates import WeekArchiveView
from django.views.generic import ListView


# Create your views here.
# from django.views.generic.edit import CreateView
from .models import Round
from .forms import RoundForm


class RoundView(generic.edit.CreateView):
    # specify the model for create view
    model = Round

    # specify the fields to be displayed
    fields = ['num_players', 'non_exclusions']

    template_name_suffix = "_create_form"


class RoundListView(ListView):
    model = Round
    context_object_name = "list_of_rounds"
    ordering = ['-created_at']


class RoundListViewLatest(ListView):
    model = Round
    # context_object_name = "list_of_rounds"
    # ordering = ['-created_at']
    my_rounds = Round.objects.latest("created_at")
    # my_round = my_rounds[-1]

    def get_latest(self, request):
        context = {
            'round': self.my_round
        }
        return render(request, "lets_play/round_list.html", context)


@login_required
def round_create_view(request):
    form = RoundForm(request.POST or None)

    context = {
        'form': form
    }

    if form.is_valid():
        obj = form.save()
        obj.user = request.user
        obj.save()
        form = RoundForm()
        # redirect??
        context = {
            'form': form,
            'id': obj.id
        }
        return redirect(f"/lets_play/{obj.id}/")

    return render(request, "lets_play/round_create_view.html", context)

@login_required
def round_update_view(request, id=None):
    obj = get_object_or_404(Round, id=id, user=request.user)
    form = RoundForm(request.POST or None, instance=obj)
    context = {
        'form': form,
        'object': obj
    }
    if form.is_valid():
        form.save()
        form = RoundForm()
        context["status"] = "round updated."

    return render(request, "lets_play/round_create_view.html", context)
    # return render(request, "lets_play/round/detail.html", context)

@login_required
def round_list_view(request):
    qs = Round.objects.filter(user=request.user)
    context = {
        "object_list": qs
    }
    return render(request, "lets_play/round/list.html", context)

@login_required
def round_detail_view(request, id=None):
    # TODO: use user
    # obj = get_object_or_404(Round, id=id, user=request.user)

    context = {}

    if request.method == "GET":
        obj = Round.objects.get(pk=id)
        context = {
            "round": obj
        }
        return render(request, "lets_play/round/detail.html", context)

    elif request.method == "POST":
        return redirect("/lets_play/create/")

    return render(request, "lets_play/round/detail.html", context)






# class CreateRound(generic.edit.CreateView):

#     # specify the model for create view
#     model = Round

#     # specify the fields to be displayed
#     fields = ['num_players', 'non_exclusions']

#     def get(self, request):
#         return HttpResponse("Get")

#     def post(self, request):
#         return HttpResponse("Post")

#     @classmethod
#     def create(cls, n, e):
#         round = cls(int(n), e)
#         # do something with the book
#         return round



def index(request):
    return render(request, "lets_play/index.html", {
        "form": RoundForm,
    })
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


# def index(request, round):
#     round = Round.objects.order_by("-pub_date")
#     context = {
#         "latest_question_list": latest_question_list
#         "num_players": round.num_play
#     }
#     return render(request, "polls/index.html", context)
# def assignment(generic.edit.CreateView):





# def round_generate(request):
#     if request.method == "POST":
#         new_round = RoundForm



# def successpage(request):
#     data = request.POST.get('submit1')
#     context = {'data': data}
#     return render(request, 'lets_play/round_list.html', context)

# def members(request):
#     return HttpResponse("Hello world!")


# https://docs.djangoproject.com/en/3.0/ref/class-based-views/generic-date-based/#django.views.generic.dates.YearArchiveView
class RoundWeekArchiveView(WeekArchiveView):
    queryset = Round.objects.all()
    date_field = "created_at"
    week_format = "%W"
    allow_future = True
