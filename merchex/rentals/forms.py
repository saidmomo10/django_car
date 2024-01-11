from django.forms import ModelForm

from .models import Rental

class RentalForm(ModelForm):
    class Meta:
        model = Rental
        fields = ['car', 'customer', 'start_date', 'expected_date']
    def clean_return_date(self):
        return_date = self.cleaned_data['return_date']
        return return_date