from django.core.management.base import BaseCommand, CommandError
from toDoRest.models import User
#from backend.toDoRest.models import User


class Command(BaseCommand):
    help = 'need file from users'

    def handle(self, *args, **options):

        User.objects.create_user(options['email'], options['password'])

    def add_arguments(self, parser):
        parser.add_argument(
        '-e',
        '--email',
        action='store',
        default=False,
        help='Почта пользователя',
        required=True
        )
        parser.add_argument(
        '-p',
        '--password',
        action='store',
        default=False,
        help='Пароль пользователя',
        required=True
        )

