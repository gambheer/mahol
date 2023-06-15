class CommonHelper(object):

    @staticmethod
    def from_db_datetime_to_datetime(_datetime, _format, to_str=False):
        __datetime = _datetime.strftime(_format)
        if to_str:
            return str(__datetime)
        return __datetime

