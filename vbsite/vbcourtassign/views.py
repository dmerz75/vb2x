# Create your views here.
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import Http404
from django.template import loader
from django.utils import timezone
from django.views import generic


# Create your views here.
# from django.views.generic.edit import CreateView
from .models import VbRoundModel


class VbRoundCreate(generic.edit.CreateView):

    # specify the model for create view
    model = VbRoundModel

    # specify the fields to be displayed
    fields = ['num_players', 'non_exclusions']


class ResultsView(HttpRequest):
    model = VbRoundModel
    template_name = 'vbcourtassign/results.html'

    def get_queryset(self):
        """
        VbRoundModel ..
        """
        # return VbRoundModel.objects
        context = {'results': "test these results"}
        return render(HttpRequest, self.template_name, context)


def court_assign(request, vb_id):
    vbassigned = get_object_or_404(VbRoundModel, pk=vb_id)

    template_name = 'vbcourtassign/assignment.html'
    message = "the message from the test function!"
    context = {'message': message,
               'num_players': vbassigned.num_players,
               'non_exclusions': vbassigned.non_exclusions,
               }

    # try:
    #     selected_choice = vbassigned.objects.get(pk=request.POST['choice'])
    # except (KeyError, VbRoundModel.DoesNotExist):
    #     # Redisplay the question voting form.
    #     return render(request, template_name, {
    #         'message': "You didn't select a choice.",
    #     })
    # else:
    #     selected_choice.votes += 1
    #     selected_choice.save()
    #     # Always return an HttpResponseRedirect after successfully dealing
    #     # with POST data. This prevents data from being posted twice if a
    #     # user hits the Back button.

    # return HttpResponseRedirect(
    #     reverse('vbcourtassign:assignment', args=(vbassigned.id))
    #     )
    return render(request, template_name, context)




# def create(request, question_id):
#     assignment = get_object_or_404(VbRoundModel)

#     # Always return an HttpResponseRedirect after successfully dealing
#     # with POST data. This prevents data from being posted twice if a
#     # user hits the Back button.
#     return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
