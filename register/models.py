from django.db import models
from django.forms import ModelForm
from django.core.files import File
from django.core.files.base import ContentFile

from PyQRNative import *
 
from cStringIO import StringIO

################ Test Retrieve Image ################
	#def qr_code(self):
	#	return '%s' % self.qr_image.url
	#qr_code.allow_tags = True
#####################################################

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name=models.CharField("Company Name", max_length=100, unique=True)
    phone=models.IntegerField("Company Phone",max_length=100)
    email=models.EmailField ("Company Email",max_length=100,unique=True)
    description=models.CharField("Company Description",max_length=255,unique=True)
    establishedDate=models.DateField("Enter Established Date")
    password=models.CharField("Enter Password",max_length=50 )
    company_photo=models.ImageField("Company Photo",max_length=100,upload_to="images")
    def __unicode__(self):
      return '%s %d %s %s %s %s' % (self.company_name,self.phone,self.email,self.description,self.password,self.company_photo)

class Product (models.Model):
    product_id = models.AutoField(primary_key=True)
    Company=models.ForeignKey(Company)
    product_name=models.CharField("Product Name", max_length=30, unique=True)
    description=models.CharField("Product Description",max_length=255)
    product_price=models.IntegerField("Price",max_length=50)
    product_price_currency=models.CharField("Price Currency", max_length=100)
    url = models.URLField("QRcode URL", max_length=150)
    qr_image = models.ImageField(upload_to="static/img/qrcode/product",height_field="qr_image_height",width_field="qr_image_width",null=True,blank=True,editable=False)
    qr_image_height = models.PositiveIntegerField(null=True, blank=True, editable=False)
    qr_image_width = models.PositiveIntegerField(null=True, blank=True, editable=False)
    product_image=models.ImageField("Product's image", max_length=255,upload_to="images")
    def __unicode__(self):
        return '%s %s %s %s %s %s' % (self.product_name,self.description,self.product_price_currency,self.product_image,self.product_image,self.qr_image.url)
    __unicode__.allow_tags = True
        
class Compaign(models.Model):
	compaign_id=models.AutoField(primary_key=True)
	product=models.ForeignKey(Product)
	company=models.ForeignKey(Company)
	compaign_name=models.CharField("Compaign Name",max_length=250,unique=True)
	description=models.CharField("Compaign Description",max_length=255)
	compaign_month=models.CharField("Compaign Month",max_length=50)
	url = models.URLField("QRcode URL", max_length=150)
	qr_image = models.ImageField(upload_to="static/img/qrcode/compaign",height_field="qr_image_height",width_field="qr_image_width",null=True,blank=True,editable=False)
	qr_image_height = models.PositiveIntegerField(null=True, blank=True, editable=False)
	qr_image_width = models.PositiveIntegerField(null=True, blank=True, editable=False)
	def __unicode__(self):
		return '%d %d %d %s %s %s %s' % (self.compaign_id,self.product_id,self.company_id,self.compaign_name,self.description,self.compaign_month,self.qr_image.url)
	__unicode__.allow_tags = True

class Newsletter(models.Model):
	subscriber_id=models.AutoField(primary_key=True)	
	subscriber_email=models.EmailField ("Subscriber Email",max_length=100,unique=True)
	def __unicode__(self):
		return '%s' % (self.subscriber_email)

class CompanyForm(ModelForm):
	class Meta:
		model = Company

class ProductForm(ModelForm):
	class Meta:
		model = Product
		#exclude=('Company','qr_image')

class CompaignForm(ModelForm):
	class Meta:
		model = Compaign
		#exclude=('company','product', 'qr_image')

class CompanyLogInForm(ModelForm):
	class Meta:
		model = Company
		fields = ('company_name', 'password')
		#field_args = { {"product_name" : {"error_messages" : {"required" : "Please insert product name!"}}}, {"description" : {"error_messages" : {"required" : "Please insert the product's description!"}}} }
