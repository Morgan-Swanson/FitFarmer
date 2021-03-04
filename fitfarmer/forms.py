from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Row, Column, Submit, Fieldset, Button, ButtonHolder
from fitfarmer.models import User, Food


class NameForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_id = 'full-user-form'
    helper.form_method = 'post'
    helper.form_action = 'register/submit'
    helper.layout = Layout(
        Row(
            Column(Fieldset('Basic Info', 'name', 'gender', 'bmi', 'weight', 'waist_cir'), css_class='col-sm'),
            Column(Fieldset('Basic Diagnostic', 'sys_bp', 'dia_bp', 'cholesterol', 'hdl', 'ldl'), css_class='col-sm'),
            Column(Fieldset('Other Measures', 'atherogenicity', 'tag', 'fpg', 'hb_a1c', 'crp', 'pulse_ox'),
                   css_class='col-sm')
        ),
        ButtonHolder(Submit("Register", "Register", css_class="btn-success"))
    )

    class Meta:
        model = User
        fields = ('name', 'gender', 'bmi', 'weight', 'waist_cir', 'sys_bp', 'dia_bp', 'hdl', 'ldl', 'cholesterol',
                  'atherogenicity', 'tag', 'fpg', 'hb_a1c', 'crp', 'pulse_ox')


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = '__all__'

