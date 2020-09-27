from django import forms
from API.models import *

class ConnexionForm(forms.Form):
	username = forms.CharField(
		widget=forms.TextInput(
			attrs={'placeholder':'Username ', 'class':'input'}),
		# label=""
	)
	password = forms.CharField(
		widget=forms.PasswordInput(
			attrs={'placeholder':'Password ', 'class':'input', 'type':'password'}
		),
		# label=""
	)

class ProfileForm(forms.ModelForm):
	lastname = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nom '}),
		label='Izina')
	firstname = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Prenom '}),
		label='Itazirano')
	phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'ex: 75 96 06 96 '}),
		label='Telephone')
	email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'ex: username@gmail.com'}),
		label='Adresse e-mail', required=False)
	ticket_type = forms.ModelChoiceField(widget = forms.Select(),
		label = 'Type de ticket',
		queryset = TicketType.objects.all())
	avatar = forms.ImageField( widget=forms.FileInput(),label='photo de profile',required=False)
	autres = forms.CharField(widget=forms.Textarea(
			attrs={'placeholder':'Autres informations', 'rows':'3'}),
		label='Autres informations', required=False)
	
	def __init__(self, *args, **kwargs):
		profile = kwargs.get('instance')
		super(ProfileForm, self).__init__(*args, **kwargs)
		if(profile) :
			self.fields["lastname"].initial = profile.user.last_name
			self.fields["firstname"].initial = profile.user.first_name
			self.fields["phone"].initial = profile.phone
			self.fields["email"].initial = profile.email
			self.fields["ticket_type"].initial = profile.ticket.ticket_type
			self.fields["autres"].initial = profile.autres
			self.fields["avatar"].initial = profile.avatar
	
	class Meta:
		model = Profile
		fields = ('firstname', 'lastname', 'phone', 'email', 'avatar', 'autres')


	# def clean_CNI(self, *arg,**kwargs):
	# 	if others and (CNI!=self.old_cni):
	# 		raise forms.ValidationError("Ce CNI existe déja. êtes-vous entrain de recuperer votre compte?")
	# 	return CNI
