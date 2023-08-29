# Create your models here.

# import the standard Django Model
# from built-in library
from django.db import models
from django.contrib.postgres.search import SearchQuery
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render


from volleyball import vb


# declare a new model with a name "GeeksModel"
class VbRoundModel(models.Model):

    # fields of the model
    num_players = models.IntegerField()
    non_exclusions = models.TextField()

    # def __init__(self):
    #     pass
    #     # self._assign_courts()

    # non_exclusions_str = non_exclusions.value_from_object.__str__()

    # if non_exclusions_str.contains(","):
    #     non_excluded = non_exclusions_str.split(",")
    # else:
    #     non_excluded = non_exclusions_str.split(" ")

    # renames the instances of the model
    # with their title name
    def __int__(self):
        return self.num_players

    # def __str__(self):
    #     return self.non_exclusions

    # def __str__(self):
    #     return self.non_excluded

    def _assign_courts(self):
        template_name = 'vbcourtassign/assignment.html'
        # self.non_excluded = self.non_exclusions.split(',')
        self.non_excluded = self.non_exclusions
        new_exclude, message = vb.main(int(self.num_players),
                                       self.non_excluded)

        # vbassigned = get_object_or_404(VbRoundModel, pk=vb_id)
        # template_name = 'vbcourtassign/assignment.html'
        message = "the message from the test function!"
        context = {
            "message": message,
            "num_players": self.num_players,
            "non_exclusions": self.non_exclusions,
        }
        return render(HttpResponse, template_name, context)




class Choice(models.Model):
    num_players = models.ForeignKey(VbRoundModel, on_delete=models.CASCADE)
    non_exclusions = models.CharField(max_length=200)

    # def __str__(self):
    #     return self.num_players
    def __str__(self):
        return self.non_exclusions
