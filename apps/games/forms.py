from django import forms
from django.conf import settings
from django.core.files.images import get_image_dimensions

from games.models import Game, Screenshot


MAX_WIDTH, MAX_HEIGHT = map(int,
                            settings.SCREENSHOTS_MAX_DIMENSIONS.split('x'))


class GameForm(forms.ModelForm):
    class Meta(object):
        model = Game
        fields = ('name', 'description', 'url', 'source', 'resources')


class ScreenshotForm(forms.ModelForm):
    class Meta(object):
        model = Screenshot
        fields = ('file',)

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if not file:
            raise forms.ValidationError('You must upload an image!')

        if file.size >> 10 > settings.SCREENSHOTS_MAX_SIZE:
            msg = 'The image was too big (%i KB)! The limit is %i KB.'
            raise forms.ValidationError(msg % (file.size >> 10,
                                               settings.SCREENSHOTS_MAX_SIZE))

        width, height = get_image_dimensions(file)
        if width > MAX_WIDTH:
            msg = 'The image was too wide (%ipx)! The limit is %ipx.'
            raise forms.ValidationError(msg % (width, MAX_WIDTH))
        if height > MAX_HEIGHT:
            msg = 'The image was too tall (%ipx)! The limit is %ipx.'
            raise forms.ValidationError(msg % (height, MAX_HEIGHT))
        return file
