from django import forms
from django.core.validators import RegexValidator
from django.core.mail import EmailMessage
from django.conf import settings


class ContactForm(forms.Form):
    phone_rg = RegexValidator(regex=r'^[0-9\-]+$')
    # message=("電話番号は数字と - のみで入力してください"))

    name = forms.CharField(label='お名前', max_length=200)

    email = forms.EmailField(label='メールアドレス', max_length=100)

    phone = forms.CharField(
            label='電  話',
            validators=[phone_rg],
            max_length=15)

    comment = forms.CharField(
            label='内  容',
            widget=forms.Textarea,
            max_length=800)

    def send_email(self):
        fdata = self.cleaned_data

        subject = 'ロングリブネットへのお問い合わせ'
        from_email = settings.FROM_EMAIL_ADDRESS
        to = [fdata['email']]
        ccs = [from_email]
        message = """
{name} 様

ロングリブネットにお問い合わせいただきまして
誠にありがとうございました。

以下のお問い合わせを承りました。
-------------------

◆ お名前
{name} 様

◆ メールアドレス
{email}

◆ 電話番号
{phone}

◆ お問い合わせ内容
{comment}

-------------------
当お問い合わせにつきましては、追ってロング
リブネットよりご連絡させていただきます。
何卒今しばらくお待ちください。

今後ともよろしくお願い申し上げます。

        """.format(**fdata)

        # Send EMail
        em = EmailMessage(subject, message, from_email, to, cc=[], bcc=ccs)
        em.send()
