from django.contrib import admin
from api.models import Model, QualElement, QuantElement, Layout, QualElementPosition, QuantElementPosition, Connection

admin.site.register(Model)
admin.site.register(QualElement)
admin.site.register(Layout)
admin.site.register(QualElementPosition)