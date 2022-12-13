from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *
from django.core.mail import send_mail
import uuid
from project.settings import EMAIL_HOST_USER
from rest_framework.decorators import api_view
from rest_framework import status



class ReactView(APIView):


    # serializer_class = UserSerializer
    # def get(self, request):
    #     output = [{"username": output.username, "fname": output.fname,"lname": output.lname,"password": output.password,"email": output.email,"phone": output.phone,"country": output.country,"DOB": output.DOB,}
    #               for output in userdata.objects.all()]
    #     return Response(output)
    
        # @api_view(['POST',])
        def post(self, request):
            try:    
                if request.method=="POST": 
                        data = request.POST.dict()
                        email=data['email']
                        token=uuid.uuid4()  
                        ver=verification_data()
                        ver.email=email
                        ver.token=token
                        ver.verified=False
                        ver.save()
                        serializer = UserSerializer(data=data)
                        print(serializer.is_valid())
                        if serializer.is_valid():
                            serializer.save()
                            send_mail(
                                    subject='DeBugHive Verification Mail',
                                    message=f'Click on the link to verify your account... http://localhost:3000/account-verified/{token}',
                                    from_email=EMAIL_HOST_USER,
                                    recipient_list=[email,],
                                            )   
                            return Response(status=status.HTTP_200_OK)
                        else:
                            return Response(status=status.HTTP_400_BAD_REQUEST)
                else:
                        return Response(status=status.HTTP_404_NOT_FOUND)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
class account_verified(APIView):
    def post(self,request):
        if request.method=='POST':
            data=request.POST.dict()
            token=data['token']
            pf=verification_data.objects.filter(token=token).first()
            pf.verified=True
            pf.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class SIGNIN(APIView):
    def post(self,request):
        if request.method=='POST':
            data=request.POST.dict()
            username=data['username']
            hi=userdata.objects.filter(username=username).first()
            log=logindata()
            log.username=hi.username
            log.fname=hi.fname
            log.lname=hi.lname
            log.save()
            if hi.password==data['password']:
                return Response(status=status.HTTP_200_OK)
     
            return Response(status=status.HTTP_404_NOT_FOUND)

class GETUSER(APIView):
    def get(self,request):
        if request.method=='GET':
            output=[{"username":output.username,
            "fname":output.fname,"lname":output.lname
            }for output in logindata.objects.filter()[:1]
            ]
            return Response(output)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

class GETSCORE(APIView):
    def get(self,request):
        if request.method=='GET':
            output=[{"username":output.username,"score":output.scores
            }for output in scoredata.objects.filter()[:5]]
            return Response(output)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

class GETTASK(APIView):
    def get(self,request):
        if request.method=='GET':
            output=[{"name":output.name,"score":output.scores,"date":output.date
            }for output in taskdata.objects.filter()[:3]]
            return Response(output)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class Forgotpassword(APIView):
    def post(self,request):
        if request.method=='POST':
            data=request.POST.dict()
            username=data['username']
            hi=userdata.objects.filter(username=username).first()
            if hi.password==data['password']:
                hi.password=data['npassword']
                hi.save()
                return Response(status=status.HTTP_200_OK)
     
            return Response(status=status.HTTP_404_NOT_FOUND)


          