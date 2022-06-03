from django import forms
from .models import Order


# Create the form class.
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        # Call the default init method to set the form up
        super().__init__(*args, **kwargs)
        # Create a dictionary to show up in the form fill
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
        }

        # Set the autofocus to "full_name"
        # Cursor will start in the "full_name" everytime page is loads
        self.fields['full_name'].widget.attrs['autofocus'] = True
        # Iterate through the forms fields
        for field in self.fields:
            if field != 'country':
                # Add a star as a required field in the placeholder
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                # Setting all the placeholder attributes to their /
                # values in the dict.
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
