

class Column:
    def __init__(self, key, value):
        self.key = key
        self.value = value

from collections import OrderedDict

class MiniCassandra:

    def __init__(self):
        self.row= {}

    # do intialization if necessary

    """
    @param: row_key: a string
    @param: column_key: An integer
    @param: value: a string
    @return: nothing
    """

    def insert(self, row_key, column_key, value):
        if row_key not in self.row:
            self.row[row_key]=OrderedDict()
        self.row[row_key][column_key]=value


    # write your code here

    """
    @param: row_key: a string
    @param: column_start: An integer
    @param: column_end: An integer
    @return: a list of Columns
    """

    def query(self, row_key, column_start, column_end):
        if row_key not in self.row:
            return []
        res=[]
        for k in range(column_start,column_end+1):
            for k in self.row[row_key]:
                res.append(Column(k,self.row[row_key][k]))
        return res
# write your code here