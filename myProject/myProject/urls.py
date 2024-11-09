from ManageCash.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('register/', register, name='register'),
    path('', signin, name='signin'),
    path('signout/', signout, name='signout'),
    
    
    
    path('dashboard/', dashboard, name='dashboard'),
    
    path('profile/', profile, name='profile'),
    
    path('add_cash/', add_cash, name='add_cash'),
    path('cash-list/', cash_list, name='cash_list'),
    path('update-cash/<int:cash_id>/', update_cash, name='update_cash'),
    path('delete-cash/<int:cash_id>/', delete_cash, name='delete_cash'),
    
    path('add_expense/', add_expense, name='add_expense'),
    path('expense-list/', expense_list, name='expense_list'),
    path('update-expense/<int:expense_id>/', update_expense, name='update_expense'),
    path('delete-expense/<int:expense_id>/', delete_expense, name='delete_expense'),
]
