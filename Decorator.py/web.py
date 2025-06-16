from login import login_required

def home_page(name,status):
    print("home page")

@login_required
def order_page(name,status):
    print("order_page")

@login_required
def update_profile(name,status):
    print('update profile')

@login_required
def contact_page(name,status):
    print("contact page")

order_page("rg",True)
order_page("rg",False)
