from django import forms
from .models import *

class Computer(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['cid', 'name', 'brand', 'price', 'stock', 'description','category','images']
        widgets = {
            'cid': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'step': '0.25'}),
            'description': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
           
            'category': forms.Select(attrs={'class': 'form-control'}),
            'images': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'cid': 'รหัสสินค้า',
            'name': 'ชื่อสินค้า',
            'brand': 'ยี่ห้อ',
            'price': 'รุ่น',
            'stock': 'ราคา',
            'description': 'คงเหลือ',
           
            'category': 'ประเภทสินค้า',
            'images':'รูปภาพ',
        }