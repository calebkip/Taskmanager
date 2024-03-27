from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.exceptions import MethodNotAllowed
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.viewsets import ModelViewSet
from .models import Ticket,Technician,Category,Messsage,Department,Supervisor
from .serializers import TaskSerializer,CategorySerializer,MessageSerializer,\
    TaskAssignSerializer,TaskResolveSerializer,DepartmentSerializer,TechnicianSerializer,\
        SupervisorSerializer,TaskCreateSerializer
# Create your views here.
class TicketViewSet(ModelViewSet):
    
    queryset=Ticket.objects.all()
    permission_classes=[IsAuthenticated]
    
    def get_serializer_class(self):
        user = self.request.user
        if user.is_authenticated and hasattr(user,'caller'):
             if self.request.method=='POST':
                return TaskCreateSerializer
            
             return TaskSerializer
            
        elif user.is_authenticated and user.is_staff:
            if self.request.method=='GET':
                return TaskSerializer
            return TaskSerializer
            
              
        elif user.is_authenticated and hasattr(user,'technician'):
            if self.request.method=='GET':
                return TaskSerializer
            return TaskResolveSerializer
        return TaskSerializer
        #     and hasattr(user,'is_supervisor') and user.is_superuser:
        # if self.request.method=='POST':
        #     return TaskCreateSerializer
        # return TaskSerializer
    
    def get_serializer_context(self):
        return {'user_id':self.request.user.id}



    
    
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
    
class DepartmentTicketsViewSet(ModelViewSet):
    http_method_names=['get','patch','delete','head','options']
    serializer_class=TaskAssignSerializer
    def get_queryset(self):
        return Ticket.objects.filter(owner__department=self.kwargs['department_pk'])
        
        
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
    
    
class SupervisorViewSet(ModelViewSet):
    
    serializer_class=SupervisorSerializer
    queryset=Supervisor.objects.all()
    @action(detail=True)
    def profile(self,request):
        return Response("ok")
    
class SupervisorTicketsViewSet(ModelViewSet):
    http_method_names=['get','patch','delete','head','options']
    serializer_class=TaskAssignSerializer
    def get_queryset(self):
        supervisor_id=self.kwargs['supervisor_pk']
        supervisor= get_object_or_404(Supervisor, pk=supervisor_id)
        department = supervisor.department_set.first()
        return Ticket.objects.filter(owner__department=department)
    

    
class AssignTicketView(ModelViewSet):
    # http_method_names=['get','patch','delete','head','options']
    serializer_class=TaskAssignSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Ticket.objects.filter(id=self.kwargs['ticket_pk'])
    
    def create(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
    
    
    # def get_serializer_class(self):
    #     if self.request.method=='PATCH':
    #         return TaskAssignSerializer
    #     return TaskSerializer
    
    # def update(self, request, *args, **kwargs):
    #     technician_id = self.request.data.get('technician_id')
    #     technician = Technician.objects.get(pk=technician_id)
    #     partial = kwargs.pop('partial', True)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance,
    #                                      assigned=technician,
    #                                      status='assigned',
    #                                      data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     return Response(serializer.data)  
    # def update(self, serializer):
    #     technician_id = self.request.data.get('technician_id')
    #     technician = Technician.objects.get(pk=technician_id)
    #     serializer.save(serializer.data,assigned=technician, status='assigned')
        
class TechnicianViewSet(ModelViewSet):
    queryset=Technician.objects.all()
    serializer_class=TechnicianSerializer
    @action(detail=False,methods=['GET','PUT'])
    def profile(self,request):
        (technician,created)=Technician.objects.get_or_create(user_id=request.user.id)
        if request.method =='GET':
            serializer=TechnicianSerializer(technician)
            return Response(serializer.data)
        elif request.method =='PUT':
            serializer=TechnicianSerializer(technician,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        
class TechnicianTicketsViewSet(ModelViewSet):
    http_method_names=['get','patch','delete','head','options']
    serializer_class=TaskResolveSerializer
    def get_queryset(self):

        return Ticket.objects.filter(assigned=self.kwargs['technician_pk'])

        # def get_serializer_class(self):
    #     if self.request.method == 'GET':
    #         return TaskSerializer
    
    #     elif self.request.method in ['PATCH', 'PUT']:
    #         ticket_object = self.get_object()

    #         if ticket_object is not None:
    #             status = ticket_object.status or 'unassigned'
    #             print(f"Debug: Status - {status}, Request Method - {self.request.method}")

    #             if status == 'unassigned':
    #                 return TaskResolveSerializer

    #             elif status == 'assigned':
    #                 return TaskAssignSerializer

    #             else:
    #                 print(f"Debug: Unexpected status value - {status}")
    #                 raise ValueError(f"Unexpected status value - {status}")
    #         else:
    #             print("Debug: Ticket object is None")
    #         # Handle the case where status is None, e.g., set a default serializer
    #             return TaskSerializer
    #     elif self.request.method == 'POST':
    #     # Use a serializer for creating new resources
    #         return TaskSerializer 
    #     else:
    #         print(f"Debug: Unexpected request method - {self.request.method}")
    #         raise ValueError(f"Unexpected request method - {self.request.method}")
    
    
        # if user.is_authenticated and hasattr(user,'department') and hasattr(user,'is_supervisor') and user.is_superuser:
    # #         department_tickets=Ticket.objects.filter(owner__department=user.department)
    
    # serializer_class=TaskSerializer
    # permission_classes=[IsAuthenticated]
    
    
    # def get_queryset(self):
    #     user=self.request.user
        
        
    #     if user.is_authenticated and hasattr(user,'department') and hasattr(user,'is_supervisor') and user.is_superuser:
    #         department_tickets=Ticket.objects.filter(owner__department=user.department)
    #         return department_tickets
    #     return Ticket.objects.none()
    #     raise ValueError('no tickets have beeen raised')