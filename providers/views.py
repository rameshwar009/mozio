from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.views import APIView
from .models import Provider, ProviderPolygon
from . serializers import ProviderSerializer, PolygonSerializer


# Create your views here.
class CreateProvider(APIView):
	model = Provider 
	serializer_class = ProviderSerializer

	def post(self, request):
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)

	def get(self, request):
		providers = Provider.objects.all()
		serializer = self.serializer_class(providers, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


class ProviderUpdate(APIView):
	model = Provider
	serializer_class = ProviderSerializer

	def put(self,request,pk):
		try:
			provider = Provider.objects.get(id=pk)
			serializer = self.serializer_class(provider,data=request.data)
			if serializer.is_valid(raise_exception=True):
				serializer.save()
				return Response(serializer.data,status=status.HTTP_200_OK)
		except :
			return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	def get(self, request,pk):
		try:
			provider = Provider.objects.get(id=pk)
			serializer = self.serializer_class(provider)
			return Response(serializer.data, status=status.HTTP_200_OK)
		except:
			return Response({'error':'ObjectDoesnotExist'},status=status.HTTP_400_BAD_REQUEST)
		

	def delete(self, request,pk):
		try:
			provider = Provider.objects.get(id=pk)
			provider.delete()
		except:
			return Response({'error':'ObjectDoesnotExist'}, status=status.HTTP_400_BAD_REQUEST)
		return Response({'message':'Done'}, status=status.HTTP_200_OK)


def geojson_format(data):
	poly = data['poly']
	obj = "POLYGON((" + data['poly'] +"))"
	data['poly']=obj
	return data


class CreatePolygon(APIView):
	model = ProviderPolygon
	serializer_class = PolygonSerializer

	def post(self,request):
		data = geojson_format(request.data)
		serializer = self.serializer_class(data=data)
		
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)

	def get(self, request):
		polygons = ProviderPolygon.objects.all()
		serializer = self.serializer_class(polygons,many=True)
		return Response(serializer.data,status=status.HTTP_200_OK)


class PolygonUpdate(APIView):
	model = ProviderPolygon
	serializer_class = PolygonSerializer

	def get(self, request, pk):
		try:
			polygon = ProviderPolygon.objects.get(id=pk)
			serializer = self.serializer_class(polygon)
			return Response(serializer.data, status=status.HTTP_200_OK)
		except:
			return Response({'error':'ObjectDoesnotExist'},status=status.HTTP_400_BAD_REQUEST)

	def put(self, request, pk):
		import ipdb;ipdb.set_trace()
		try:
			polygon = ProviderPolygon.objects.get(id=pk)
		except:
			return Response({'error':'ObjectDoesnotExist'},status=status.HTTP_400_BAD_REQUEST)
		if request.data['poly']:
			data = geojson_format(request.data)
		else:
			data = request.data
		serializer = self.serializer_class(polygon,data=data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			return Response(serializer.data,status=status.HTTP_200_OK)
	

class PolygonSearch(APIView):
	model = ProviderPolygon
	serializer_class = PolygonSerializer

	def get(self,request):
		lat = request.GET['latitude']
		lon = request.GET['longitude']

		point = 'POINT('+lat + ' ' +lon +')'
		polygons = ProviderPolygon.objects.filter(poly__contains=point)
		serializer = self.serializer_class(polygons,many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)