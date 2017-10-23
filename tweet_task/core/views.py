from rest_framework import views
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from helper import paginated_results
from constants import match_query, date_range_query, numeric_range_query, imp_query, senti_query

class SearchView(views.APIView):
    """
    Provides Full text search
    """
    permission_classes = [AllowAny,]

    def get(self, request):
        try:
            term = request.GET['q']
            page_no = int(request.GET['page'])
            query = match_query(term)
            res = paginated_results(query, page_no)
            if len(res)==0:
                return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"data":[], "message": "Filter not found"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"data": res, "message":"Success"},status=status.HTTP_200_OK)


class RangeSearchView(views.APIView):
    """
    Provides Range query for Date fields as well as Numeric fields
    """
    permission_classes = [AllowAny,]

    def get(self, request):
        try:
            field = request.GET['field']
            page_no = int(request.GET['page'])
            range_start = request.GET['range_start']
            range_end = request.GET['range_end']
            is_date = int(request.GET['is_date'])
            if is_date:
                query = date_range_query(field, range_start, range_end)
            else:
                query = numeric_range_query(field, range_start, range_end)
            res = paginated_results(query, page_no)
            if len(res)==0:
                return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"data":[], "message": "Filter not found"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"data": res, "message":"Success"},status=status.HTTP_200_OK)


class ImpSearchView(views.APIView):
    """
    Provides Exact match and fuzzy query
    """
    permission_classes = [AllowAny, ]

    def get(self, request):
        try:
            field = request.GET['field']
            page_no = int(request.GET['page'])
            query_type = request.GET['qt']
            field_value = request.GET['fv']
            query = imp_query(query_type, field, field_value)
            res = paginated_results(query, page_no)
            if len(res)==0:
                return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"data":[], "message": "Filter not found"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"data": res, "message":"Success"},status=status.HTTP_200_OK)


class SentimentSearchView(views.APIView):
    """
    Provides tweets corresponding to particular sentiment
    """
    permission_classes = [AllowAny, ]

    def get(self, request):
        try:
            sentiment = request.GET['s']
            page_no = int(request.GET['page'])
            query=senti_query(sentiment)
            res = paginated_results(query, page_no)
            if len(res)==0:
                return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"data":[], "message": "Filter not found"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"data": res, "message":"Success"},status=status.HTTP_200_OK)

