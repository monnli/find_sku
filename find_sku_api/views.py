from django.shortcuts import render

# Create your views here.

from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.http import JsonResponse
import json


def find_same_sku(request):
    input_data = json.loads(request.body)
    input_skuId = input_data['skuId']

    return JsonResponse(
        {
            "status": {
                "code": "0",
                "description": "成功"
            },
            "data": {
                "query_id": input_skuId,
                "result_id": "0a64bb916b3a1d7070518a01c638273c",
                "weighted_score": 0.9,
                "title_score": 1.0,
                "query_url": "https://www.asos.com/us/ellesse/ellesse-ion-overhead-jacket-with-reflective-logo-in-black/prd/8631428",
                "result_url": "https://www.asos.com/us/ellesse/ellesse-ion-overhead-jacket-with-reflective-logo-in-black/prd/8631428",
                "stdCateName": "Apparel",
                "stdSubCateName": "Clothing",
                "stdSubCate2Name": "Coats & Jackets"
            }
        }
    )


def find_similary_sku(request):
    return JsonResponse(
        {
            "status": {
                "code": "0",
                "description": "成功"
            },
            "data": {
                "skuId": "0a64bb916b3a1d7070518a01c638273c",
                "spuId": "1b6e4e9d549a8cbfb030eb6ef57f0b53",
                "canonicalUrl": "https://www.asos.com/us/ellesse/ellesse-ion-overhead-jacket-with-reflective-logo-in-black/prd/8631428",
                "title": "ellesse Ion overhead jacket with reflective logo in black",
                "score": 0.9
            }
        }
    )
