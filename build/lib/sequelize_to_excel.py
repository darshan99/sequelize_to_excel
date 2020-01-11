# -*- coding: utf-8 -*-
#
# Copyright 2019
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# 

import  re
import json;
import pandas as pd;
import logging
from pandas.io.json import json_normalize

""" This module will help you extract info from your standard 
sequelize file to excel format , consisiting column name , field name ,
auto increment etc"""
def main():
    """ 
        This function accepts filename , removes noise and 
        maps field to columns of excel

        Args:
            filename : command line input for file name
        
        Returns :
            Saves excel at the same location
    """
    try:
        # request for filename
        filename = input("pls enter the filename w/o extn :-> ")
        # Reads the file
        f = open(filename+".js","r")

        txt = f.read()

        # uses regex to clear noise
        x = re.sub("^\/*.*\n","",txt)
        x2 = re.sub("^module.*\n..*',","[",x.strip())
        x3 = x2.replace(");","")
        x3 = x3.replace("};","]")
        x3 = re.sub(r'DataTypes.',r'',x3)
        x3 = re.sub("'",r'',x3)
        x3 = re.sub(r'(\w+)',r'"\1"',x3)
        x3 = x3.replace(" ","")

        jsonObj = json.loads(x3)

        listRows = []
        # defines excel header and maps value
        lstColumnHeader = ["name","type","allowNull","primaryKey","autoIncrement","field","defaultValue","references","tableName","version"]
        for (k,v) in jsonObj[0].items():
            listColumns = []
            listColumns.append(k)
            listColumns.append(v.get("type","na"))
            listColumns.append(v.get("allowNull","na"))
            listColumns.append(v.get("primaryKey","na"))
            listColumns.append(v.get("autoIncrement","na"))
            listColumns.append(v.get("field","na"))
            listColumns.append(v.get("defaultValue","na"))
            listColumns.append(v.get("references","na"))
            listColumns.append(jsonObj[1].get("tableName","na"))
            listColumns.append(jsonObj[1].get("version","na"))
            listRows.append(listColumns)

        df = pd.DataFrame(listRows,columns=lstColumnHeader)
        df.to_excel(filename+".xlsx")
    except FileNotFoundError as fe:
        logging.error(" File name passed is not present at the location ",stack_info=True)
    except ValueError as ve:
        logging.error(" attributes in the model are unknown ",stack_info=True)
    except Exception as e:
        logging.error(e)

if __name__ == "__main__":
    main()
    pass