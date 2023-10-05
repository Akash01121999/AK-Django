from django.contrib import admin
from .models import user,trlist,contact,complaint
# Register your models here.

class Clients(admin.ModelAdmin):
    list_display=('id','first_name','last_name','gender','userid','acc_no','password','ifsc','acc_type','balan','phone','email','location','loan','cr_type','dob')
admin.site.register(user,Clients)
class statement(admin.ModelAdmin):
    list_display=('acc_no','to_acc','tr_amount','balan','d_t')
class conadmin(admin.ModelAdmin):
    list_display=('ad','ph1','ph2','ph3','lp','em')
    
admin.site.register(contact,conadmin)
admin.site.register(trlist,statement)

admin.site.register(complaint)