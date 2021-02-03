from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django import forms


def user_partition(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename) # new: id, included in ForeignKey

class Composer(models.Model):

    COMPOSER_OCCUPATION = (
        ('CO', 'Compositeur'),
        ('TE' , 'Enesignant'),
        ('SC', 'Musicien de scène'),
        ('PS', 'Etudiant professionnel'),
        ('YS', 'Jeune étudiant'),
        ('AM', 'Amateur de musique'),
        ('AL', 'Algorythme de composition'),
        ('OT', 'Autre'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    composerName = models.CharField(max_length=100) #firstname/last name <---- --> changer

    composerOccupation = models.CharField(max_length=2, choices=COMPOSER_OCCUPATION)    #optionnel
    experience = models.DateField(auto_now_add=False) #optionel


class TheoryComment(models.Model):
    COMMENT_TYPE = (('LC', 'Comment about level'),
    ('TC', 'Comment about general technique'),)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    theorytype = models.CharField(max_length=2, choices=COMMENT_TYPE)

class MusicScore(models.Model):

    titrescore = 'Le titre de la pièce'
    # to make a scroll menu??
    
    SCORE_TYPE = (
        ('PI', 'Piece'),
        ('MS', 'Gamme mélodique'),
        ('HS', 'Gamme harmonique'),
        ('CS', 'Gamme en accords'), 
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    scorefile = models.FileField(upload_to=user_partition, null=False, unique=True) # != upload_to='upload/' caus I'd like to have this rep name.
    scoretype = models.CharField(max_length=2, choices=SCORE_TYPE) #ok
    scoretitle = models.CharField(max_length=100)
    scorecollection = models.CharField(max_length=100, blank=True, null=True)
    scoredate = models.DateTimeField(auto_now_add=True)
    readlevel = models.PositiveIntegerField(default=1) # up to level 10 (or more)
    # scorenote = models.CharField(blank=True, null=True, widget=forms.TextInput(attrs={'placeholder': 'Inscrire une note au sujet de la composition'})) #placeholder for textfield <----
    moderatorok = models.BooleanField(default=False) # also, not available to users
    mechanicalrights = models.BooleanField(default=False)   #if True, go to 'Rights' page, fift floor...
    #right model?
    downloadOrWatch = models.BooleanField(default=False)

    def publier(self):
        self.publish_date = timezone.now()
        self.save()
#avec erreur: django no such table,        
#>py manage.py migrate --run-syncdb #et enregistre
    def __str__(self):
        return self.scoretitle


        # def scoresubmit(self):
#     self.scoredate = timezone.now() #but it is different than composition date...
#     self.save()# done automatically
# !!!!--->>>> https://docs.djangoproject.com/en/3.1/ref/models/fields/#field-options
# def is_upperclass(self):
#        return self.year_in_school in {self.JUNIOR, self.SENIOR}