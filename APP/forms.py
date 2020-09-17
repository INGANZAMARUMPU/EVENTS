from django import forms
from API.models import Profile, Ticket

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
	lastname = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Izina '}),
		label='izina')
	firstname = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Itazirano '}),
		label='Itazirano')
	phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Telephone '}),
		label='Telephone')
	mobile = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Téléphone 2'}),
		label='Tél. de bureau', required=False)
	ticket = forms.ModelChoiceField(widget = forms.Select(),label = 'Tiquet',
		queryset = Ticket.objects.all())
	autres = forms.CharField(widget=forms.Textarea(
			attrs={'placeholder':'Autres informations', 'rows':'3'}),
		label='Itazirano', required=False)
	avatar = forms.ImageField( widget=forms.FileInput(),label='photo de profile',required=False)
	
	def __init__(self, *args, **kwargs):
		profile = kwargs.get('instance')
		super(ProfileForm, self).__init__(*args, **kwargs)
		if(profile) :
			self.fields["lastname"].initial = profile.user.last_name
			self.fields["firstname"].initial = profile.user.first_name
			self.fields["phone"].initial = profile.phone
			self.fields["mobile"].initial = profile.mobile
			self.fields["ticket"].initial = profile.ticket
			self.fields["autres"].initial = profile.autres
			self.fields["avatar"].initial = profile.avatar
	
	class Meta:
		model = Profile
		fields = ('firstname', 'lastname', 'phone', 'mobile', 'ticket', 'avatar', 'autres')


	# def clean_CNI(self, *arg,**kwargs):
	# 	if others and (CNI!=self.old_cni):
	# 		raise forms.ValidationError("Ce CNI existe déja. êtes-vous entrain de recuperer votre compte?")
	# 	return CNI
