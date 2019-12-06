from secciones.users.models.users import Users
from secciones.users.serializers.users import usersSerializer
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from secciones.users.libs.encrypt import Encryption
class usersViewSet(viewsets.ModelViewSet):
    """ViewSet for the Usuarios class"""

    queryset = Users.objects.all()
    serializer_class = usersSerializer

 
    @action(detail = False, methods = ['get'])
    def loggedInUser(self, request):
        user = {}        
        if request.user.is_authenticated:
            
            user = usersSerializer(self.request.user).data
            return Response(user, status.HTTP_200_OK)

        return Response(user, status.HTTP_200_OK)


    def update(self, request, pk = None):
        #creo la instancia
        instance = self.get_object()
        data = request.data
        serializer = usersSerializer(instance, data = data)

        if "users" in data["profile_picture"]:
            data.pop("profile_picture") 

        if serializer.is_valid(raise_exception = True):
            serializer.save()
            
        return Response(status.HTTP_201_CREATED)


    @action(detail = False, methods = ['put'])
    def activateAccount(self, request):
        encodeSended = request.data["encodeUser"]
        username = Encryption.decrypt(encodeSended)
        print(username)
        if Users.objects.filter(username = username).exists():
            user = Users.objects.get(username = username)
            user.is_active = True 
            user.save()
            return Response(status.HTTP_200_OK)
        else:
            return Response(status.HTTP_404_NOT_FOUND)
