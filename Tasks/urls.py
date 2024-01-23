from django.contrib import admin
from django.urls import path,include
from . import views

# from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers


router=routers.DefaultRouter()
router.register('tickets',views.TicketViewSet)
router.register('categories',views.CategoryViewSet)
router.register('department',views.DepartmentViewSet)

ticket_router=routers.NestedDefaultRouter(router,'tickets',lookup='ticket')
ticket_router.register('messages',views.MessageViewSet,basename="ticket_messages")
urlpatterns =  router.urls+ ticket_router.urls
    
#     path('',include(router.urls)),
#     path('messages/',views.MessageViewSet.as_view),
# ]

