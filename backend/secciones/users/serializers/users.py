from secciones.users.models.users import Users
from rest_framework import serializers
from django.core.mail import send_mail
from django.conf import settings
from secciones.users.libs.encrypt import Encryption
from drf_extra_fields.fields import Base64ImageField

class usersSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, required=False) 
    profile_picture = Base64ImageField(required=False)
    class Meta:
        model = Users
        fields = (
            'pk', 
            'nickname', 
            'phone', 
            'first_name', 
            'last_name',
            'password',
            'profile_picture',
            'is_admin',
            'is_active'
        )



    def sendMail(self,data):
        user = Encryption.encrypt(data["username"])
        subject = 'Gracias por registrarte en theTherosNest'
        message = ' Haz click en el siguiente link para finalizar el registro: https://theterosnest.com/account/activate/?code={}'.format(user)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [data["username"],]
        send_mail( subject, message, email_from, recipient_list )

    def to_representation(self, instance):
        response = super(usersSerializer, self).to_representation(instance)
        if instance.profile_picture: 
            response['profile_picture'] = instance.profile_picture.url
        return response 
