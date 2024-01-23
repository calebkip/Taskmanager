from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.viewsets import ModelViewSet
from .models import Ticket,Technician,Category,Messsage,Department
from .serializers import TaskSerializer,CategorySerializer,MessageSerializer,\
    TaskAssignSerializer,TaskResolveSerializer,DepartmentSerializer
# Create your views here.
class TicketViewSet(ModelViewSet):
    
    queryset=Ticket.objects.all()
    permission_classes=[IsAuthenticated]
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TaskSerializer
    
        elif self.request.method in ['PATCH', 'PUT']:
            ticket_object = self.get_object()

            if ticket_object is not None:
                status = ticket_object.status or 'unassigned'
                print(f"Debug: Status - {status}, Request Method - {self.request.method}")

                if status == 'unassigned':
                    return TaskResolveSerializer

                elif status == 'assigned':
                    return TaskAssignSerializer

                else:
                    print(f"Debug: Unexpected status value - {status}")
                    raise ValueError(f"Unexpected status value - {status}")
            else:
                print("Debug: Ticket object is None")
            # Handle the case where status is None, e.g., set a default serializer
                return TaskSerializer
        elif self.request.method == 'POST':
        # Use a serializer for creating new resources
            return TaskSerializer 
        else:
            print(f"Debug: Unexpected request method - {self.request.method}")
            raise ValueError(f"Unexpected request method - {self.request.method}")


    
    
class CategoryViewSet(ModelViewSet):
    queryset=Category.objects.all()  
    serializer_class=CategorySerializer
    
class MessageViewSet(ModelViewSet):
    
    serializer_class=MessageSerializer
    def get_queryset(self):
        
        return Messsage.objects.filter(ticket_id=self.kwargs['ticket_pk'])
    
    def get_serializer_context(self):
        return {'ticket_id':self.kwargs['ticket_pk']}
    
class DepartmentViewSet(ModelViewSet):
    serializer_class=DepartmentSerializer
    queryset=Department.objects.all()
    # permission_classes=IsAdminUser
    # def get(self,request):
    #     queryset=Ticket.objects.all()
    #     serializer=TaskSerializer(queryset,many=True,context={'request':request})
    #     return Response(serializer.data)
    # def post(self,request):
    #     serializer=TaskSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data,status=status.HTTP_201_CREATED)