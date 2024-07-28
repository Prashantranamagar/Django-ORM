# practice_orm/management/commands/run_orm_practice.py
from django.core.management.base import BaseCommand
from practice_orm.practice_orm import practice_orm


class Command(BaseCommand):
    help = 'Run ORM practice commands'

    def handle(self, *args, **kwargs):
        practice_orm()