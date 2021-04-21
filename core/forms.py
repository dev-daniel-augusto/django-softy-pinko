from django import forms
from django.core.mail.message import EmailMessage


class ContactUsForm(forms.Form):
    name = forms.CharField(label='Name', max_length=200)
    email = forms.EmailField(label='E-mail', max_length=200)
    message = forms.CharField(label='Message', widget=forms.Textarea)

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']

        body = f"""
        Sent by: {name}
        Reply-To: {email}
        
        ******************** Message ******************** 
        {message}
        """

        email = EmailMessage(
            body=body,
            from_email='you_company_email@gmail.com',
            to=['email_1@gmail.com', 'email_2@gmail.com', ],
            headers={'Reply-To': email}
        )
        email.send()

