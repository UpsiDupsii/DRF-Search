from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Empl_Details
from .serializers import Empl_DetailsSerializer

# Create your views here.
def index(request):
    query = request.GET.get('search', default='')
    queries = (Empl_Details.objects.filter(emp_id__icontains=query)) | (Empl_Details.objects.filter(name__icontains=query)) | (Empl_Details.objects.filter(salary__icontains=query))
    context = {
        'queries': queries,
        'search' : query,
        
    }
    if query == '':
        return render (request, 'index.html', context)
    return render(request, 'index.html', context)

@api_view(['GET'])
def show(request):
    emp_details = Empl_Details.objects.all().values()
    serializer = Empl_DetailsSerializer(emp_details, many=True)
    serialized_data = serializer.data
    return Response({'data':serialized_data})

@api_view(['POST'])
def add(request):
    emp_details = Empl_DetailsSerializer(data = request.data)
    if emp_details.is_valid():
        emp_details.save()
        return Response({'data':emp_details.data})
    else:
        return Response({'status': 201, 'message' : "Error Occured"})
    
@api_view(['DELETE'])
def delete(request, id):
    emp_details = Empl_Details.objects.get(id=id)
    emp_details.delete()
    return Response(f"One Record with ID {id} is deleted from the database")

@api_view(['PUT'])
def update(request, id):
    emp_details = Empl_Details.objects.get(id = id)
    serializer = Empl_DetailsSerializer(instance= emp_details, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({'data':serializer.data})