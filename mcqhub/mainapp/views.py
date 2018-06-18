from django.shortcuts import render
from django.http import HttpResponse



from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *




# Create your views here.
def loginView(request):
    return render(request, "login.html")


def takeInput(request):
    mno = request.POST["mobilenum"]
    print(mno)
    return HttpResponse("hello")


class UserViewSet(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def get(self,request):
        queryset = Mcqdata.objects.all()
        serializer_class = McqSerializer(queryset, many=True)
        return Response(serializer_class.data)
