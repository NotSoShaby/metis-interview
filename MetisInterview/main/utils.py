import logging
import time
from functools import wraps

from django.conf import settings
import copy


class Utils:
    """
    A class with only staticmethods to be used as utils (the only reason its a class is for convieniency)
    """

    @staticmethod
    def get_basic_response_data():
        return copy.deepcopy(settings.BASIC_RESPONSE_DATA_STRUCTURE)

    @staticmethod
    def log(func):
        """ functions that will be wrapped in this decorator will log their execution status and time"""
        func_name = func.__qualname__

        @wraps(func)
        def wrapper(*args, **kwargs):
            logger = logging.getLogger('django')
            logger.info(f'Executing `{func_name}`')
            start_time = time.time()
            res = func(*args, **kwargs)
            exec_time = time.time() - start_time
            logger.info(f'Finished `{func_name}` - Execution time was: {exec_time} seconds')
            return res

        return wrapper
