from django import forms

# class ContactForm1(forms.Form):
#     subject = forms.CharField(max_length=100)

class OrderPaymentForm(forms.Form):
    BOOL_CHOICES = [
        ('1', 'Option 1'),
        ('2', 'Option 2'),
    ]
    payment = forms.BooleanField(
        widget=forms.RadioSelect(choices=BOOL_CHOICES)
    )