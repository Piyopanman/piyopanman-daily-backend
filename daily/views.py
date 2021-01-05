from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets, filters

from .models import Daily

from .common.common import get_all, get_main, category_dict

class ListDaily(APIView):
    def get(self, request):
        try:
            daily = Daily.objects.filter(isOpen=True).order_by('-date') #n+1問題
            daily = Daily.objects.select_related(
                "evaluation").filter(isOpen=True).order_by('-date')  # JOINでテーブルを結合して解消
            # daily = Daily.objects.raw('SELECT daily_daily.id, date, daily_evaluation.evaluation FROM daily_daily INNER JOIN daily_evaluation ON daily_daily.evaluation_id = daily_evaluation.id WHERE isOpen = true;')

            res_list = [get_main(item) for item in daily]
            return Response(res_list)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# class ListDaily(generics.ListCreateAPIView):
#     queryset = Daily.objects.filter(isOpen=True).order_by('-date')
#     serializer_class = DailySerializer


# class DetailDaily(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Daily.objects.all()
#     serializer_class = DailySerializer

class DetailDaily(APIView):
    def get(self, request, pk):
        try:
            try:
                daily = Daily.objects.get(id=pk)
            except:
                error_msg = "そんなidの日報はないよ！"
                return Response(error_msg, status=status.HTTP_404_NOT_FOUND)
            res = get_all(daily)
            return Response(res)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CategoryDairy(APIView):
    def get(self, request, cat):
        try:
            daily = Daily.objects.raw('SELECT id, date, {category} FROM daily_daily WHERE isOpen = true ORDER BY date DESC;'.format(category=cat))
            res = [category_dict[cat](item) for item in daily]
            return Response(res)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
