from django.contrib import admin
from .models import Media, Membre, Livre, DVD, CD, Jeuplateau

admin.site.register(Media)
admin.site.register(Membre)
admin.site.register(Livre)
admin.site.register(DVD)
admin.site.register(CD)
admin.site.register(Jeuplateau)