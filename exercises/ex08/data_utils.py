"""Dictionary related utility functions."""

__author__ = "730314205"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str,str]]:
    """Read the rows of a csv into a 'table.'"""
    result: list[dict[str,str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str,str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """"Transforms a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head1(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first n rows of data for each column."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = table[0]
    for column in first_row:
        values: list[str] = []
        for item in column:
            values.append(item)
            result[column] = values
    return result


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first n rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in table:
        values: list[str] = []
        i: int = 0
        if n >= len(table):
            return table
        while i < n:
            values.append(table[column][i])
            i = i + 1
        result[column] = values
    return result


def select(data_table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a new column based table with only a specific subset of original columns."""
    result: dict[str, list[str]] = {}
    for column in names:
        result[column] = data_table[column]
    return result


def concat(table1: dict[str, list[int]], table2: dict[str, list[int]]) -> dict[str, list[int]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[int]] = {}
    column: str = ""
    for column in table1:
        result[column] = table1[column]
    for column in table2:
        if table2[column] in result:
            result[column] = result + table2[column]
        else:
            result[column] = table2[column]
    return result


def count(list1: list[str]) -> dict[str, int]:
    """Given a list[str], produce a dict[str, int] where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    result: dict[str, int] = {}
    for i in list1:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result