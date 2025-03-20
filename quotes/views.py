from django.shortcuts import render, redirect, get_object_or_404
from .models import Quote, QuoteItem
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa  # PDF generation library


def create_quote(request):
    if request.method == 'POST':
        # Fetch POST data
        client_name = request.POST.get('client_name')
        client_address = request.POST.get('client_address')
        project_name = request.POST.get('project_name')
        items = request.POST.getlist('item_name[]')

        # Validate required fields
        if not client_name or not client_address or not project_name or not items:
            return HttpResponse("Missing required fields", status=400)

        # Create the Quote
        quote = Quote.objects.create(
            client_name=client_name,
            client_address=client_address,
            project_name=project_name
        )

        # Add items to the Quote
        for i in range(len(items)):
            QuoteItem.objects.create(
                quote=quote,
                item_name=items[i],
                description=request.POST.getlist('description[]')[i],
                subcontractor=request.POST.getlist('subcontractor[]')[i],
                quantity=int(request.POST.getlist('quantity[]')[i]),
                unit_price=float(request.POST.getlist('unit_price[]')[i])
            )

        return redirect('quotes:existing_quotes')


    return render(request, 'quotes/create_quote.html')


def existing_quotes(request):
    quotes = Quote.objects.all()
    return render(request, 'quotes/existing_quotes.html', {'quotes': quotes})


def download_quote(request, pk):
    try:
        # Fetch the quote and its related items
        quote = get_object_or_404(Quote, pk=pk)
        items = quote.items.all()

        # Calculate the total price for the quote
        total_price = sum(item.total_cost() for item in items)

        # Render the HTML template with context
        template = get_template('quotes/quote_pdf.html')
        html = template.render({'quote': quote, 'items': items, 'total_price': total_price})

        # Create PDF with xhtml2pdf
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="quote_{pk}.pdf"'

        # Use pisa to generate the PDF
        pisa_status = pisa.CreatePDF(html, dest=response)

        # Check for errors during PDF generation
        if pisa_status.err:
            return HttpResponse(f"An error occurred while generating the PDF.", status=500)

        return response

    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}", status=500)
    
def delete_all_quotes(request):
    if request.method == "POST":  # Allow POST method only for security
        Quote.objects.all().delete()
        return redirect('quotes:existing_quotes')
    return HttpResponse("Method not allowed", status=405)    

def delete_quote(request, pk):
    if request.method == 'POST':
        quote = get_object_or_404(Quote, pk=pk)
        quote.delete()
        return redirect('quotes:existing_quotes')
    return HttpResponse("Method not allowed", status=405)
