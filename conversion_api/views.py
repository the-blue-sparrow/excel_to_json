from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
import pandas as pd
# Create your views here.


@api_view(["POST"])
def excel(location):
    try:

        conv = json.loads(location.body)
        w = pd.read_excel(conv['numbr'])
        wb = w.columns
        nwb = len(wb)
        n = []
        for i in range(nwb):
            x = {wb[i]: w[wb[i]]}
            n.append(x)
        n = json.dumps(str(n))

        return JsonResponse(n, safe=False)

    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
