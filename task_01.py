#!/usr/bin/env python
# -*- coding: utf-8 *-*
"""Print current date."""

import datetime

CURDATE = None


def get_current_date():
    """Current date.

    Args:
        none

    Returns:
        Current date

    Example:
        >>> get_current_date()
        datetime.date(2015, 9, 28)
    """
    return datetime.date.today()

if __name__ == '__main__':
    CURDATE = get_current_date()
    print CURDATE
