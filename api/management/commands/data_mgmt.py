from django.core.management.base import BaseCommand
from api.models import *
from datetime import date


class Command(BaseCommand):
    def handle(self, *args, **options):
        for model in Model.objects.all():
            layout = Layout(
                label="default",
                model=model,
            )
            layout.save()