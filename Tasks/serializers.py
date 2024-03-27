from rest_framework import serializers
from .models import Ticket,Department,Category,Supervisor,Messsage,Caller,Technician

class MessageSerializer(serializers.ModelSerializer):
    created=serializers.DateTimeField(read_only=True)
    class Meta:
        model=Messsage
        fields=['id','commeter','created','description']
        
    def create(self, validated_data):
        ticket_id=self.context['ticket_id']
        return Messsage.objects.create(ticket_id=ticket_id,**validated_data)
    
class CallerSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model=Caller
        fields=['username','user_id','title','department']
class TaskSerializer(serializers.ModelSerializer):
    # owner=serializers.IntegerField()
    messages=MessageSerializer(many=True,read_only=True)
    owner=CallerSerializer(read_only=True)
    status=serializers.ReadOnlyField()
    class Meta:
        model=Ticket
        fields=['id','category','description','owner','messages','status']
class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ticket
        fields=['category','description']
    
    def create(self,validated_data):
        (owner,created)=Caller.objects.get_or_create(user_id=self.context['user_id'] )
        ticket_instance = Ticket.objects.create(owner=owner,**validated_data)
        return ticket_instance  
           
class TaskAssignSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Ticket
        fields=['id','priority','assigned','owner','category']
        
    def update(self, instance, validated_data):
        
        
        instance.status = "assigned"  # Update with your logic
        return super().update(instance, validated_data)
class TaskResolveSerializer(serializers.ModelSerializer):
    class Meta:
        
        model=Ticket
        fields=['id','description','owner','resolved','status']   
    # def def save(self, *args, **kwargs):
       
    #    super(ModelName, self).save(*args, **kwargs) # Call the real save() method
    
    
    
    # class Meta:
    #     model=Ticket
    #     fields=['category','description']   
        
        
        # def get_owner(self, obj):
        #     # Access the authenticated user from the context
        #     user = self.context['request'].user
        #     return {'id': user.id, 'username': user.username, 'email': user.email}

           
        # def save(self, validated_data):
            
        #     owner_id=Caller.objects.only('id').get(user_id=self.request.user)

          
        #     ticket_instance = Ticket.objects.create(**validated_data,owner_id=owner_id)

        #     return ticket_instance
    # def create(self, validated_data):
    #     owner_id=self.context['owner_id']
    #     return Ticket.objects.create(owner_id=owner_id,**validated_data)

        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','title','description']
        
        
# class MessageSerializer(serializers.ModelSerializer):
#     created=serializers.DateTimeField(read_only=True)
#     class Meta:
#         model=Messsage
#         fields=['id','commeter','ticket_id','created','description']
        
        
    
# class CallerSerializer(serializers.ModelSerializer):
#     username = serializers.ReadOnlyField(source='user.username')
#     class Meta:
#         model=Caller
#         fields=['username','title','department']
class DepartmentSerializer(serializers.ModelSerializer):
    # tickets_raised=serializers.SerializerMethodField()
    
    class Meta:
        model=Department
        fields=['id','title','supervisor']
# class DepartmentTicketsSerializer(serializers.ModelSerializer):    
#     def get_tickets_raised(self,instance):
#         tickets=Ticket.objects.filter(owner__department=instance)
#         ticketserializer=TaskSerializer(tickets,many=True)
#         return ticketserializer.data
class TechnicianSerializer(serializers.ModelSerializer):
    # technicianassigned=TaskSerializer(many=True)
    username = serializers.ReadOnlyField(source='user.username')
    email=serializers.ReadOnlyField(source='user.email')
    class Meta:
        model=Technician
        fields=['id','user_id','department','email','username']
        
class SupervisorSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    # dept_tickets=serializers.SerializerMethodField()
    class Meta:
        model=Supervisor
        fields=['username','title']
        
        
    # def get_dept_tickets(self,instance):
    #     tickets=Ticket.objects.filter(owner__department=instance)
    #     ticketserializer=TaskSerializer(tickets,many=True)
    #     return ticketserializer.data