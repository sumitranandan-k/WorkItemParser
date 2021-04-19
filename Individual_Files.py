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
import tkinter as tkr
from tkinter import filedialog


    


taskTypesDictionary = {
                 'ax_config'    :'F&O Config',
                 'ax_dev'       :'F&O Development',
                 'ce_config'    :'CE Config',
                 'ce_dev'       :'CE Development',
                 'pp_config'    :'PowerPlatform Config',
                 'pp_dev'       :'Power Platform Development',
                 'int_config'   :'Integration - Config (Internal)',
                 'int_inbound'  :'Integration - Inbound ( DEV / EXTERNAL)',
                 'int_outbound' :'Integration - Outbound ( DEV / EXTERNAL)'
                }

tasksDict = {
             'Config'   :'Configuration',
             'FDD'      :'Functional Design',
             'TDD'      :'Technical Design',
             'Dev'      : 'Build & Unit Test',
             'FTest'    : 'Functional Test',
             'Rework'   : 'Manage & perform fixes',
             'Release'  : 'Release to VT environment'
            }

configTasksList = [tasksDict.get('Config')]
devTasksList    = [tasksDict.get('FDD'),tasksDict.get('TDD'),tasksDict.get('Dev'),tasksDict.get('FTest'),tasksDict.get('Rework'),tasksDict.get('Release')]

# tasksByType = { 'ConfigOnly': []
                # }
commonTaskList = ['Process test', 'QRC - Quick Reference Cards', 'Training', 'Demo / Acceptance test', 'Key user training']
    
complexities = {
                'VS'    :'VS - Very Simple',
                'S'     :'S - Simple',
                'M'     :'M - Medium',
                'C'     :'C - Complex',
                'VC'    :'VC - Very Complex'
                }

def taskTypesDict():
    tempDict =  {
                 taskTypesDictionary.get('ax_config')     :configTasksList,
                 taskTypesDictionary.get('ax_dev')        :devTasksList,
                 taskTypesDictionary.get('ce_config')     :configTasksList,
                 taskTypesDictionary.get('ce_dev')        :devTasksList,
                 taskTypesDictionary.get('pp_config')     :configTasksList,
                 taskTypesDictionary.get('pp_dev')        :devTasksList,
                 taskTypesDictionary.get('int_config')    :configTasksList,
                 taskTypesDictionary.get('int_inbound')   :devTasksList,
                 taskTypesDictionary.get('int_outbound')  :devTasksList
                 }
    return tempDict

#percentage of dev estimate for a given task
def parameters():
    tempDict =  {
            'customization':{
                    tasksDict['FDD']:70,
                    tasksDict['TDD']:40,                        
                    tasksDict['FTest']:70,
                    tasksDict['Rework']:11,
                    tasksDict['Release']:0
                    },
            'inbound':{
                    tasksDict['FDD']:30,
                    tasksDict['TDD']:60,                        
                    tasksDict['FTest']:90,
                    tasksDict['Rework']:19,
                    tasksDict['Release']:0
                    },                     
            'outbound':{
                    tasksDict['FDD']:30,
                    tasksDict['TDD']:60,                        
                    tasksDict['FTest']:90,
                    tasksDict['Rework']:19,
                    tasksDict['Release']:0
                    }
            }
    return tempDict;

def config_dev():
    tempDict = {
                complexities.get('VS')  :0,
                complexities.get('S')   :0,
                complexities.get('M')   :0,
                complexities.get('C')   :0,
                complexities.get('VC')  :0,
                }    
    return tempDict

def customization_dev():
    tempDict = {
                complexities.get('VS')  :4,
                complexities.get('S')   :9,
                complexities.get('M')   :14,
                complexities.get('C')   :32,
                complexities.get('VC')  :60,
                }    
    return tempDict

def inbound_dev():
    tempDict = {
                complexities.get('VS')  :16,
                complexities.get('S')   :24,
                complexities.get('M')   :40,
                complexities.get('C')   :80,
                complexities.get('VC')  :120,
                }    
    return tempDict

def outbound_dev():
    tempDict = {
                complexities.get('VS')  :8,
                complexities.get('S')   :16,
                complexities.get('M')   :24,
                complexities.get('C')   :40,
                complexities.get('VC')  :60,
                }    
    return tempDict

def estimateParameters():
    tempDict = {
            'configuration' : config_dev(),
            'customization' :customization_dev(),
            'inbound'       :inbound_dev(),                     
            'outbound'      :outbound_dev()
            }
    return tempDict

    
def calcDevEstimates(percent, devEstimates):
    tempDict = {
                complexities.get('VS')  :(devEstimates.get(complexities.get('VS'))*percent)/100,
                complexities.get('S')   :(devEstimates.get(complexities.get('S'))*percent)/100,
                complexities.get('M')   :(devEstimates.get(complexities.get('M'))*percent)/100,
                complexities.get('C')   :(devEstimates.get(complexities.get('C'))*percent)/100,
                complexities.get('VC')  :(devEstimates.get(complexities.get('VC'))*percent)/100
               }
    return tempDict

def getEstimateByTaskType(parameter, devEstimates):
    tempDict = {
                tasksDict['Dev']:devEstimates,
                tasksDict['FDD']:calcDevEstimates(parameter.get(tasksDict['FDD']), devEstimates),
                tasksDict['TDD']:calcDevEstimates(parameter.get(tasksDict['TDD']), devEstimates),
                tasksDict['FTest']:calcDevEstimates(parameter.get(tasksDict['FTest']), devEstimates),
                tasksDict['Rework']:calcDevEstimates(parameter.get(tasksDict['Rework']), devEstimates),
                tasksDict['Release']:calcDevEstimates(parameter.get(tasksDict['Release']), devEstimates)
            }
    return tempDict

def estimates():
    tempDict =  {
                    taskTypesDictionary.get('ax_config')      :{tasksDict.get('Config'):estimateParameters()['configuration']},
                    taskTypesDictionary.get('int_config')     :{tasksDict.get('Config'):estimateParameters()['configuration']},
                    taskTypesDictionary.get('ce_config')      :{tasksDict.get('Config'):estimateParameters()['configuration']},           
                    taskTypesDictionary.get('pp_config')      :{tasksDict.get('Config'):estimateParameters()['configuration']},            
                    taskTypesDictionary.get('ax_dev')         :getEstimateByTaskType(parameter = parameters().get('customization'), devEstimates = estimateParameters()['customization']),                                                                            
                    taskTypesDictionary.get('ce_dev')         :getEstimateByTaskType(parameter = parameters().get('customization'), devEstimates =  estimateParameters()['customization']),                                                                    
                    taskTypesDictionary.get('pp_dev')         :getEstimateByTaskType(parameter = parameters().get('customization'), devEstimates = estimateParameters()['customization']),                                             
                    taskTypesDictionary.get('int_inbound')    :getEstimateByTaskType(parameter = parameters().get('inbound'), devEstimates = estimateParameters()['inbound']),                                             
                    taskTypesDictionary.get('int_outbound')   :getEstimateByTaskType(parameter = parameters().get('outbound'), devEstimates = estimateParameters()['outbound'])                            
                }
    return tempDict

def browseFiles():
    filetypes = (
        ('Excel files', '*.xlsx'),
        ('All files', '*.*')
    )   
    
    # Create the root window
    window = tkr.Tk()
      
    # Set window title
    window.title('File Explorer')
      
    # Set window size
    window.geometry("500x500")
      
    #Set window background color
    window.config(background = "white")
      
    # # Create a File Explorer label
    # label_file_explorer = Label(window,
    #                             text = "Choose the requirements file",
    #                             width = 100, height = 4,
    #                             fg = "blue")
      
 
    # button_explore = Button(window,
    #                         text = "Browse Files",
    #                         command = browseFiles)
                             
    selectedFile = filedialog.askopenfilename(initialdir = r'c:\temp', filetypes = filetypes, title = 'Select a file')
    window.withdraw()
    
    return selectedFile

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
            
        
        listOfTasks = taskTypesDict().get(taskType)
        
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
                'Original Estimate' : estimates()[taskType][taskName][complexity],
                'Type of Work': taskType
                }    
            rowsList.append(tempDict)
        
        return rowsList
    
    def addTaskTYpes(rowList, rowSeries):
        
        for taskTypeName in taskTypesDictionary.values():
            requirementComplexity = rowSeries[taskTypeName]
            print(requirementComplexity)
            if (requirementComplexity != '' and requirementComplexity in complexities.values()):        
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
        
    for taskTypeColumn in taskTypesDictionary.values():
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
                    
                     
# all_dfs = pa.read_excel (r'c:\temp\CP DevOps upload -test1.xlsx', sheet_name=None)
all_dfs = pa.read_excel (browseFiles(), sheet_name=None)

for key in all_dfs.keys():
    processSheet(all_dfs.get(key), key)