# core/management/commands/check_db.py
import sys
import time
import psycopg2
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Waits until PostgreSQL is available before continuing"

    def handle(self, *args, **options):
        suggest_unrecoverable_after = 30
        start = time.time()

        while True:
            try:
                psycopg2.connect(
                    dbname=settings.DATABASES["default"]["NAME"],
                    user=settings.DATABASES["default"]["USER"],
                    password=settings.DATABASES["default"]["PASSWORD"],
                    host=settings.DATABASES["default"]["HOST"],
                    port=settings.DATABASES["default"]["PORT"],
                )
                self.stdout.write(self.style.SUCCESS(
                    "✅ PostgreSQL is available"))
                break
            except psycopg2.OperationalError as error:
                self.stderr.write(
                    "⏳ Waiting for PostgreSQL to become available...")
                if time.time() - start > suggest_unrecoverable_after:
                    self.stderr.write(
                        f"⚠️ This is taking longer than expected. "
                        f"The following error may be unrecoverable:\n{error}"
                    )
                time.sleep(3)
