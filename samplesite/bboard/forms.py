from django.forms import ModelForm, modelformset_factory

from .models import Bb, Rubric

class BbForm(ModelForm):
	class Meta:
		model = Bb
		fields = ('title', 'content', 'price', 'rubric')


RubricFormSet = modelformset_factory(Rubric, fields=('name',), can_order=True, can_delete=True )