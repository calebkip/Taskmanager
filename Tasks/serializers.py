from rest_framework import serializers
from .models import Ticket,Department,Category,Supervisor,Messsage,Caller

class MessageSerializer(serializers.ModelSerializer):
    created=serializers.DateTimeField(read_only=True)
    class Meta:
        model=Messsage
        fields=['id','commeter','created','description']
class CallerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Caller
        fields=['user','title','department']
class TaskSerializer(serializers.ModelSerializer):
    # owner=serializers.IntegerField()
    messages=MessageSerializer(many=True)
    owner=CallerSerializer()
    class Meta:
        
        model=Ticket
        fields=['id','category','description','owner','messages']
        
        
    # def create(self, validated_data):
    #     owner_id=self.context['owner_id']
    #     return Ticket.objects.create(owner_id=owner_id,**validated_data)
class TaskAssignSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Ticket
        fields=['id','description','priority','assigned','owner','status']
        
class TaskResolveSerializer(serializers.ModelSerializer):
    class Meta:
        
        model=Ticket
        fields=['id','description','owner','resolved','status']
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','title','description']
        
        
class MessageSerializer(serializers.ModelSerializer):
    created=serializers.DateTimeField(read_only=True)
    class Meta:
        model=Messsage
        fields=['id','commeter','ticket_id','created','description']
        
        
    def create(self, validated_data):
        ticket_id=self.context['ticket_id']
        return Messsage.objects.create(ticket_id=ticket_id,**validated_data)
    
class CallerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Caller
        fields=['user','title','department']
class DepartmentSerializer(serializers.ModelSerializer):
    tickets_raised=serializers.SerializerMethodField()
    class Meta:
        model=Department
        fields=['title','supervisor','tickets_raised']
        
    def get_tickets_raised(self,instance):
        tickets=Ticket.objects.filter(owner__department=instance)
        ticketserializer=TaskSerializer(tickets,many=True)
        return ticketserializer.data