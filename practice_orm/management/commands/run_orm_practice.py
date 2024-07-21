# practice_orm/management/commands/run_orm_practice.py
from django.core.management.base import BaseCommand
from practice_orm.models import Author, Books

class Command(BaseCommand):
    help = 'Run ORM practice commands'

    def handle(self, *args, **kwargs):
        #  Query 1: Fetching all books from the database
        objec
