# from django.db import models
#
# from django.conf import settings
#
# # Create your models here.
#
#
# class Actor(models.Model):
#     Actor_Id = models.CharField(max_length=100, auto_created=True)
#     #Actor_Rating = models.ForeignKey(ActorRating, related_name='actors_rating', on_delete=models.CASCADE)
#     Actor_Body_Type = models.TextField(max_length=100)
#     #comment = models.ForeignKey(comments, related_name='actors', on_delete=models.CASCADE)
#     Actor_Description = models.TextField(max_length=100)
#     Actor_Ethnicity = models.TextField(max_length=100)
#     Actor_Eye_Color = models.TextField(max_length=100)
#     Actor_Favorite_Acting_Styles = models.TextField(max_length=100)
#     Actor_Height =models.CharField(max_length=100)
#     #language = models.ForeignKey(languages,related_name='actors',on_delete=models.CASCADE)
#     #portfolio= models.ForeignKey(portfolios,related_name='actors',on_delete=models.CASCADE)
#     #profileproject = models.ForeignKey(profileprojects, related_name='actors',on_delete=models.CASCADE)
#     Actor_Rates = models.PositiveIntegerField()
#     Actor_SceneComfort = models.TextField(max_length=100)
#     ACTOR_Skin_Color = models.TextField(max_length=100)
#     Actor_Smoker = models.BooleanField()
#     Actor_Alcoholic = models.BooleanField()
#
#     #special_skill = models.ForeignKey(special_skills, related_name='actors',on_delete=models.CASCADE)
#
#     #video = models.ForeignKey(videos,related_name='actors',on_delete=models.CASCADE)
#     Actor_Weight = models.CharField(max_length=100)
#     #creator = models.ForeignKey(User, related_name='actors',on_delete=models.CASCADE)
#     Actor_Created_Date = models.DateTimeField(auto_now_add=True, auto_now=False)
#     Actor_Updated_Date = models.DateTimeField(auto_now=True)
#
#
# class ActorRating(models.Model):
#     Rating = models.PositiveSmallIntegerField(blank=True, null=True)
#     #Given_By = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, null=False)
#     #Given_To = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False)

