from rest_framework import generics
from contactapp.models import Contact
from .serializers import ContactSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def contact_list(request):
    contacts = Contact.objects.all()
    serializer = ContactSerializer(contacts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def contact_detail(request, id):
    contacts = Contact.objects.get(id=id)
    serializer = ContactSerializer(contacts, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def contactCreate(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
