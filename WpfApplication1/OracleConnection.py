import clr
import System
clr.AddReference("System.Data")

from System.Data import DataSet
from System.Data.OleDb import OleDbConnection, OleDbDataAdapter, OleDbCommand

class class1(object):
    #WORK_SKO/WORK_SKO@bvn002b.bbdo.local/PRDBATCH
    conStr = "Provider=MSDAORA.1;User ID=WORK_SKO;Password=WORK_SKO;Persist Security Info=False"

    con = OleDbConnection(conStr)

    query = "SELECT * FROM PERSONAJE"

    adapter = OleDbDataAdapter(query, con)
    ds = DataSet()
    con.Open()

    adapter.Fill(ds, "t1")
    for i in range(ds.Tables["t1"].Rows.Count -1):
        print ds.Tables["t1"].Rows[i][0]
        print ds.Tables["t1"].Rows[i][1]
        print ds.Tables["t1"].Rows[i][2]

    con.Close()





