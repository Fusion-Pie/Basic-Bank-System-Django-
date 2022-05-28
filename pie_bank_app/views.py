from asyncio.windows_events import NULL
import email
from multiprocessing import context
from pydoc import doc
from re import T
from unicodedata import name
from django.dispatch import receiver
from django.shortcuts import redirect, render, HttpResponse
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserChangeForm
import random as rand

from django.contrib.auth.models import User
from pie_bank_app.models import *

# Create your views here.
def index(request):
    if request.method == 'POST':

        # If the user already has username and password
        if  request.POST.get('btn_name') == 'Registered User':
            return render(request,'registered_user.html')

        elif request.POST.get('btn_name') == 'Log in':
            user  = authenticate(username = request.POST.get('username'), password = request.POST.get('password'))

            if user is not None:
                # A backend authenticated the credentials
                id = Bank_user.objects.filter(Customer_id = user.id)

                if id.exists() == False:
                    ifsc_val = list(Bank_user.objects.values_list('IFSC'))

                    ifsc_code = 'PBIIN'

                    for i in range(5):
                        num = str(rand.randint(0,9))
                        ifsc_code += num
                    
                    while(ifsc_code in ifsc_val):
                        ifsc_code = 'PBIIN'
                        for i in range(5):
                            num = str(rand.randint(0,9))
                            ifsc_code += num

                    bank_user = Bank_user(Customer_id = user.id, IFSC = ifsc_code, Balance = NULL)
                    bank_user.save()

                login(request, user)
                return redirect('/home/')
            else:
                # No backend authenticated the credentials
                messages.error(request,'Credentials does not match')
                return redirect('/')


        # If user want to create new user
        elif  request.POST.get('btn_name') == 'New User':
            return render(request,'new_user.html')

        # Creating new user
        elif  request.POST.get('btn_name') == 'Create User':
            username = request.POST.get('username')
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = User.objects.create_user(username,email, password)
            user.email = email
            user.first_name = firstname
            user.last_name = lastname
            user.save()

            messages.success(request,'User created successfully!! Please log in as a registered user')

            return render(request,'index.html')

    return render(request,'index.html')

def home(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if  request.POST.get('btn_name') == 'Logout':
                logout(request)
                messages.success(request,"Logged Out Successfully")
                return redirect('/')
        
        else:
            return render(request, 'homePage.html')

    else:
        return  redirect('/')

def about(request):
    if request.user.is_authenticated:
        return render(request, 'about.html')
    
    else:
        return redirect('/')
    
    

def contact(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            date = datetime.today()

            contact = Contact(name = name, email = email, message = message, date = date)
            contact.save()
            
            messages.success(request, 'Thank you for messaging us! We got your message')
    
        else:
            return render(request, 'contact.html')

    else:
        return redirect('/')


def details(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            bal = request.POST.get('add_value')

            if (bal != None):
                up_bal = Bank_user.objects.filter(Customer_id = request.user.id)

                for i in up_bal:
                    old_bal = i.Balance
                
                up_bal.update(Balance = float(bal) + old_bal)
            

        user_details = User.objects.filter(username = request.user)
        user_bank_details = Bank_user.objects.filter(Customer_id = request.user.id)
        
        for data in user_details:
            uname = data.username
            fname = data.first_name
            lname = data.last_name
            email = data.email
            join_month = data.date_joined

        ifsc = ''
        balance = 0
        
        for data in user_bank_details:
            ifsc = data.IFSC
            balance = data.Balance
       
        context = {'uname': uname, 
                    'fname': fname,
                    'lname': lname,
                    'email': email,
                    'join_month': join_month,
                    'ifsc': ifsc,
                    'balance': balance,
                    }
        
        return render(request,'user_details.html',context)

    else:
        return redirect('/')


def payment(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            receiver_ifsc = request.POST.get('ifsc_value')

            customer = Bank_user.objects.filter(IFSC = receiver_ifsc)

            amount = float(request.POST.get('amount_value'))

            date = datetime.today()

            if customer.exists():
                curr_user = Bank_user.objects.filter(Customer_id = request.user.id)

                for i in curr_user:
                    curr_bal = i.Balance
                    curr_ifsc = i.IFSC

                if curr_bal >= amount:
                    curr_user.update(Balance = curr_bal - amount)

                    for i in customer:
                        old_bal = i.Balance

                    customer.update(Balance = old_bal + amount)

                    trans_obj = Transction(Transction_from = curr_ifsc, Transction_to = receiver_ifsc, Amount = amount, date = date,status = 'Success')
                    trans_obj.save()

                    messages.success(request, "Transaction Completed")
                
                else:
                    messages.error(request, "Balance Low")

            else:
                receiver_ifsc = request.POST.get('ifsc_value')

                curr_user = Bank_user.objects.filter(Customer_id = request.user.id)

                for i in curr_user:
                    curr_ifsc = i.IFSC

                trans_obj = Transction(Transction_from = curr_ifsc, Transction_to = receiver_ifsc, Amount = amount, date = date,status = 'Failed')
                trans_obj.save()
                messages.error(request,"Something went wrong!")


        return render(request, 'payment.html')



def history(request):
    if request.user.is_authenticated:
        curr_user = Bank_user.objects.filter(Customer_id = request.user.id)

        for i in curr_user:
            check_ifsc = i.IFSC

        trans = Transction.objects.filter(Transaction_from = check_ifsc)

        if trans.exists():

            context =  {
                'trans': trans
            }

            return render(request,'history.html',context)

        else:
            return render(request, 'history.html',context = {'msg': 'no'})
