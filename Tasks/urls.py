from django.contrib import admin
from django.urls import path,include
from . import views

# from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers


router=routers.DefaultRouter()
router.register('tickets',views.TicketViewSet)
router.register('categories',views.CategoryViewSet)
router.register('department',views.DepartmentViewSet)
router.register('technicians',views.TechnicianViewSet)
router.register('supervisors',views.SupervisorViewSet,basename='supervisors')

ticket_router=routers.NestedDefaultRouter(router,'tickets',lookup='ticket')
ticket_router.register('messages',views.MessageViewSet,basename="ticket_messages")
ticket_router.register('assign',views.AssignTicketView,basename='assign_ticket')
technician_router=routers.NestedDefaultRouter(router,'technicians',lookup='technician')
technician_router.register('technician_ticket',views.TechnicianTicketsViewSet,basename='technician_ticket')
department_router=routers.NestedDefaultRouter(router,'department',lookup='department')
department_router.register('tickets_raised',views.DepartmentTicketsViewSet,basename='tickets_raised')
supervisor_router=routers.NestedDefaultRouter(router,'supervisors',lookup='supervisor')
supervisor_router.register('dept_tickets',views.SupervisorTicketsViewSet,basename='dept_tickets')

# ticket_router.register('technicians',views.TechnicianViewSet)
# ticket_router.register('assign-ticket',views.AssignTicketView,basename='assign-ticket')
urlpatterns = [
    path('',include(router.urls)),
    path('',include(ticket_router.urls)),
    # path('department_tickets/',views.SupervisorTicketListView.as_view()),
    path('',include(department_router.urls)),
    path('',include(technician_router.urls)),
    path('',include(supervisor_router.urls)),
    # path('tickets/assign/<int:pk>/',views.AssignTicketView.as_view(), name='assign-ticket'),
]


# router.urls+ ticket_router.urls
    
#     path('',include(router.urls)),
#     path('messages/',views.MessageViewSet.as_view),
# ]

