from django.shortcuts import render_to_response
from models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
import datetime

def current_time(request):
	now =datetime.datetime.now()
	html="<html><body> time is %s.</body></html>"% now
	return HttpResponse(html)

######################## Company Registeration #########################

def insert_data_company(request):
	if request.method == 'POST':
		form = CompanyForm(request.POST,request.FILES)
		if form.is_valid():

			form.save()
			#form.company_id

		return render_to_response('register/company.html', {'form': form}, RequestContext(request))
	else:
			form = CompanyForm()
			return render_to_response('register/company.html', {'form': form}, RequestContext(request))

######################## Product Registeration #########################

def insert_data_product(request):
	if request.method == 'POST':
		form = ProductForm(request.POST,request.FILES)
		if form.is_valid():
			#cd= form.cleaned_data
			#data=(cd['product_name'],cd['description'],cd['product_qrcode'])
			form.save()
		return render_to_response('register/product.html', {'form': form}, RequestContext(request))
	else:
		form = ProductForm()
		return render_to_response('register/product.html', {'form': form}, RequestContext(request))

######################## Compaign Registeration #########################

def insert_data_compaign(request):
	if request.method == 'POST':
		form = CompaignForm(request.POST,request.FILES)
		if form.is_valid():
			#cd= form.cleaned_data
			#data=(cd['product_name'],cd['description'],cd['product_qrcode'])
			form.save()
		return render_to_response('register/compaign.html', {'form': form}, RequestContext(request))
	else:
		form = CompaignForm()
		return render_to_response('register/compaign.html', {'form': form}, RequestContext(request))

############################## Company Login #############################

def companyLogIn(request):
	if request.method == 'POST':
		form = CompanyLogInForm(request.POST)
		cName = request.POST.get('company_name')
		passwd = request.POST.get('password')
		if Company.objects.filter(company_name=cName):
				if Company.objects.filter(password=passwd):
					#cfilter = Company.objects.filter(company_name=cName)
					#for e in Company.objects.filter(company_name=cName):
					#	cid = e.id
					#return HttpResponseRedirect('/companies/cloginsucceed/'+str(cid))
					return HttpResponse("LogIn Succeeded =)")
				else:
					return HttpResponse("Invalid Password !")
		else:
				return HttpResponse("Invalid Company Name !")
	else:
		form = CompanyLogInForm()
		return render_to_response('companies/login.html', {'form': form}, RequestContext(request))

######################## Newsletter Subscription #########################

def subscribe_newsletter(request):
	if 'newsletter' in request.GET:
		message = 'You entered: %s' % request.GET['newsletter']
	else:
		message = 'You submitted an empty form.'
	return HttpResponse(message)

################################ Product QRcode ########################################

def urlqrcode_pre_save_product(sender, instance, **kwargs):
	if not instance.pk:
		instance._QRCODE = True
	else:
		if hasattr(instance, '_QRCODE'):
			instance._QRCODE = False
		else:
			instance._QRCODE = True
 
models.signals.pre_save.connect(urlqrcode_pre_save_product, sender=Product)
 
def urlqrcode_post_save_product(sender, instance, **kwargs):
	
	if instance._QRCODE:
		instance._QRCODE = False
		if instance.qr_image:
			instance.qr_image.delete()
		qr = QRCode(4, QRErrorCorrectLevel.L)
		qr.addData(instance.url)
		qr.make()
		image = qr.makeImage()
 
		#Save image to string buffer
		image_buffer = StringIO()
		image.save(image_buffer, format='JPEG')
		image_buffer.seek(0)
		 
		#Here we use django file storage system to save the image.
		file_name = 'UrlQR_%s.jpg' % instance.product_id
		file_object = File(image_buffer, file_name)
		content_file = ContentFile(file_object.read())
		instance.qr_image.save(file_name, content_file, save=True)
 
models.signals.post_save.connect(urlqrcode_post_save_product, sender=Product)

################################ Compaign QRcode ########################################

def urlqrcode_pre_save_compaign(sender, instance, **kwargs):
	if not instance.pk:
		instance._QRCODE = True
	else:
		if hasattr(instance, '_QRCODE'):
			instance._QRCODE = False
		else:
			instance._QRCODE = True
 
models.signals.pre_save.connect(urlqrcode_pre_save_compaign, sender=Compaign)
 
def urlqrcode_post_save_compaign(sender, instance, **kwargs):
	
	if instance._QRCODE:
		instance._QRCODE = False
		if instance.qr_image:
			instance.qr_image.delete()
		qr = QRCode(4, QRErrorCorrectLevel.L)
		qr.addData(instance.url)
		qr.make()
		image = qr.makeImage()
 
		#Save image to string buffer
		image_buffer = StringIO()
		image.save(image_buffer, format='JPEG')
		image_buffer.seek(0)
		 
		#Here we use django file storage system to save the image.
		file_name = 'UrlQR_%s.jpg' % instance.compaign_id
		file_object = File(image_buffer, file_name)
		content_file = ContentFile(file_object.read())
		instance.qr_image.save(file_name, content_file, save=True)
 
models.signals.post_save.connect(urlqrcode_post_save_compaign, sender=Compaign)

################################ Retrieve Code ########################################

def companyProfile (request):
    com = Company.objects.get(company_id=2)
    dic={}
    #dic['MEDIA_ROOT']=settings.MEDIA_URL
    return render_to_response('profiles/companyprofile.html',{'companyData': com})

def listAllCompanies (request):
    com = Company.objects.all()
    dic={}
    return render_to_response('profiles/listallcompanies.html',{'companyData': com})
    
def productProfile (request):
    #com=Company.objects.get(company_id=2)
    pro = Product.objects.filter(Company=2)
    dic={}
    return render_to_response('profiles/productprofile.html',{'pro': pro})
    
def listAllProducts (request):
    pro = Product.objects.all()
    dic={}
    return render_to_response('profiles/listallproducts.html',{'pro': pro})


def compaignProfile (request):
    #com=Company.objects.get(company_id=2)
    comp = Compaign.objects.filter(product=3)
    dic={}
    return render_to_response('profiles/compaignprofile.html',{'comp': comp})
    
def listallCompaignes (request):
    comp = Compaign.objects.all()
    dic={}
    return render_to_response('profiles/listallCompaignes.html',{'comp': comp})

