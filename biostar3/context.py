from __future__ import absolute_import, division, print_function, unicode_literals

from django.conf import settings

from django.core.cache import cache
from biostar3 import VERSION

def shortcuts(request):
    # These values will be added to each context

    context = {
        "BIOSTAR_VERSION": VERSION,
    }

    return context

