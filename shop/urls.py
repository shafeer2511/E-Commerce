"""
Here's an overview of the process flow for rendering a template in Django when a URL is entered:

1. **URL Entered**: The user enters a URL in the browser, sending an HTTP request to the Django server.

2. **URL Dispatcher**: Django's `urls.py` file matches the requested URL pattern to a specific view function.

3. **View Function**: The matched view function processes the request and calls `render()` to generate the response.

4. **Template Rendering**:  
   - `render()` looks for the specified template file.
   - It combines the template with any provided context data to generate HTML.

5. **Response Sent**: Django sends the rendered HTML back to the user's browser as an HTTP response.

6. **Browser Displays**: The browser displays the rendered HTML page to the user. 

"""
from django.contrib import admin
from django.urls import path
from . import views  ## '.' means current project directory 
urlpatterns = [
    # path('admin/',admin.site.urls),
#     Purpose of the 'name' Parameter
# Template Usage: The name allows you to use the {% url %} template tag to generate URLs
    path('',views.home,name="home"),
    path('login/',views.login_page,name='login'),
    path('logout/',views.logout_page,name='logout'),
    path('register/',views.register,name="register"),
    path('cart',views.cart_page,name='cart'),
    path('remove_cart/<str:cid>',views.remove_cart,name='remove_cart'),
    path('collection/',views.collection,name='collection'),
    path('collection/<str:name>',views.collectionview,name='collection'),
    path('collection/<str:cname>/<str:pname>',views.product_details,name='product_details'),
    path('addtocart',views.add_to_cart,name='addtocart')
]
