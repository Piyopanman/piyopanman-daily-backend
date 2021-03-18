from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets, filters

from .models import Daily, Evaluation, Contact

from .common.calc import calc_eva


class ListDaily(APIView):
    def get(self, request):
        try:
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

class ContactView(APIView):
    def post(self, request):
        body = dict(request.data)
        contact = Contact(name=body['name'], email=body['email'],
                          twitter=body['twitter'], oshi=body['oshi'], content=body['content'])
        contact.save()
        return Response(body)


class EvalRatio(APIView):
    def get(self, request):
        try:
            try:
                dailies = Daily.objects.select_related(
                    "evaluation").filter(isOpen=True)
                eva_list = {"perfect": 0, "good": 0, "soso": 0, "bad": 0}
                for d in dailies:
                    eva = d.evaluation.evaluation
                    if eva == "perfect":
                        eva_list["perfect"] += 1
                    elif eva == "good":
                        eva_list["good"] += 1
                    elif eva == "soso":
                        eva_list["soso"] += 1
                    else:
                        eva_list["bad"] += 1
                calc_eva(eva_list)
            except:
                error_msg = "no id error"
                return Response(error_msg, status=status.HTTP_404_NOT_FOUND)

            return Response(eva_list)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
