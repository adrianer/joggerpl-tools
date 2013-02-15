from django.contrib import admin
from models import Kategoria, Wpis, Komentarz, Trackback, Link, GrupaLinkow

"""
This file is part of joggertester.

Joggertester is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

Joggertester is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Foobar; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""

class KategoriaAdmin(admin.ModelAdmin):
    pass

class WpisAdmin(admin.ModelAdmin):
    pass

class KomentarzAdmin(admin.ModelAdmin):
    pass

class TrackbackAdmin(admin.ModelAdmin):
    pass

class LinkAdmin(admin.ModelAdmin):
    pass

class GrupaLinkowAdmin(admin.ModelAdmin):
    pass


admin.site.register(Kategoria, KategoriaAdmin)
admin.site.register(Wpis, WpisAdmin)
admin.site.register(Komentarz, KomentarzAdmin)
admin.site.register(Trackback, TrackbackAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(GrupaLinkow, GrupaLinkowAdmin)
