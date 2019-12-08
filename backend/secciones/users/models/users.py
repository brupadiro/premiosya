from django.urls import reverse
from django.db.models import CharField
from django.db.models import EmailField
from django.db.models import IntegerField
from django.db import models
from django.contrib.auth.models import AbstractUser
from Crypto.Cipher import AES
from django.conf import settings
from Crypto import Random
from PIL import Image
import os

from secciones.apuestas.models.apuesta import Apuesta


class Users(AbstractUser):

    phone = models.IntegerField()
    nickname = models.CharField(max_length=150, null=True, blank=True)
    is_admin = models.BooleanField(
        'is_admin',
        default=False
    )
    is_active = models.BooleanField(
        'is_active',
        default=False
    )
    
    apuesta = models.ForeignKey(Apuesta, verbose_name=_("apuesta"), on_delete=models.CASCADE)

    USERNAME_FIELD = 'username'
    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('usuarios_usuarios_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('usuarios_usuarios_update', args=(self.pk,))

    """
    def save(self, *args, **kwargs):
        size = 300, 300
        try:
            id_user = Users.objects.latest('pk').pk + 1
        except:
            id_user = 1
        if os.path.isdir(os.path.join(settings.MEDIA_ROOT +'/users/{}'.format(id_user))) is False:
            os.mkdir(os.path.join(settings.MEDIA_ROOT +'/users/{}'.format(id_user)))
        if self.profile_picture and 'users' not in self.profile_picture.url:
            im = Image.open(self.profile_picture)
            new = Image.new('RGBA', size, (255, 255, 255, 0))  #with alpha
            im.thumbnail(size)
            new.paste(im,(int((size[0] - im.size[0]) / 2), int((size[1] - im.size[1]) / 2)))
            new.save('uploads/users/{}/{}.png' .format( id_user, self.profile_picture.name[:-4]),'PNG')
            self.profile_picture = 'users/{}/{}.png'.format( id_user, self.profile_picture.name[:-4])


        super(Users, self).save(*args, **kwargs)
    """