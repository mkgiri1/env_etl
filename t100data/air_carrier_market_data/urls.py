# urls.py
from django.urls import path
from . views import MarketDataList, \
    Top5AirportsPaxByOrigin, \
    Top5AirportsPaxByDestination, \
    TopDistanceByMonth, \
    Top5AirportsFreightByOrigin, \
    Top5AirportsFreightByDest,\
    Top5AirportsMailByOrigin,\
    Top5AirportsMailByDest, \
    MaxPassengerByAirlines, \
    MaxMailsByAirlines


urlpatterns = [
    path('list/', MarketDataList.as_view(), name="list"),

    path('top5freightorigin/',
         Top5AirportsFreightByOrigin.as_view(
             extra_context={
                 'title': "Top 5 Airports - Freight by Origin Airport"}
         ),
         name="top5freightorigin"),

    path('top5freightdest/',
         Top5AirportsFreightByDest.as_view(
             extra_context={
                 'title': "Top 5 Airports - Freight by Destination Airport"}
         ),
         name="top5freightdest"),

    path('top5mailorigin/',
         Top5AirportsMailByOrigin.as_view(
             extra_context={
                 'title': "Top 5 Airports - Mail by Origin Airport"}
         ),
         name="top5mailorigin"),

    path('top5maildest/',
         Top5AirportsMailByDest.as_view(
             extra_context={
                 'title': "Top 5 Airports - Mail by Destination Airport"}
         ),
         name="top5maildest"),

    path('top5paxorigin/',
         Top5AirportsPaxByOrigin.as_view(
             extra_context={
                 'title': "Top 5 Airports - Passengers by Origin Airport"}
         ),
         name="top5paxorigin"),

    path('top5paxdestination/',
         Top5AirportsPaxByDestination.as_view(
             extra_context={
                 'title': "Top 5 Airports - Passengers by Destination Airport"}
         ),
         name="top5paxdestination"),

    path('topdistance_month/',
         TopDistanceByMonth.as_view(
             extra_context={'title': "Top Distance by Month"}
         ),
         name="topdistance_month"),

    path('Maxpassengers/',
         MaxPassengerByAirlines.as_view(
             extra_context={'title': "Most passengers carried"}
         ),
         name="Maxpassengers"),

    path('MaxMails/',
         MaxMailsByAirlines.as_view(
             extra_context={'title': "Most Mails carried"}
         ),
         name="MaxMails"),



]
