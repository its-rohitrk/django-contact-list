from django.shortcuts import render,redirect
from .models import Contact
# Create your views here.
def index(request):
    contacts = Contact.objects.all()
    search_input = request.GET.get('search-area')
    if search_input:
        contacts = Contact.objects.filter(full_name__icontains=search_input)
    else:
        contacts = Contact.objects.all()
        search_input =''

    return render(request,'index.html',{'contacts':contacts,'search_input':search_input})
def addcontact(request):
    if request.method== 'POST':
        new_contact = Contact(
         full_name = request.POST['fullname'],
         relationship = request.POST['relationship'],
         enail = request.POST['email'],
         phone = request.POST['phone-number'],
         address = request.POST['address']

        )
        new_contact.save()
        return redirect('index')
    return render(request,'new.html')


def contactprofile(request,pk):
    contact = Contact.objects.get(id =pk)
    return render(request,'contact-profile.html',{'contact':contact})

def editcontact(request,pk):
    contact = Contact.objects.get(id=pk)
    if request.method=='POST':
        contact.full_name = request.POST['fullname']
        contact.relationship = request.POST['relationship']
        contact.phone = request.POST['phone-number']
        contact.enail = request.POST['email']
        contact.address = request.POST['address']
        contact.save()

        return redirect('/profile/'+str(contact.id))

    return render(request,'edit.html',{'contact':contact})


def deletecontact(request,pk):
    contact = Contact.objects.get(id=pk)
    if request.method=='POST':
        contact.delete()

        return redirect('/')

    return render(request,'delete.html',{'contact':contact})