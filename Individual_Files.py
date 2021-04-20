import pandas as pa
import tkinter as tkr
from tkinter import filedialog

#Constants
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

commonTaskList = ['Process test', 'QRC - Quick Reference Cards', 'Training', 'Demo / Acceptance test', 'Key user training']
    
complexities = {
                'VS'    :'VS - Very Simple',
                'S'     :'S - Simple',
                'M'     :'M - Medium',
                'C'     :'C - Complex',
                'VC'    :'VC - Very Complex'
               }

#Combinations derived from constants
configTasksList = [tasksDict.get('Config')]
devTasksList    = [tasksDict.get('FDD'),tasksDict.get('TDD'),tasksDict.get('Dev'),tasksDict.get('FTest'),tasksDict.get('Rework'),tasksDict.get('Release')]

#creates a dictionary of tasks types per proposed solution
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

#percentage of dev estimate to calculate estimates of other types of work
#read it as for inbound integrations TDD is 60% of dev estimate
def parameters():
    tempDict =  {
            'customization':{
                    tasksDict['FDD']    :70,
                    tasksDict['TDD']    :40,                        
                    tasksDict['FTest']  :70,
                    tasksDict['Rework'] :11,
                    tasksDict['Release']:0
                    },
            'inbound':{
                    tasksDict['FDD']    :30,
                    tasksDict['TDD']    :60,                        
                    tasksDict['FTest']  :90,
                    tasksDict['Rework'] :19,
                    tasksDict['Release']:0
                    },                     
            'outbound':{
                    tasksDict['FDD']    :30,
                    tasksDict['TDD']    :60,                        
                    tasksDict['FTest']  :90,
                    tasksDict['Rework'] :19,
                    tasksDict['Release']:0
                    }
            }
    return tempDict;

#estimates for configuration
def config_dev():
    tempDict = {
                complexities.get('VS')  :0,
                complexities.get('S')   :0,
                complexities.get('M')   :0,
                complexities.get('C')   :0,
                complexities.get('VC')  :0,
                }    
    return tempDict

#estimates for customization
def customization_dev():
    tempDict = {
                complexities.get('VS')  :4,
                complexities.get('S')   :9,
                complexities.get('M')   :14,
                complexities.get('C')   :32,
                complexities.get('VC')  :60,
                }    
    return tempDict

#estimates for inbound integration
def inbound_dev():
    tempDict = {
                complexities.get('VS')  :16,
                complexities.get('S')   :24,
                complexities.get('M')   :40,
                complexities.get('C')   :80,
                complexities.get('VC')  :120,
                }    
    return tempDict

#estimates for outbound integration
def outbound_dev():
    tempDict = {
                complexities.get('VS')  :8,
                complexities.get('S')   :16,
                complexities.get('M')   :24,
                complexities.get('C')   :40,
                complexities.get('VC')  :60,
               }    
    return tempDict

#wraps the estimates in a dictionary with values of each type of work <key>:<value> = <type of work>:<dictionary of default estimated for the type of work>
def estimateParameters():
    tempDict = {
                'configuration' : config_dev(),
                'customization' : customization_dev(),
                'inbound'       : inbound_dev(),                     
                'outbound'      : outbound_dev()
               }
    return tempDict

#calclate related work and wrap it in a dictionary based on complexity    
def calcDevEstimates(percent, devEstimates):
    tempDict = {
                complexities.get('VS')  :(devEstimates.get(complexities.get('VS'))*percent)/100,
                complexities.get('S')   :(devEstimates.get(complexities.get('S'))*percent)/100,
                complexities.get('M')   :(devEstimates.get(complexities.get('M'))*percent)/100,
                complexities.get('C')   :(devEstimates.get(complexities.get('C'))*percent)/100,
                complexities.get('VC')  :(devEstimates.get(complexities.get('VC'))*percent)/100
               }
    return tempDict

#wraps calculated estimates by task type
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

#wraps estimates per task type by technology used
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

#opens file picker dialog to choose the file to process
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
    
    #open the dialog and capture selection
    selectedFile = filedialog.askopenfilename(initialdir = r'C:\temp', filetypes = filetypes, title = 'Select a file')
    #close file picker
    window.withdraw()
    
    return selectedFile

def processSheet(df, sheetName):
    #Initialize blank row list, this will hold the result set for the sheet before writing into dataframe
    rows_list = []
    
    #feedback - user for troubleshooting      
    print(sheetName)
    
    
    df.sort_values(by=['Process reference', 'Requirement ID'], ignore_index = True, inplace=True)
        
    #Create epic and feature names based on process reference
    df['Title 1'] = df['Process reference'].str.slice(0,7)
    df['Title 2'] = df['Process reference'].str.slice(0,11)
    df['Title 3'] = df['Requirement ID']+'-'+df['Process reference']+'-'+df['Title']
    df['Work Item Type'] = 'User Story'
    #add empty columns for taskType and task names
    df['Title 4'] = ''
    df['Title 5'] = ''
    

    #remove the columns as we do not need them anymore
    del df['Requirement ID']
    del df['Process reference']
    del df['Title']

    #replace nulls with empty strings
    df.fillna('', inplace = True)

    #adds task that are common to every feature
    def addCommonTasks(rowsList,  epic, feature, story):
        for taskName in commonTaskList:
            tempDict = {
                'Work Item Type'    : 'Task',
                'Title 4'           : taskName,
                'Original Estimate' : 0,
                'Type of Work'      : 'Misc',
                'Title 1'           : epic,
                'Title 2'           : feature,
                'Title 3'           : story
                }    
            rowsList.append(tempDict)
            
        return rowsList
            
    #adds task type per complexity and corresponding tasks with estimates
    def addRowsPerTaskType(rowsList, taskType, complexity,  epic, feature, story):
        listOfTasks = taskTypesDict().get(taskType)
        
        #add tasktype 
        tempDict = {
            'Work Item Type'    : 'TaskType',
            'Title 4'           : taskType,
            'Complexity'        : complexity,
            'Title 1'           : epic,
            'Title 2'           : feature,
            'Title 3'           : story             
            }    
        rowsList.append(tempDict)
          
        
        for taskName in listOfTasks:
            print (taskType + '-' + taskName + '-' + complexity)
            tempDict = {
                'Work Item Type'    : 'Task',
                'Title 4'           : taskType,
                'Title 5'           : taskName,
                'Original Estimate' : estimates()[taskType][taskName][complexity], #add estimates
                'Type of Work'      : taskType,
                'Title 1'           : epic,
                'Title 2'           : feature,
                'Title 3'           : story
                }    
            rowsList.append(tempDict)
        
        return rowsList
    
    #calls addRowsPerTaskType if a complextiy is defined for the proposed solution
    def addTaskTYpes(rowList, rowSeries, epic, feature, story):
        
        for taskTypeName in taskTypesDictionary.values():
            requirementComplexity = rowSeries[taskTypeName]
            print(requirementComplexity)
            if (requirementComplexity != '' and requirementComplexity in complexities.values()):        
                rowList = addRowsPerTaskType(rowsList=rowList, taskType=taskTypeName, complexity=requirementComplexity, epic = epic, feature = feature, story = story)
        return rowList        
        
    #sets to group user stories under features and features under epics  
    processedEpics = set()
    processedFeatures = set()

    #for each row in requirements add a epic and feature if new, else nest under existing ones
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
            
            #add the requirement as story  
            row['Title 1'] = title1
            row['Title 2'] = title2
                      
            rows_list.append(row.to_dict())        
            #add level4 and level 5 work items
            rows_list = addTaskTYpes(rows_list, row, title1, title2, row['Title 3'])  
            #add tasks common to every story at level 4
            rows_list = addCommonTasks(rows_list, title1, title2, row['Title 3'])
            
    #dump the accumuated list to a dataframe            
    df2 = pa.DataFrame(rows_list)    
    #clean up nulls, replace with empty string
    df2['Original Estimate'].fillna(0, inplace=True)
    df2.fillna('', inplace = True)
        
    #remove complexity columns
    for taskTypeColumn in taskTypesDictionary.values():
        del df2[taskTypeColumn]
    
    df2['TaskTypeSumUpColumn'] = df2['Title 3'] + df2['Title 4']
    #Sum estimates by feature
    storySumUp = df2.groupby(['Title 3'])['Original Estimate'].sum()
    featureSumUp = df2.groupby(['Title 2'])['Original Estimate'].sum()
    epicSumUp = df2.groupby(['Title 1'])['Original Estimate'].sum()
    taskTypeSumUp = df2.groupby(['TaskTypeSumUpColumn'])['Original Estimate'].sum()
    
    #cleanup 
    df2.loc[df2['Work Item Type'] != 'Epic', 'Title 1'] = ''
    df2.loc[df2['Work Item Type'] != 'Feature', 'Title 2'] = ''
    df2.loc[df2['Work Item Type'] != 'User Story', 'Title 3'] = ''
    df2.loc[df2['Work Item Type'] != 'TaskType', 'Title 4'] = ''
   
    for rowIndex,row in df2.iterrows():
        effort = 0
        if (row['Work Item Type'] == 'Epic' and epicSumUp[row['Title 1']]):
            effort = epicSumUp[row['Title 1']]
        if (row['Work Item Type'] == 'Feature' and featureSumUp[row['Title 2']] != 0):
            effort = featureSumUp[row['Title 2']]
        if (row['Work Item Type'] == 'User Story' and storySumUp[row['Title 3']] != 0):
            effort = storySumUp[row['Title 3']]
        if (row['Work Item Type'] == 'TaskType' and taskTypeSumUp[row['TaskTypeSumUpColumn']] != 0):
            effort = taskTypeSumUp[row['TaskTypeSumUpColumn']]
            
        df2.at[rowIndex, 'Effort'] = effort
        
    #copy dataframe to a new new dataframe with columns arranged in proper order
    df3 = df2[['Work Item Type','Type of Work','Title 1','Title 2', 'Title 3',
               'Title 4', 'Title 5','Complexity', 'Original Estimate', 'Effort', 'Domain', 'Prio',
               'Description', 'Detailed description', 'Proposed Solution',
               'Solution Mapping', 'Requested by', 'Fit/Gap']]        
    
    #print for UI feedback
    print ('creating output file:'+ 'D:\temp\forUpload-'+sheetName+'.csv')
    #create csv from dataframe, skip index column
    df3.to_csv(r'C:\temp\forUpload - '+sheetName+'.csv', index=False)
                    
#driver code
#read all sheets in excel
all_dfs = pa.read_excel (browseFiles(), sheet_name=None)

#process each sheet in excel to generate a seperate csv file
for key in all_dfs.keys():
    processSheet(all_dfs.get(key), key)