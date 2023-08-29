from django.db import models
from django.urls import reverse
from django.utils.functional import cached_property
# from django.utils import timezone

# Create your models here.
from volleyball import vb

class GeneralManager(models.Manager):
    def search(self, query):
        lookups = models.Q(title__icontains=query) | models.Q(content__icontains=query)
        return self.get_queryset().filter(lookups)


class Round(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    num_players = models.IntegerField(default=4, help_text="Enter the total number of players for this round.")
    non_exclusions = models.CharField(default="", blank=True, max_length=20, help_text='Enter field documentation')
    # pub_date = models.DateField(default=None, null=True, help_text="Round publish date.")
    _message = models.TextField(default=None, blank=True, null=True, help_text="The court assignment results.")
    # end = models.DateField(default=None, blank=True, null=True)

    # now = timezone.now()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Managers:
    # objects = RoundManager

    # Metadata
    class Meta:
        ordering = ['-created_at', '-num_players', 'non_exclusions']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        # return reverse('model-detail-view', args=[str(self.id)])
        return reverse("lets_play:detail", kwargs={"id": str(self.id)})

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return str(self.num_players)

    # @cached_property
    # def court_assignment(self):
    #     # template_name = 'lets_play/assignment.html'
    #     new_exclude, message = vb.main(int(self.num_players),
    #                                    self.non_exclusions)
    #     self.message = message

    @property
    def message(self):
        print(f"players: {int(self.num_players)}")
        print(f"non_exclusions: {self.non_exclusions}")
        new_excluded, message = vb.main(int(self.num_players),
                                        self.non_exclusions)
        print("model-results:")
        print(type(new_excluded), type(message))
        print(f"new_excluded: {new_excluded}")
        print(f"message: {message}")
        self._message = message
        # self._message = "test this"
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    # def activate_button(self):
    #     return format_html(
    #         '''<form action="activate/" method="POST">
    #                <button type="submit"> Activate </button>
    #             </form>''')