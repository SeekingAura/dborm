import pandas as pd
import ast
from pathlib import Path


def process_numbers(precision=None, scale=None, *args, **kwargs):
    if precision is not None and scale is not None:
        result = [f"Numeric(\n{' '*12}precision={precision},\n{' '*12}scale={scale},\n"]
        if scale == 0:
            result.append(f"{' '*12}asdecimal=False,\n")
        result.append(f"{' '*8})")
        return "".join(result)
    if precision is not None:
        print("WARNING: only precision for process numbers")
    return "BigInteger"


def process_varchar2(max_length=None, *args, **kwargs):
    if max_length is None:
        return "String"

    return f"String({max_length})"


def process_char(max_length=None, *args, **kwargs):
    if max_length is None:
        raise ValueError("Length is expected for CHAR")

    return f"CHAR({max_length})"


def process_largebinary(size=None, *args, **kwargs):
    if size is None:
        return "LargeBinary"
    return f"LargeBinary({size})"


def process_date(*args, **kwargs):
    return "Date"


data_types = {
    "NUMBER": process_numbers,
    "VARCHAR2": process_varchar2,
    "RAW": process_largebinary,
    "DATE": process_date,
    "CHAR": process_char,
}

'''
    {Column Name.lower()} = sqlalchemy.Column(
        "{Column Name}",
        sqlalchemy.{data_types.get(Type)},
        {"nullable=False," if Not Null else ""}
    )
    """
    Columna: {Column Name}
    Tipo en Oracle: {Type}
    """
'''


# Main
if __name__ == "__main__":
    with open("sample.csv", "r", encoding="utf8") as r_file:
        df = pd.read_csv(
            r_file,
            sep="\t",
        )
    df["Comment"] = df["Comment"].fillna("???")
    # df["Comment"] = df["Comment"].replace("nan", "???")
    df.sort_values(by=["#"], ascending=True, inplace=True)
    keys = {key_i: enum for enum, key_i in enumerate(df.columns.values)}

    result_path = Path("result.txt")
    with open("result.txt", "w", encoding="utf8") as out:
        out.truncate()

    for row in zip(*df.to_dict("list").values()):
        print(row[keys.get("Column Name")])
        # print(row[keys.get("Type")])
        split_data_type = dict(enumerate(row[keys.get("Type")].split("(", 1)))
        data_type = split_data_type.get(0)
        data_type_func = data_types.get(data_type)
        if data_type_func is None:
            raise IndexError(f"data_type {row[keys.get('Type')]} is not defined")
        data_type_args_str = f"({split_data_type.get(1, ')')}"
        data_type_args_str = data_type_args_str.replace(")", ",)")
        data_type_args_str = data_type_args_str.replace("(,)", "()")
        data_type_args = ast.literal_eval(data_type_args_str)
        with open("result.txt", "a+", encoding="utf8") as out:
            out.write(f"{' '*4}{row[keys.get('Column Name')].lower()} = sqlalchemy.Column(\n")
            out.write(f"{' '*8}\"{row[keys.get('Column Name')]}\",\n")
            out.write(f"{' '*8}sqlalchemy.{data_type_func(*data_type_args)},\n")
            if row[keys.get("Not Null")] == "false":
                out.write(f"{' '*8}nullable=True,\n")
            out.write(f"{' '*4})\n")
            out.write(f"{' '*4}\"\"\"\n")
            out.write(f"{' '*4}{row[keys.get('Comment')]}\n\n")
            out.write(f"{' '*4}Columna: {row[keys.get('Column Name')]}\n")
            out.write(f"{' '*4}Tipo en Oracle: {row[keys.get('Type')]}\n")
            out.write(f"{' '*4}\"\"\"\n")
