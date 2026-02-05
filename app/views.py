import csv
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import IntegrityError
from .models import RetailData
from .forms import CsvUploadForm, AnnotationForm

# Store the data from a given CSV file as SQLite
def upload_csv(request):
    if request.method == 'POST':
        form = CsvUploadForm(request.POST, request.FILES)

        if form.is_valid():
            csv_file = request.FILES['csv_file']
            csv_lines = csv.DictReader(csv_file.read().decode('utf-8').splitlines())
            
            # Track for notification
            created_count = 0
            skipped_count = 0
            
            for row in csv_lines:
                try:
                    RetailData.objects.create(
                        merchant = row['merchant'],
                        sku = row['sku'],
                        country = row['productcountry']
                    )

                    created_count += 1

                except IntegrityError:
                    # TO DO: Add better error handling for actual complex files/cases; okay only for this one simple file
                    skipped_count += 1
            
            messages.success(request, f'🎉 Created {created_count} record(s) and skipped {skipped_count} duplicate(s)')
            return redirect('annotation_list')
    else:
        form = CsvUploadForm() # Pre-upload and before user first enters page
    
    return render(request, 'upload_csv.html', {'form': form})

# Display all uploaded data and enable annotation edits
def annotation_list(request):
    # Only when retailer AND segment are user-edited can the record be considered a "Completed Annotation"
    # TO DO: Add a third condition for records "In Progress" in prod
    # TO DO: Optomize for larger data sets (pk__in is slower for anything bigger than this one file)
    annotated_data = RetailData.objects.exclude(retailer__isnull = True).exclude(retailer = '').exclude(segment__isnull = True).exclude(segment = '')
    unannotated_data = RetailData.objects.exclude(pk__in = annotated_data)
    
    return render(request, 'annotation_list.html', {
        'unannotated_data': unannotated_data,
        'annotated_data': annotated_data
    })

# Displays annotation and enables editing
def edit_annotation(request, id):
    retail_data = get_object_or_404(RetailData, pk = id)
    
    if request.method == 'POST':
        form = AnnotationForm(request.POST, instance = retail_data)

        if form.is_valid():
            form.save()
            messages.success(request, 'Annotation saved successfully.')
            return redirect('annotation_list')
    else:
        form = AnnotationForm(instance = retail_data)
    
    return render(request, 'edit_annotation.html', {'form': form, 'retail_data': retail_data})