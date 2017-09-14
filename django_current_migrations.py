# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.management.base import BaseCommand, CommandError
from django.db import DEFAULT_DB_ALIAS, connections
from django.db.migrations.loader import MigrationLoader
from collections import defaultdict
from django.conf import settings


class Command(BaseCommand):
    help = "Show latest applied migrations for current project"

    def handle(self, *args, **options):
        db = DEFAULT_DB_ALIAS
        connection = connections[db]
        
        self.show_list(connection)

    def show_list(self, connection):
        loader = MigrationLoader(connection, ignore_no_migrations=True)

        app_names = set(settings.PROJECT_APPS)
        applied_migrations = {(a, m) for a, m in loader.applied_migrations if a in app_names}

        latest_migrations = defaultdict(lambda: None)

        for app, migration in applied_migrations:
            latest_migrations[app] = max(
                latest_migrations[app],
                migration
            )

        for app, migration in sorted(latest_migrations.iteritems()):
            print './manage.py migrate {app} {migration}'.format(app=app, migration=migration)
