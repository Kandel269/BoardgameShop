from django import forms

# class ContactForm1(forms.Form):
#     subject = forms.CharField(max_length=100)

class OrderDetailForm(forms.Form):
    RADIO_CHOICES_PAYMENT = [
        ('Blik', 'Blik'),
        ('Payment_24', 'Payment 24'),
    ]
    payment = forms.ChoiceField(
        widget=forms.RadioSelect, choices=RADIO_CHOICES_PAYMENT
    )

class DeliveryForm(forms.Form):
    RADIO_CHOICES_DELIVERY = [
        ('Inpost', 'Inpost'),
        ('UPS', 'UPS'),
    ]
    delivery =forms.ChoiceField(
        widget=forms.RadioSelect, choices=RADIO_CHOICES_DELIVERY
    )

class ConfirmOrder(forms.Form):
    pass