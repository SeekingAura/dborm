import datetime
from enum import Enum
from decimal import Decimal


class ColTypeEnum(Enum):
    BIG_INTEGER = int
    """
    large-range integer, -9223372036854775808 to +9223372036854775807,
    common data types:
    * PostgreSql: bigint
    * MySql: BIGINT
    * SQL Server: BIGINT
    * Oracle: NUMBER(38, 0)
    """
    INTEGER = int
    """
    typical choice for integer, -2147483648 to +2147483647,
    common data types:
    * PostgreSql: integer
    * MySql: INT
    * SQL Server: INT
    * Oracle: NUMBER(10, 0)
    """
    SMALL_INTEGER = int
    """
    small-range integer, -32768 to +32767,
    common data types:
    * PostgreSql: smallint
    * MySql: SMALLINT
    * SQL Server: SMALLINT
    * Oracle: NUMBER(5, 0)
    """

    CHAR = str
    """
    Fixed-length string, usually more faster when all of values have the same
    length of characters with defined n length, if string have less than n
    chars will filled with whitespace chars
    common data types:
    * PostgreSql: char(n)
    * MySql: CHAR(n)
    * SQL Server: CHAR(n)
    * Oracle: CHAR(n)
    """
    VARCHAR = str
    """
    Variable-length string, space-efficient for varying lengths of data with
    defined max n length, common data types:
    * PostgreSql: varchar(n)
    * MySql: VARCHAR(n)
    * SQL Server: VARCHAR(n)
    * Oracle: VARCHAR(n)
    """
    TEXT = str
    """
    string without defined limit, suitable for storing long text entries such
    as articles, descriptions, or logs common data types:
    * PostgreSql: TEXT
    * MySql: TEXT
    * SQL Server: TEXT
    * Oracle: CLOB
    """

    REAL = float
    """
    Number with few decimals (usually 6 digits) with variable-precision,
    inexact, common data types:
    * PostgreSql: real
    * MySql: FLOAT
    * SQL Server: REAL
    * Oracle: BINARY_FLOAT
    """
    DOUBLE: float
    """
    Number with decimals more decimals than REAL type (usually 15 digits) with
    variable-precision, inexact, common data types:
    * PostgreSql: double precision
    * MySql: DOUBLE
    * SQL Server: FLOAT
    * Oracle: BINARY_DOUBLE
    """
    NUMERIC = float
    """
    Number with decimals specified by user more exact, common data types:
    * PostgreSql: numeric
    * MySql: NUMERIC
    * SQL Server: NUMERIC
    * Oracle: NUMBER
    """
    DECIMAL = Decimal
    """
    Number with number of digits and decimals specified by user more exact, common data types:
    * PostgreSql: decimal(num_digits, num_decimals)
    * MySql: DECIMAL(num_digits, num_decimals)
    * SQL Server: DECIMAL(num_digits, num_decimals)
    * Oracle: NUMBER(num_digits, num_decimals)
    """
    DATE = datetime.date
    """
    Date without time, common data types:
    * PostgreSql: DATE
    * MySql: DATE
    * SQL Server: DATE
    * Oracle: DATE
    """
    TIMESTAMP: datetime.datetime
    """
    Timestamp that allow to get Date with time, some cases could have tz,
    common data types:
    * PostgreSql: TIMESTAMP
    * MySql: TIMESTAMP
    * SQL Server: TIMESTAMP
    * Oracle: TIMESTAMP
    """

    UNKNOWN: None
    """
    Undefined case
    """


class ColType:
    pass
