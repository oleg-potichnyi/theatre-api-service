import time

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    helps = "Wait for DB"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Waiting for DB..."))
        db_connection = None
        while not db_connection:
            try:
                db_connection = connections["default"].cursor()
            except OperationalError:
                self.stdout.write(
                    self.style.WARNING("Database unavailable, waiting 1 second...")
                )
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("DB available"))
