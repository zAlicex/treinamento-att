from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='midia/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    empresa = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.username} - {self.empresa}'

class VideoProgress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pilar_watched = models.BooleanField(default=False)
    equipamento_watched = models.BooleanField(default=False)
    insercao_watched = models.BooleanField(default=False)
    plataforma_watched = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s Progress"

# Sinal para criar um perfil de usuário e progresso de vídeo automaticamente quando um User é criado
@receiver(post_save, sender=User)
def create_user_profile_and_progress(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)
        VideoProgress.objects.get_or_create(user=instance)

# Sinal para salvar o perfil de usuário e progresso sempre que o User for salvo
@receiver(post_save, sender=User)
def save_user_profile_and_progress(sender, instance, **kwargs):
    # Verifica e salva apenas se os objetos existirem, evitando erros no admin
    if hasattr(instance, 'userprofile'):
        instance.userprofile.save()
    if hasattr(instance, 'videoprogress'):
        instance.videoprogress.save()
