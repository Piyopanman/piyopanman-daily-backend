from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets, filters

from .models import Daily
from .serializers import DailySerializer


class ListDaily(APIView):
    def get(self, request):
        try:
            post = Daily.objects.filter(isOpen=True).order_by('-date')
            r = [
                {
                    'id': i.id,
                    'date': i.date,
                    'univ': i.univ,
                    'study': i.study,
                    'other': i.other,
                    'first_meet': i.first_meet,
                    'wanna_do': i.wanna_do,
                    'evaluation': i.evaluation.evaluation,
                }
                for i in post
            ]
            return Response(r)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# class ListDaily(generics.ListCreateAPIView):
#     queryset = Daily.objects.filter(isOpen=True).order_by('-date')
#     serializer_class = DailySerializer


class DetailDaily(generics.RetrieveUpdateDestroyAPIView):
    queryset = Daily.objects.all()
    serializer_class = DailySerializer


class CategoryDairy(APIView):
    def get(self, request, cat):

        post = Daily.objects.values_list('date', cat).order_by('-date')

        res_list = [
            {
                'date': d[0],
                'cat': cat,
                'content': d[1]
            }
            for d in post
        ]
        print(post)
        print(res_list)

        return Response(res_list)

        # q = 'select id, date, {} from daily_daily'.format(cat)
        # post = Daily.objects.raw(q)
        # print(list(post))

        # res_list = [
        #     {
        #         'date': i.date,
        #         'content': i.cat,
        #         # catを探しちゃう univを探してくれない
        #         # 'Daily' object has no attribute 'cat'
        #     }
        #     for i in post
        # ]

        # print(res_list)

        # return Response(res_list)
