from django.core.management.base import BaseCommand
import logging


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Тест команды my_command
    """
    help = "Print 'Hello world!' to output."

    def handle(self, *args, **kwargs):
        logger.info('Help requested!')
        self.stdout.write('Hello world!')
