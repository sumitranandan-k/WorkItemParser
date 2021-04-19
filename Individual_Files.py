# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 11:36:06 2021

@author: sumit.kamarajugadda
"""


# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 19:11:07 2021

@author: Sumit
"""

import pandas as pa

    
complexities = ['VS - Very Simple', 'S - Simple', 'M - Medium', 'C - Complex', 'VC - Very Complex']

estimates = {'F&O Config':{'Configuration':{'VS - Very Simple':0,'S - Simple':0, 'M - Medium':0,'C - Complex':0, 'VC - Very Complex':0}},
            'F&O Development':{
                                'Functional Design':{'VS - Very Simple':2.8,'S - Simple':6.3, 'M - Medium':9.8,'C - Complex':22.4, 'VC - Very Complex':42},
                                'Technical Design':{'VS - Very Simple':1.6,'S - Simple':3.6, 'M - Medium':5.6,'C - Complex':12.8, 'VC - Very Complex':24},
                                'Build & Unit Test':{'VS - Very Simple':4,'S - Simple':9, 'M - Medium':14,'C - Complex':32, 'VC - Very Complex':60},
                                'Functional Test':{'VS - Very Simple':2.8,'S - Simple':6.3, 'M - Medium':9.8,'C - Complex':22.4, 'VC - Very Complex':42},
                                'Manage & perform fixes':{'VS - Very Simple':0.44,'S - Simple':0.99, 'M - Medium':1.54,'C - Complex':3.52, 'VC - Very Complex':6.6},
                                'Release to VT environment':{'VS - Very Simple':0,'S - Simple':0, 'M - Medium':0,'C - Complex':0, 'VC - Very Complex':0}
                                },
            'CE Config':{'Configuration':{'VS - Very Simple':0,'S - Simple':0, 'M - Medium':0,'C - Complex':0, 'VC - Very Complex':0}},            
            'PowerPlatform Config':{'Configuration':{'VS - Very Simple':0,'S - Simple':0, 'M - Medium':0,'C - Complex':0, 'VC - Very Complex':0}},
            'CE Development':{
                                'Functional Design':{'VS - Very Simple':2.8,'S - Simple':6.3, 'M - Medium':9.8,'C - Complex':22.4, 'VC - Very Complex':42},
                                'Technical Design':{'VS - Very Simple':1.6,'S - Simple':3.6, 'M - Medium':5.6,'C - Complex':12.8, 'VC - Very Complex':24},
                                'Build & Unit Test':{'VS - Very Simple':4,'S - Simple':9, 'M - Medium':14,'C - Complex':32, 'VC - Very Complex':60},
                                'Functional Test':{'VS - Very Simple':2.8,'S - Simple':6.3, 'M - Medium':9.8,'C - Complex':22.4, 'VC - Very Complex':42},
                                'Manage & perform fixes':{'VS - Very Simple':0.44,'S - Simple':0.99, 'M - Medium':1.54,'C - Complex':3.52, 'VC - Very Complex':6.6},
                                'Release to VT environment':{'VS - Very Simple':0,'S - Simple':0, 'M - Medium':0,'C - Complex':0, 'VC - Very Complex':0}
                                },
            'Power Platform Development':{
                                'Functional Design':{'VS - Very Simple':2.8,'S - Simple':6.3, 'M - Medium':9.8,'C - Complex':22.4, 'VC - Very Complex':42},
                                'Technical Design':{'VS - Very Simple':1.6,'S - Simple':3.6, 'M - Medium':5.6,'C - Complex':12.8, 'VC - Very Complex':24},
                                'Build & Unit Test':{'VS - Very Simple':4,'S - Simple':9, 'M - Medium':14,'C - Complex':32, 'VC - Very Complex':60},
                                'Functional Test':{'VS - Very Simple':2.8,'S - Simple':6.3, 'M - Medium':9.8,'C - Complex':22.4, 'VC - Very Complex':42},
                                'Manage & perform fixes':{'VS - Very Simple':0.44,'S - Simple':0.99, 'M - Medium':1.54,'C - Complex':3.52, 'VC - Very Complex':6.6},
                                'Release to VT environment':{'VS - Very Simple':0,'S - Simple':0, 'M - Medium':0,'C - Complex':0, 'VC - Very Complex':0}
                                },
            'Integration - Config (Internal)':{'Configuration':{'VS - Very Simple':0,'S - Simple':0, 'M - Medium':0,'C - Complex':0, 'VC - Very Complex':0}},            
            'Integration - Inbound ( DEV / EXTERNAL)':{
                                'Functional Design':{'VS - Very Simple':4.8,'S - Simple':7.2, 'M - Medium':12,'C - Complex':24, 'VC - Very Complex':36},
                                'Technical Design':{'VS - Very Simple':9.6,'S - Simple':14.4, 'M - Medium':24,'C - Complex':48, 'VC - Very Complex':72},
                                'Build & Unit Test':{'VS - Very Simple':16,'S - Simple':24, 'M - Medium':40,'C - Complex':80, 'VC - Very Complex':120},
                                'Functional Test':{'VS - Very Simple':14.4,'S - Simple':21.6, 'M - Medium':36,'C - Complex':72, 'VC - Very Complex':108},
                                'Manage & perform fixes':{'VS - Very Simple':3.04,'S - Simple':4.56, 'M - Medium':7.6,'C - Complex':15.2, 'VC - Very Complex':22.8},
                                'Release to VT environment':{'VS - Very Simple':0,'S - Simple':0, 'M - Medium':0,'C - Complex':0, 'VC - Very Complex':0}
                                },
            'Integration - Outbound ( DEV / EXTERNAL)':{
                                'Functional Design':{'VS - Very Simple':2.4,'S - Simple':4.8, 'M - Medium':7.2,'C - Complex':12, 'VC - Very Complex':18},
                                'Technical Design':{'VS - Very Simple':4.8,'S - Simple':9.6, 'M - Medium':14.4,'C - Complex':24, 'VC - Very Complex':36},
                                'Build & Unit Test':{'VS - Very Simple':8,'S - Simple':16, 'M - Medium':24,'C - Complex':40, 'VC - Very Complex':60},
                                'Functional Test':{'VS - Very Simple':7.2,'S - Simple':14.4, 'M - Medium':21.6,'C - Complex':36, 'VC - Very Complex':54},
                                'Manage & perform fixes':{'VS - Very Simple':1.52,'S - Simple':3.04, 'M - Medium':4.56,'C - Complex':7.6, 'VC - Very Complex':11.4},
                                'Release to VT environment':{'VS - Very Simple':0,'S - Simple':0, 'M - Medium':0,'C - Complex':0, 'VC - Very Complex':0}
                                },   
            }

taskTypesList = ['F&O Config',
                 'F&O Development',
                 'CE Config',
                 'CE Development',
                 'PowerPlatform Config',
                 'Power Platform Development',
                 'Integration - Config (Internal)',
                 'Integration - Inbound ( DEV / EXTERNAL)',
                 'Integration - Outbound ( DEV / EXTERNAL)']


dictTaskTypes = {'F&O Config':['Configuration'],
                 'F&O Development':['Functional Design', 'Technical Design', 'Build & Unit Test', 'Functional Test', 'Manage & perform fixes', 'Release to VT environment'],
                 'CE Config':['Configuration'],
                 'CE Development':['Build & Unit Test', 'Functional Design', 'Technical Design', 'Functional Test', 'Manage & perform fixes', 'Release to VT environment'],
                 'PowerPlatform Config':['Configuration'],
                 'Power Platform Development':['Functional Design', 'Technical Design', 'Build & Unit Test', 'Functional Test', 'Manage & perform fixes', 'Release to VT environment'],
                 'Integration - Config (Internal)':['Configuration'],
                 'Integration - Inbound ( DEV / EXTERNAL)':['Functional Design', 'Technical Design', 'Build & Unit Test', 'Functional Test', 'Manage & perform fixes', 'Release to VT environment'],
                 'Integration - Outbound ( DEV / EXTERNAL)':['Functional Design', 'Technical Design', 'Build & Unit Test', 'Functional Test', 'Manage & perform fixes', 'Release to VT environment']
                 }

commonTaskList = ['Process test', 'QRC - Quick Reference Cards', 'Training', 'Demo / Acceptance test', 'Key user training']
    
def processSheet(df, sheetName):
    rows_list = []
    # df = pa.read_excel (r'c:\temp\Copy of CP DevOps Requriements upload.xlsx', sheet_name=sheetName)
      
    print(sheetName)
    
    df['Title 1'] = df['Process reference'].str.slice(0,7)
    df['Title 2'] = df['Process reference'].str.slice(0,11)
    df['Title 3'] = df['Requirement ID']+'-'+df['Process reference']+'-'+df['Title']
    df['Work Item Type'] = 'User Story'
    df['Title 4'] = ''
    df['Title 5'] = ''
       
    del df['Requirement ID']
    del df['Process reference']
    del df['Title']

    df.fillna('', inplace = True)

    
    def addCommonTasks(rowsList):
        for taskName in commonTaskList:
            tempDict = {
                'Work Item Type': 'Task',
                'Title 4': taskName,
                'Original Estimate' : 0,
                'Type of Work': 'Misc'
                }    
            rowsList.append(tempDict)
            
        return rowsList
            
    
    def addRowsPerTaskType(rowsList, taskType, complexity):
            
        
        listOfTasks = dictTaskTypes.get(taskType)
        
        tempDict = {
            'Work Item Type': 'TaskType',
            'Title 4': taskType,
            'Complexity': complexity        
            }    
        rowsList.append(tempDict)
          
        
        for taskName in listOfTasks:
            print (taskType + '-' + taskName + '-' + complexity)
            tempDict = {
                'Work Item Type': 'Task',
                'Title 5': taskName,
                'Original Estimate' : estimates[taskType][taskName][complexity],
                'Type of Work': taskType
                }    
            rowsList.append(tempDict)
        
        return rowsList
    
    def addTaskTYpes(rowList, rowSeries):
        
        for taskTypeName in taskTypesList:
            requirementComplexity = rowSeries[taskTypeName]
            print(requirementComplexity)
            if (requirementComplexity != '' and requirementComplexity in complexities):        
                rowList = addRowsPerTaskType(rowsList=rowList, taskType=taskTypeName, complexity=requirementComplexity)
        return rowList        
        
    processedEpics = set()
    processedFeatures = set()
    
    df2 = pa.DataFrame(data=None, columns=df.columns)
    
    # print (df)
   
    for rowIndex,row in df.iterrows():
        print(rowIndex)
        if row['Work Item Type'] == 'User Story':           
            
            title1 = row['Title 1']
            if title1 not in processedEpics:
                tempDict = {
                    'Work Item Type': 'Epic',
                    'Title 1': title1
                    }
                rows_list.append(tempDict)
                processedEpics.add(title1)        
        
            title2 = row['Title 2']
            if title2 not in processedFeatures:
                tempDict = {
                    'Work Item Type': 'Feature',
                    'Title 2': title2
                    }
                rows_list.append(tempDict)
                processedFeatures.add(title2)
            
            row['Title 1'] = ''
            row['Title 2'] = ''
            rows_list.append(row.to_dict())        
            rows_list = addTaskTYpes(rows_list, row)  
            rows_list = addCommonTasks(rows_list)
            
            
    df2 = pa.DataFrame(rows_list)    
    df2.fillna('', inplace = True)
        
    for taskTypeColumn in taskTypesList:
        del df2[taskTypeColumn]
    
    #TODO1: can we loop all sheets in excel? -done
    #TODO2: can we Sum up original estimate? 
    #TODO3: can we split the dataframe into max rows less than 999 but at epic level?
    
    df3 = df2[['Work Item Type','Type of Work','Title 1','Title 2', 'Title 3',
               'Title 4', 'Title 5','Complexity', 'Original Estimate', 'Domain', 'Prio',
               'Description', 'Detailed description', 'Proposed Solution',
               'Solution Mapping', 'Requested by', 'Fit/Gap']]
        
    # df2.to_csv(r'C:\temp\result.csv', index=False)
    print ('creating output file:'+ 'C:\temp\forUpload-'+sheetName+'.csv')
    df3.to_csv(r'C:\temp\forUpload-'+sheetName+'.csv', index=False)


# Read excel sheet
#skiprows = 7,header = 2
all_dfs = pa.read_excel (r'c:\temp\CP DevOps upload -test1.xlsx', sheet_name=None)

for key in all_dfs.keys():
    processSheet(all_dfs.get(key), key)