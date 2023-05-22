from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TrashReportSerializer
from .models import TrashReport
from rest_framework.parsers import MultiPartParser, FormParser

class TrashReportListCreateAPIView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        reports = TrashReport.objects.all()
        serializer = TrashReportSerializer(reports, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TrashReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TrashReportRetrieveUpdateDestroyAPIView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get_object(self, pk):
        try:
            return TrashReport.objects.get(pk=pk)
        except TrashReport.DoesNotExist:
            return None

    def get(self, request, pk):
        report = self.get_object(pk)
        if report is None:
            return Response({'error': 'Trash report not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TrashReportSerializer(report)
        return Response(serializer.data)

    def put(self, request, pk):
        report = self.get_object(pk)
        if report is None:
            return Response({'error': 'Trash report not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TrashReportSerializer(report, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        report = self.get_object(pk)
        if report is None:
            return Response({'error': 'Trash report not found'}, status=status.HTTP_404_NOT_FOUND)
        report.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

