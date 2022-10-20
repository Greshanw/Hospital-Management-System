from django.shortcuts import render, redirect, reverse
from .models import Inventory
from django.http import HttpResponse
from .form import InventoryCreateForm, InventorySearchForm, InventoryUpdateForm 
from django.contrib import messages
import csv
import cv2
from pyzbar.pyzbar import decode
from pyzbar.pyzbar import decode
from pyzbar import pyzbar
import barcode
from barcode.writer import ImageWriter
from barcode import EAN13
from io import BytesIO
from django.views.decorators.http import require_POST, require_GET, require_safe

# Create your views here.

# define what will be displayed in home.html

redirect_url = '/medicines'

@require_safe
def home(request):
    # title of the view
    title = 'Dashboard of the Inventory'
    queryset = Inventory.objects.all()

    # inside the context stores the variables
    # these variables can be called from the html page
    context = {
        "title": title,
        "Inventory": Inventory,
        "queryset": queryset
    }
    # return the html page and the context
    return render(request, "Ihome.html", context)


def list_item(request):
    title = 'List of Medical Products'
    form = InventorySearchForm(request.POST or None)
        
    # assign all the objects in the Inventory to the queryset
    queryset = Inventory.objects.all()
    
    if request.method == 'POST': # if press the search button
        queryset = Inventory.objects.filter(Medicine_name__icontains=form['Medicine_name'].value())

    context = {
        "title": title,
        "form": form,
        "queryset": queryset,
    }
    return render(request, "InventoryList.html", context)


def insert_product(request):
    form = InventoryCreateForm(request.POST or None)
    if form.is_valid(): # checking the validation of form data
        form.save() # save data in database
        messages.success(request, 'Successfully inserted the Medical product')
        # this allow you the page to be redirected to another after saving data
        return redirect(redirect_url)
    context = {
        "form": form,
        "title": "Insert Product",
    }
    return render(request, "InsertProduct.html", context)

@require_safe
def generate_report(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="List of Medicines.csv"'
    writer = csv.writer(response)
    writer.writerow([ 'Medicine NAME', 'QUANTITY',
                        'Net PRICE', 'Vendor', 'Last Updated Date'])
    queryset = Inventory.objects.all().values_list('Medicine_name', 'quantity',
                        'Net_price', 'Vendor', 'last_updated')
    
    for stock in queryset:
        writer.writerow(stock)
    return response


# view to updating product details

def update_product(request, pk):
    queryset = Inventory.objects.get(id=pk)
    form = InventoryUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = InventoryUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            # message notify after updating
            messages.success(
                request, 'Successfully Updated the Product Details')
            return redirect(redirect_url)

    context = {
        'form': form,
        "title": "Update  Item",
    }
    return render(request, 'InsertProduct.html', context)


#view to delete a product from the database.

def delete_items(request, pk):
    queryset = Inventory.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'Successfully Deleted the product')# message notify after deleting
        return redirect(redirect_url)
    return render(request, 'delete_items.html')

class scbar:
    def __init__(self):
        self.barco_id = " "

    def setbarco(self, bid):
        self.barco_id = bid

    def getbarco(self):
        return self.barco_id


sc = scbar()

#barcode decoding function

def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        # 1 - here decoding the information from barcode, then drawing a rectangle around it.
        # from this we can identify that machine has detected the barcode.
        barcode_stri = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # 2 - adding text/ product ID on top of the rectangle that was created
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_stri, (x + 6, y - 6),
                    font, 2.0, (255, 255, 255), 1)
        # 3 - for the testing purpose saving the ID in a text file.
        with open("barcode_result.txt", mode='w') as file:
            file.write("Detected Barcode:" + barcode_stri)

        print(barcode_stri)
        barco_id = int(barcode_stri)
        barco_id = barco_id // 10
        sc.setbarco(str(barco_id))
        print(sc.getbarco())
    return frame

# main function will turn on the camera then call the decoding function.
@require_safe
def main(request):
    # 1- turn on the camera using OpenCV
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    # 2 - here , runs a while loop to keep running decoding function
    # unitl the Esc key is pressed.
    while ret:
        ret, frame = camera.read()
        frame = read_barcodes(frame)
        cv2.imshow('Barcode/QR code reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    # 3 - releasing the camera and closing the app window,
    camera.release()
    cv2.destroyAllWindows()

    # redirect to list_itemb view.
    return redirect ('product_Scaned')

#4 - calling the main function. name is used to exeucte some code if the file runs directly
if __name__ == '__main__':
    main()


@require_safe
def product_scaned(request):
    title = 'List of Medical Products'
    form = InventorySearchForm(request.POST or None)
        
    # assign all the objects in the Inventory to the queryset
    queryset = Inventory.objects.filter(Product_ID=sc.getbarco())
    
    if request.method == 'POST': # if press the search button
        queryset = Inventory.objects.filter(Medicine_name__icontains=form['Medicine_name'].value())

    context = {
        "title": title,
        "form": form,
        "queryset": queryset,
    }
    return render(request, "InventoryList.html", context)