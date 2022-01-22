from .fact_checker import DbFactChecker
from .utils import Utils


class DbRuleChecker:

    def __init__(self, conn, table_name):
        self.fact_checker = DbFactChecker(conn, table_name)

    @Utils.log
    def run_all(self):
        return {
            'check-row-count': self.check_row_number_rule(),
            'check-primary-key': self.check_primary_key(),
            'check-too-many-pks': self.pk_with_many_cols()
        }

    @Utils.log
    def check_row_number_rule(self):
        row_count = self.fact_checker.number_of_rows()
        if row_count > 10000000:
            return 'Warning! Large table. The number of rows is number-of rows'
        else:
            return 'Passed'

    @Utils.log
    def check_primary_key(self):
        has_pk = self.fact_checker.has_primary_key()
        if not has_pk:
            return 'Warning: the table doesn’t have a PK.'
        else:
            return 'Passed'

    @Utils.log
    def pk_with_many_cols(self):
        pk_cols_count = self.fact_checker.primary_key_count_column()
        if pk_cols_count > 3:
            return f'Warning: High number of columns in the PK. found {pk_cols_count} PK columns (max is 3)'
        else:
            return 'Passed'
