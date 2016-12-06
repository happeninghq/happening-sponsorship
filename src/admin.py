"""Sponsorship administration."""

from django.conf.urls import url
from plugins.sponsorship import views


urlpatterns = [
    url(r'^sponsorship_tiers$', views.sponsorship_tiers,
        name='sponsorship_tiers'),
    url(r'^sponsorship_tiers/create$', views.create_sponsorship_tier,
        name='create_sponsorship_tier'),
    url(r'^sponsorship_tiers/(?P<pk>\d+)$', views.edit_sponsorship_tier,
        name='edit_sponsorship_tier'),
    url(r'^sponsors$', views.sponsors, name='sponsors'),
    url(r'^sponsors/create$', views.create_sponsor, name='create_sponsor'),
    url(r'^sponsors/(?P<pk>\d+)$', views.staff_view_sponsor,
        name='staff_view_sponsor'),
    url(r'^sponsors/(?P<pk>\d+)/edit$', views.edit_sponsor,
        name='edit_sponsor'),
    url(r'^sponsors/(?P<pk>\d+)/edit/community$',
        views.add_community_sponsorship_to_sponsor,
        name='add_community_sponsorship_to_sponsor'),
    url(r'^sponsors/event/(?P<pk>\d+)$',
        views.add_sponsor_to_event, name='add_sponsor_to_event'),
    url(r'^sponsors/event/(?P<pk>\d+)/remove$',
        views.remove_sponsor_from_event, name='remove_sponsor_from_event'),
]

admin_links = (
    ("Sponsorship", "sponsors"),
)
