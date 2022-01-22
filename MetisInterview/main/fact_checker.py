import logging

from .utils import Utils


class DbFactChecker:

    def __init__(self, conn, table_name):
        self.conn = conn
        self.table_name = table_name
        self.has_pk = None

    def run_all(self):
        return {
            'number-of-rows': self.number_of_rows(),
            'number-of-indexes': self.number_of_indexes(),
            'has-primary-key': self.has_primary_key(),
            'primary-key-count-columns': self.primary_key_count_column()
        }

    @Utils.log
    def number_of_rows(self):
        return self.conn.execute(f'SELECT count(*) FROM {self.table_name}').fetchone()[0]

    @Utils.log
    def number_of_indexes(self):
        return self.conn.execute(f'''
            SELECT count(*) 
            FROM  sys.indexes AS IND
            WHERE object_id = object_ID('{self.table_name}')
            AND index_id != 0
        ''').fetchone()[0]

    @Utils.log
    def has_primary_key(self):
        res = self.conn.execute(f'''
             SELECT CASE
                WHEN Count(index_id) = 1 THEN 'true'
                    ELSE 'false'
                    END
                FROM sys.indexes 
                WHERE object_id = object_id('{self.table_name}') 
                AND is_primary_key = 1;
        ''').fetchone()[0]
        self.has_pk = True if res == 'true' else False
        return res

    @Utils.log
    def primary_key_count_column(self):
        if self.has_pk == False:
            logger = logging.getLogger('django')
            msg = 'Skipped PK check as this table doesn\'t have pk'
            logger.info(msg)
            return msg
        return self.conn.execute(f'''
            SELECT COUNT(INC.column_id)
            FROM sys.indexes as IND
                    INNER JOIN sys.index_columns as INC
                        ON IND.object_id = INC.object_id
                        AND IND.index_id = INC.index_id
            WHERE IND.object_id = object_id('{self.table_name}') 
                AND IND.is_primary_key = 1;
        ''').fetchone()[0]