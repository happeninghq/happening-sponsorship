"""Sponsorship template blocks."""
from happening.plugins import plugin_block
from happening.utils import render_block
from .forms import EventSponsorForm


@plugin_block("events.event.secondary_content")
def event_secondary_content(request, event):
    """Add sponsorship information to event page."""
    if event.event_sponsors.count() == 0:
        return ""
    return render_block(
        request,
        "sponsorship/blocks/events/event/secondary_content.html",
        {"event": event})


@plugin_block("staff.event")
def staff_event(request, event):
    """Add sponsorship links to staff event."""
    return render_block(
        request,
        "sponsorship/blocks/admin/event.html",
        {"event": event,
         "event_sponsor_form": EventSponsorForm(event=event)})
