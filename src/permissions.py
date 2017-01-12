"""Sponsorship permissions."""
from happening.permissions import register_permission

register_permission(
    "Sponsorship",
    "manage_sponsors",
    "Manage Sponsors",
    "Can create/delete/manage sponsors.")
