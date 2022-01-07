from django import forms
from videos.models import Video
from playlists.models import PlayList

class VideoCreateForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('title', 'youtube_url', 'thumbnail_image', 'description', 'available')

        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'youtube_url' : forms.URLInput(attrs={'class' : 'form-control'}),
            'description' : forms.Textarea(attrs={'class' : 'form-control'}),
            'available' : forms.CheckboxInput(attrs={'class' : 'form-check'})
        }

class PlayListCreateForm(forms.ModelForm):
    class Meta:
        model = PlayList
        fields = ('title', )

        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
        }