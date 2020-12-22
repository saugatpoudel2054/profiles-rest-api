from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPIView(APIView):
    '''Sample basic API View'''

    def get(self, request, format=None):
        '''Returns Basic get request response'''
        d = [1,2,3,4,5]
        return Response({'message':'Success', 'list':d})
        
