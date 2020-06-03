from django import forms

class ApprovalForm(forms.Form):

	Firstname=forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Enter Firstname'}))
	Lastame=forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Enter Lastname'}))
	Age=forms.IntegerField()
	CreditAmount=forms.IntegerField()
	Duration=forms.IntegerField()
	Gender=forms.ChoiceField(choices=[('Male', 'Male'),('Female', 'Female')])
	Housing=forms.ChoiceField(choices=[('Own', 'Own'),('Free', 'Free'),('Rent', 'Rent')])
	SavingAccount=forms.ChoiceField(choices=[('little', 'Little'),('Moderate', 'Moderate'),('Rich', 'Rich')])
	CheckingAccount=forms.ChoiceField(choices=[('little', 'Little'),('Moderate', 'Moderate'),('Rich', 'Rich')])
	Purpose=forms.ChoiceField(choices=[('Own', 'Own'),('Free', 'Free'),('Rent', 'Rent')])
