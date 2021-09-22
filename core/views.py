from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import searchModel
from .serializers import APISerializer

'''
input value converted to list data and remove all space
also remove space and convert it integer data.
then sort as descending order
after sort i check search value available or not, if available
then i passed context as result True otherwise False
then i convert list to string and save to database within
current user.
'''

@login_required(login_url='login')
def HomeView(request):
    context = {}
    context['result'] = ''
    if request.method == 'POST':
        data = request.POST
        input_value = [int(value.strip()) for value in data['input'].split(',')]
        search = int(data['search'].strip())
        input_value.sort(reverse=True)
        if search in input_value:
            context['result'] = 'True'
        else:
            context['result'] = 'False'
        input_value = ', '.join(str(value) for value in input_value)
        object = searchModel.objects.create(input_value=input_value, user=request.user)
        object.save()
    return render(request, 'main.html', context)



# passed all objects to serializer for convert json data
# objects filtered by current logged in user.

class dataAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        objects = searchModel.objects.filter(user=request.user)
        return Response({
            'status': 'success',
            'user': request.user.id,
            'payload': APISerializer(objects, many=True).data
        })
