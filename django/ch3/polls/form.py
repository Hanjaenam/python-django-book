from django import forms

class test_form(forms.Form):
  label_id_or_input_name = forms.CharField(label="label", max_length=100)