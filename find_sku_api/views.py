from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from config import tidb_conn
import pandas as pd
import json


def find_same_sku(request):
    input_data = json.loads(request.body)
    input_skuId = input_data['skuId']
    token = input_data['token']

    cursor, conn = tidb_conn()
    sql = f"select * from voila_similarity_table where query_id='{input_skuId}' or result_id='{input_skuId}'"
    df = pd.read_sql(sql, conn)
    cursor.close()
    conn.close()

    if (token != "bd1d9a173032db5ce554794d52208081") or (not isinstance(token, str)) or (not isinstance(input_skuId, str)):
        return JsonResponse(
            {
                "status": {
                    "code": "0",
                    "description": "成功"
                },
                "data": {
                }
            }
        )

    try:
        query_id = df.loc[0, 'query_id']
        result_id = df.loc[0, 'result_id']
        weighted_score = df.loc[0, 'weighted_score']
        title_score = df.loc[0, 'title_score']
        query_url = df.loc[0, 'query_url']
        result_url = df.loc[0, 'result_url']
        stdCateName = df.loc[0, 'stdCateName']
        stdSubCateName = df.loc[0, 'stdSubCateName']
        stdSubCate2Name = df.loc[0, 'stdSubCate2Name']

        if (result_id == input_skuId) and (query_id == input_skuId):
            return JsonResponse(
                {
                    "status": {
                        "code": "0",
                        "description": "成功"
                    },
                    "data": {
                    }
                }
            )
        elif (result_id == input_skuId) and (query_id != input_skuId):
            query_id, result_id = result_id, query_id
            query_url, result_url = result_url, query_url
            return JsonResponse(
                {
                    "status": {
                        "code": "0",
                        "description": "成功"
                    },
                    "data": {
                        "query_id": query_id,
                        "result_id": result_id,
                        "weighted_score": weighted_score,
                        "title_score": title_score,
                        "query_url": query_url,
                        "result_url": result_url,
                        "stdCateName": stdCateName,
                        "stdSubCateName": stdSubCateName,
                        "stdSubCate2Name": stdSubCate2Name
                    }
                }
            )
        elif (result_id != input_skuId) and (query_id == input_skuId):
            return JsonResponse(
                {
                    "status": {
                        "code": "0",
                        "description": "成功"
                    },
                    "data": {
                        "query_id": query_id,
                        "result_id": result_id,
                        "weighted_score": weighted_score,
                        "title_score": title_score,
                        "query_url": query_url,
                        "result_url": result_url,
                        "stdCateName": stdCateName,
                        "stdSubCateName": stdSubCateName,
                        "stdSubCate2Name": stdSubCate2Name
                    }
                }
            )
        else:
            return JsonResponse(
                {
                    "status": {
                        "code": "0",
                        "description": "成功"
                    },
                    "data": {
                    }
                }
            )
    except Exception as e:
        print(e)
        return JsonResponse(
            {
                "status": {
                    "code": "0",
                    "description": "成功"
                },
                "data": {
                }
            }
        )


# if __name__ == '__main__':
#     find_same_sku()