from django import forms

from .models import Hosts,Visitors

class HostsForm(forms.ModelForm):

    class Meta:
        model = Hosts
        fields = ('name','email','phone')

class VisitorsForm(forms.ModelForm):

    class Meta:
        model = Visitors
        fields = ('name','email','phone','name_of_host_id')

class VisitorsOutForm(forms.ModelForm):

    class Meta:
        model = Visitors
        fields = ('phone',)