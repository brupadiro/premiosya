from secciones.users.models.users import Users
from rest_framework import serializers


class usersSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    class Meta:
        model = Users
        fields = (
            'pk',
            'nickname',
            'username',
            'email',
            'password',
            'is_admin'
        )

    def create(self, data):
        user = Users()
        user.username = data["username"]
        user.nickname = data["nickname"]
        user.is_admin = False
        user.is_active = True
        user.phone = data["email"]
        user.set_password(data["password"])
        user.save()
        return user
