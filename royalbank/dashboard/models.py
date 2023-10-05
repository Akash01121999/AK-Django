from django.db import models

# Create your models here.

class user(models.Model):
    userid=models.CharField(max_length=6,verbose_name="USER ID",default='0')
    acc_no=models.CharField(max_length=11,verbose_name='Account No',default='0')
    first_name=models.CharField(max_length=100 ,null=True,verbose_name="First Name",default='0')
    last_name=models.CharField(max_length=100,null=True,verbose_name="Last Name",default='0')
    dob=models.DateField(verbose_name="Date of Birth",null=True,default='0')
    gender=models.CharField(verbose_name="Gender",max_length=1,default='0')
    password=models.CharField(max_length=20,verbose_name="PASSWORD",default='0')
    ifsc=models.CharField(max_length=50,verbose_name="IFSC",default='0')
    acc_type=models.CharField(max_length=50,verbose_name="Account Type",default='0')
    balan=models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Balance",default=0)
    phone=models.CharField(max_length=10,verbose_name="Phone No",default='0')
    email=models.EmailField(verbose_name="Email Id",default='0')
    location=models.CharField(max_length=100,verbose_name="Location",default='0')
    loan=models.CharField(max_length=50,null=True,verbose_name="Type of Loans",default="one")
    cr_type=models.CharField(max_length=50,null=True,verbose_name="Card Type",default="one")
    
    
    
    def __str__(self):
        return self.first_name

class trlist(models.Model):
    acc_no=models.CharField(max_length=11,verbose_name='Account No',default='0')
    tr_amount=models.DecimalField(max_digits=20,decimal_places=2,verbose_name="Amount to Transfer",default='0')
    balan=models.DecimalField(max_digits=20,decimal_places=2,verbose_name="Balance",default='0')
    d_t=models.DateTimeField(verbose_name="Transaction Date",default='0')
    to_acc=models.CharField(max_length=11,verbose_name="To Account",default='0')
    
    def __str__(self):
        demo=user.objects.all()
        for i in demo:
            if self.acc_no in i.acc_no:
                return i.first_name
            
class contact(models.Model):
    ad=models.CharField(max_length=250,default=0)
    ph1=models.CharField(max_length=250,default=0)
    ph2=models.CharField(max_length=250,default=0)
    ph3=models.CharField(max_length=250,default=0)
    lp=models.CharField(max_length=250,default=0)
    em=models.CharField(max_length=250,default=0)
    def __str__(self):
        return self.ad
    
    
class complaint(models.Model):
    com_letter=models.CharField(max_length=250,default=0)
    
    