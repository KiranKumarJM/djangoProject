from django.http import HttpResponse
from django.template import loader
from rest_framework.response import Response
from rest_framework.views import APIView

from login.models import Users
from login.serializers import UsersSerializer


def index(request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render())

#def home(reqest):
 # return HttpResponse("Hello world!")

class userList(APIView):
    def get(self, request):
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)