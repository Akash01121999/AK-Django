from django.urls import path
from .import views
app_name='dashboard'
urlpatterns = [
    path('',views.first,name='home'),
    path('log',views.logi,name='loginpg'),
    path('loginuser',views.logver,name='signin'),
    path('create',views.adduserfm,name="regpage"),
    path('reg',views.addnuser, name="Register"),
    path('pset',views.passet,name='setpasw'),
    path('pro',views.pro,name='profile'),
    path('acc',views.account,name='accounts'),
    path('loan',views.loan,name='loans'),
    path('deppage',views.deppage,name='deppage'),
    path('dep',views.deposite,name='depose'),
    path('trans',views.transfer,name='trans'),
    path('res',views.resetpg,name='res'),
    path('reset',views.reset,name='rst'),
    path('lgout',views.logout,name='lgout'),
    path('statepg',views.statementpg,name='statepg'),
    path('get',views.statement,name='state'),
    path('calu',views.calu,name='calu'),
    path('intro',views.intro,name='backfirst'),
    path('about',views.about,name='about'),
    path('complaint',views.complaint,name='complaint'),
    path('contact',views.contact1,name='contact'),
    path('comp',views.post_comp,name='com')
    
    
    
    
]

