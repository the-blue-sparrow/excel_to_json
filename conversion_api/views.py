from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
import pandas as pd
from rest_framework.parsers import MultiPartParser, FileUploadParser
# Create your views here.


@api_view(["POST"])
@parser_classes([FileUploadParser])
def excel(location):
    try:
        conv = location.data['file']
        # conv =
        #w = pd.read_excel(conv['numbr'])
        w = pd.read_excel(conv)
        wb = w.columns
        n = {}
        y = {}

        for i in range(len(w[wb[1]])):
            for j in wb:
                y[j] = str(w[j][i])
            n[i] = y
        n = json.dumps(n, skipkeys=True, ensure_ascii=False, indent=4)

        return JsonResponse(n, safe=False)

    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
