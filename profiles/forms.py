from django import forms
from .models import UserProfile


# Create the form class.
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        # Call the default init method to set the form up
        super().__init__(*args, **kwargs)
        # Create a dictionary to show up in the form fill
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        # Set the autofocus to "default_phone_number"
        # Cursor will start in the "default_phone_number" when page is loads
        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        # Iterate through the forms fields
        for field in self.fields:
            if field != 'default_country':
                # Add a star as a required field in the placeholder
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                # Setting all the placeholder attributes to their /
                # values in the dict.
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = (
                'border-black rounded-0 profile-form-input')
            self.fields[field].label = False
