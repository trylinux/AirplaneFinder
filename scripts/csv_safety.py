"""Spreadsheet-safe CSV output; lossless machine interchange is explicit."""


def spreadsheet_row(row, *, raw=False):
    if raw:
        return row
    return {
        key: ("'" + value if isinstance(value, str) and value and
              (value[0] in '\t\r\n' or value.lstrip().startswith(('=', '+', '-', '@')))
              else value)
        for key, value in row.items()
    }
