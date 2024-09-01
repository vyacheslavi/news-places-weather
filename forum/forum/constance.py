from django.db.utils import OperationalError
from constance import config as constance_config

import logging

...


def get_constance_setting(setting):
    """
    A dirty workaround to enable Constance do the inital migration and not
    fail because the table that is about to be created doesn't exist yet.

    @setting (str) setting to retrieve

    @returns given setting value
    """
    try:
        return getattr(constance_config, setting)
    except OperationalError as exc:
        if str(exc).startswith("no such table: constance_constance") or str(
            exc
        ).startswith("no such table: constance_constance"):
            logging.exception("This workaround allows to setting initial migration")
        else:
            # print(str(exc))
            raise exc
