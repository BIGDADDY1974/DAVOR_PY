from django.shortcuts import render

def index(request):
    return render(request,'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html', {'content':['If you would like to contact me, please email me or visit my sites.',
                                                              'svilar@beotel.rs.','davorsvilar@gmail.com.','https://www.facebook.com/davor',
                                                              'Profilehttps://rs.linkedin.com/in/davorsvilar','http://svilardavor.tk/',
                                                              'http://davor.smallideafactory.com/']})

# Create your views here.
