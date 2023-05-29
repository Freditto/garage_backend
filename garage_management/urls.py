from django.urls import path
# from .views import RegisterUser,LoginView
from rest_framework_simplejwt import views as jwt_views
from .views import *
app_name = 'garage_management'

urlpatterns = [
    path('viewEngineers/<int:garage_id>', GetEngineer),
    path('registerGarage', RegisterGarage),
    path('registerEngineer', RegisterEngineer),
    path('nearBy', GetNearByGarage),
    # path('nearBy/<ps:lat>/<float:lon>', GetNearByGarage),
    path('garageInfo/<int:garage_id>', GarageInfo),
    path('createFeedRequest', CreateFeedBackRequest),
    path('createFeedAppointment', CreateFeedBackAppointment),
    path('garageFeeds/<int:garage_id>', GarageFeeds),
    path('driverFeeds/<int:driver_id>', GarageAcceptedFeeds),
    path('feedRequestInfo/<int:feed_id>', FeedRequestInfo),
    path('feedAppointmentInfo/<int:feed_id>', FeedAppointmentInfo),
    path('toYesRequest/<int:feed_id>', toYesRequest),
    path('toApprovedRequest/<int:feed_id>', toApprovedRequest),
    path('toYesAppointment/<int:feed_id>', toYesAppointment),
    path('toApprovedAppointment/<int:feed_id>', toApprovedAppointment),
]
