
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, AddCashForm, ExpenseForm
from .models import AddCash, Expense
from django.contrib import messages

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('dashboard') 
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')


@login_required
def signout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('signin')



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('signin') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def profile(request):
    cash_entries = AddCash.objects.filter(user=request.user)
    expenses = Expense.objects.filter(user=request.user)
    return render(request, 'profile.html', {'cash_entries': cash_entries, 'expenses': expenses})

@login_required
def dashboard(request):
    cash_entries = AddCash.objects.filter(user=request.user)
    expenses = Expense.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'cash_entries': cash_entries, 'expenses': expenses})

@login_required
def add_cash(request):
    if request.method == 'POST':
        form = AddCashForm(request.POST)
        if form.is_valid():
            cash = form.save(commit=False)
            cash.user = request.user
            cash.save()
            return redirect('dashboard')
    else:
        form = AddCashForm()
    return render(request, 'add_cash.html', {'form': form})


@login_required
def cash_list(request):
    cash_entries = AddCash.objects.filter(user=request.user)
    return render(request, 'cash_list.html', {'cash_entries': cash_entries})


@login_required
def update_cash(request, cash_id):
    cash = get_object_or_404(AddCash, id=cash_id, user=request.user)
    if request.method == 'POST':
        form = AddCashForm(request.POST, instance=cash)
        if form.is_valid():
            form.save()
            return redirect('cash_list')
    else:
        form = AddCashForm(instance=cash)
    return render(request, 'update_cash.html', {'form': form})


@login_required
def delete_cash(request, cash_id):
    cash = get_object_or_404(AddCash, id=cash_id, user=request.user)
    if request.method == 'POST':
        cash.delete()
        return redirect('cash_list')
    return render(request, 'confirm_delete.html', {'item': cash})


@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('dashboard')
    else:
        form = ExpenseForm()
    return render(request, 'add_expense.html', {'form': form})



@login_required
def expense_list(request):
    expense_entries = Expense.objects.filter(user=request.user)
    return render(request, 'expense_list.html', {'expense_entries': expense_entries})


@login_required
def update_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'update_expense.html', {'form': form})


@login_required
def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    return render(request, 'confirm_delete.html', {'item': expense})