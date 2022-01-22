import logging

from django.db import connections, ProgrammingError
from rest_framework.response import Response
from rest_framework.views import APIView

from .rule_checker import DbRuleChecker
from .utils import Utils
from .fact_checker import DbFactChecker

logger = logging.getLogger(__name__)


class BaseView(APIView):

    @staticmethod
    def _insure_table_exists(db_conn, table_name):
        data = Utils.get_basic_response_data()
        try:
            db_conn.execute(f"select 1 from {table_name}")
            data['Info'].append(f'Table with the name {table_name} found')
            return Response(data=data, status=200)
        except ProgrammingError as e:
            if 'Invalid object name' in str(e):
                data['Errors'].append({
                    f'Table {table_name} not found': str(e)
                })
                return Response(data=data, status=400)
            else:
                data['Errors'].append({
                    f'Server Error': str(e)
                })
                return Response(data=data, status=500)


class FactView(BaseView):

    def get(self, request):
        table_name = request.GET.get('tableName')
        conn = connections['remote_metis'].cursor()
        response = self._insure_table_exists(conn, table_name)
        if not response.status_code == 200:
            return response
        else:
            checker = DbFactChecker(conn, table_name)
            response.data[table_name] = checker.run_all()
            return response


class RuleView(BaseView):
    def get(self, request):
        table_name = request.GET.get('tableName')
        conn = connections['remote_metis'].cursor()
        response = self._insure_table_exists(conn, table_name)
        if not response.status_code == 200:
            return response
        else:
            checker = DbRuleChecker(conn, table_name)
            response.data[table_name] = checker.run_all()
            return response