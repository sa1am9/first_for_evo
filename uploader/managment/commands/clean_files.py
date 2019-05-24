from django.core.management.base import BaseCommand, CommandError
from uploader.models import Upload

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('pic', nargs='+')

    def handle(self, *args, **options):
        for pic in options['pic']:
            try:
                file = Upload.objects.get(pk=pic)
            except Upload.DoesNotExist:
                raise CommandError('File "%s" does not exist' % pic)

            file.opened = False
            file.save()

            self.stdout.write(self.style.SUCCESS('Successfully delete file "%s"' % pic))