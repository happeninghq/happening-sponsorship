from pages.utils import BlockType, register_block_type
from django import forms
from django.template.loader import render_to_string


@register_block_type
class SponsorsBlockType(BlockType):
    """List sponsors."""

    title = forms.CharField()

    def render_content(self, request, data):
        """Return the list of sponsors."""
        from .models import SponsorTier, CommunitySponsorship

        if CommunitySponsorship.objects.count() == 0:
            # No sponsors, don't show it
            return ""

        return render_to_string("sponsorship/page_blocks/sponsors.html",
                                {"sponsor_tiers": SponsorTier.objects.all()},
                                request=request)
