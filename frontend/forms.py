# from django import forms
# from .models import Product, Bid

# class ProductForm(forms.ModelForm):
#     closing_time = forms.DateField(
#         input_formats=['%Y-%m-%d'],  # Ensure this matches the format users will input
#         widget=forms.DateInput(attrs={
#             'class': 'form-control date-picker',
#             'placeholder': 'YYYY-MM-DD',
#             'type': 'date'  # This will use the browser's date picker
#         })
#     )
    
#     class Meta:
#         model = Product
#         fields = ['productname', 'content', 'image', 'closing_time', 'starting_price']

# class BidForm(forms.ModelForm):
#     class Meta:
#         model = Bid
#         fields = ['bid_price',]

#     def clean_bid_price(self):
#         bid_price = self.cleaned_data.get('bid_price')
#         product = self.instance.product
#         if bid_price <= product.starting_price:
#             raise forms.ValidationError("Bid must be greater than starting price.")
#         if product.bids.exists() and bid_price <= product.bids.latest('bid_price').bid_price:
#             raise forms.ValidationError("Bid must be greater than the last bid.")
#         return bid_price


from django import forms
from .models import Product, Bid

class ProductForm(forms.ModelForm):
    closing_time = forms.DateField(
        input_formats=['%Y-%m-%d'],  # Ensure this matches the format users will input
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'placeholder': 'YYYY-MM-DD',
            'type': 'date'  # This will use the browser's date picker
        })
    )

    class Meta:
        model = Product
        fields = ['productname', 'content', 'image', 'closing_time', 'starting_price']

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['bid_price']

    def clean_bid_price(self):
        bid_price = self.cleaned_data.get('bid_price')
        product = self.instance.product
        if bid_price <= product.starting_price:
            raise forms.ValidationError("Bid must be greater than starting price.")
        if product.bids.exists() and bid_price <= product.bids.latest('created_at').bid_price:
            raise forms.ValidationError("Bid must be greater than the last bid.")
        return bid_price

