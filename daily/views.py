from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets, filters

from .models import Daily, Evaluation, Contact


class ListDaily(APIView):
    def get(self, request):
        try:
            # daily = Daily.objects.filter(isOpen=True).order_by('-date') #n+1問題
            daily = Daily.objects.select_related(
                "evaluation").filter(isOpen=True).order_by('-date')  # JOINでテーブルを結合して解消

            res_list = [
                {
                    'id': d.id,
                    'date': d.date,
                    'evaluation': d.evaluation.evaluation,
                }
                for d in daily
            ]
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
            res = {
                'id': daily.id,
                'date': daily.date,
                'univ': daily.univ,
                'study': daily.study,
                'other': daily.other,
                'first_meet': daily.first_meet,
                'wanna_do': daily.wanna_do,
                'summary': daily.summary,
            }
            return Response(res)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CategoryDairy(APIView):
    def get(self, request, cat):
        try:
            daily = Daily.objects.filter(isOpen=True).values_list(
                'date', cat).order_by('-date')

            res_list = [
                {
                    'date': d[0],
                    'content': d[1],
                }
                for d in daily
            ]

            return Response(res_list)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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


class Contact(APIView):
    def post(self, reqest):
        body = dict(reqest.data)
        contact = Contact(name=body['name'], email=body['email'],
                          twitter=body['twitter'], content=body['content'])
        contact.save()
        return Response(contact)
