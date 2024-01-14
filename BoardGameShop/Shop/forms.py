from django import forms

# class ContactForm1(forms.Form):
#     subject = forms.CharField(max_length=100)

class OrderDetailForm(forms.Form):
    BOOL_CHOICES_PAYMENT = [
        ('1', 'Blik'),
        ('2', 'Payment 24'),
    ]
    payment = forms.BooleanField(
        widget=forms.RadioSelect(choices=BOOL_CHOICES_PAYMENT)
    )

class DeliveryForm(forms.Form):
    BOOL_CHOICES = [
        ('1', 'Inpost'),
        ('2', 'UPS'),
    ]
    delivery = forms.BooleanField(
        widget=forms.RadioSelect(choices=BOOL_CHOICES)
    )

class ConfirmOrder(forms.Form):
    pass