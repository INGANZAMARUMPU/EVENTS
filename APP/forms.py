from django import forms
from API.models import Profile

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
	firstname = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Izina '}),
		label='izina')
	lastname = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Itazirano '}),
		label='Itazirano')
	phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Telephone '}),
		label='Telephone')
	mobile = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Téléphone 2'}),
		label='Tél. de bureau')
	autres = forms.CharField(widget=forms.Textarea(
			attrs={'placeholder':'Autres informations', 'rows':'3'}),
		label='Itazirano')
	avatar = forms.ImageField( widget=forms.FileInput(),label='photo de profile')
	
	def __init__(self, *args, **kwargs):
		# user = kwargs.get('user')
		# if(user) :
		# 	kwargs.pop('user')
		super(ProfileForm, self).__init__(*args, **kwargs)
	
	class Meta:
		model = Profile
		fields = ('firstname', 'lastname', 'phone', 'mobile', 'avatar', 'autres')


	# def clean_CNI(self, *arg,**kwargs):
	# 	if others and (CNI!=self.old_cni):
	# 		raise forms.ValidationError("Ce CNI existe déja. êtes-vous entrain de recuperer votre compte?")
	# 	return CNI
