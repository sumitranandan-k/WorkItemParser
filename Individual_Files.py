import pandas as pa
import tkinter as tkr
from tkinter import filedialog
import warnings
    
warnings.filterwarnings('ignore')

areaPrefix = 'LDI\\'
filterField = 'Phase'
filterValue = '1. - Go-lIve'

statusList = ['Oorspronkelijk','Nieuw','Geupdate']

#Constants
inputColumnsList = ['Requirement ID','Domain','Process reference','Title','Prio','Description',
                    'Detailed description','Requested by','Fit or Gap','Proposed Solution',
                    'Solution Mapping','F&O Config','F&O Development','CE Config','CE Development',
                    'PowerPlatform Config','Power Platform Development','Integration - Config (Internal)',
                    'Integration - Inbound ( DEV / EXTERNAL)','Integration - Outbound ( DEV / EXTERNAL)','Phase', 'Referentie status']

outputColumnsList = ['Work Item Type','Area Path','Type of Work','Title 1','Title 2', 'Title 3',
                   'Title 4', 'Title 5','Complexity', 'Original Estimate','Remaining Work', 'Effort', 'Domain', 
                   'Description', 'Detailed description', 'Proposed Solution',
                   'Solution Mapping', 'Requested by', 'Fit or Gap', 'Process reference', 'Group ID', 'Phase','Referentie status']

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

areas = {
            '01. Sales':areaPrefix+'Verkoop',
            '02. Order':areaPrefix+'Order en Inkoop',
            '03. Inkoop':areaPrefix+'Order en Inkoop',
            '04. Logistics':areaPrefix+'Logistiek',
            '05. Projects':areaPrefix+'Projecten',
            '06. Service':areaPrefix+'Service',
            '07. Fixed Assets':areaPrefix+'Financien',
            '08. General Ledger':areaPrefix+'Financien',
            '09. Budgeting':areaPrefix+'Financien',
            '10. Accounts Receivable':areaPrefix+'Financien',
            '11. Accounts Payable':areaPrefix+'Financien',
            '12. Invoicing':areaPrefix+'Financien',
            '13. Non-Functional':areaPrefix+'Tech'
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

#commonTaskList = ['Process test', 'QRC - Quick Reference Cards', 'Training', 'Demo / Acceptance test']
    
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

def validateSheet(df, sheetName):
    print('Validating sheet . . . . . '+sheetName)
    df.fillna('', inplace = True)
    listOfColumns = df.columns.values.tolist()

    for columnName in inputColumnsList:
        if (columnName not in listOfColumns):
            raise Exception('Check spaces and new line characters. Missing column: '+columnName)
        
    for rowIndex,row in df.iterrows():        
        for taskTypeTemp in taskTypesDictionary.values():
            if (row[taskTypeTemp] != '' and (row[taskTypeTemp] not in complexities.values())):
                raise Exception('Complexity mismatch. Check Sheet: '+sheetName+',Row: '+str(rowIndex+1)+',Task type: '+taskTypeTemp+'. Invalid complexity: '+row[taskTypeTemp])
                           
        
def processSheet(df, sheetName):
    #Initialize blank row list, this will hold the result set for the sheet before writing into dataframe
    rows_list = []
    
    #feedback - user for troubleshooting      
    print('Processing sheet - '+sheetName)
    
    
    df.sort_values(by=['Process reference', 'Requirement ID'], ignore_index = True, inplace=True)
        
    #Create epic and feature names based on process reference
    for rowIndex,row in df.iterrows(): 
        
        if (statusList.__contains__(row['Referentie status']) == False):
            print('*'+row['Requirement ID']+' skipped due to status - ' + row['Referentie status'])
            continue;
        
        if(row['Process reference'] == ''):
            print('*'+row['Requirement ID']+' skipped due to missing process reference *')
            continue;
        
        if (row['Process reference'].count('.') == 3):            
            splitStrings = row['Process reference'].split('.')
        
            df.at[rowIndex, 'Title 1'] = splitStrings[0] +'.'+ splitStrings[1]
            df.at[rowIndex, 'Title 2'] = df.iloc[rowIndex]['Title 1']  +'.'+ splitStrings[2]
        else:
            df.at[rowIndex, 'Title 1'] = row['Process reference']
            df.at[rowIndex, 'Title 2'] = row['Process reference']
            
        df.at[rowIndex, 'Area Path'] = areas.get(row['Domain'])
       
    
    df['Title 3'] = df['Requirement ID']+'-'+df['Process reference']+'-'+df['Title']
    
    df['Work Item Type'] = 'Feature'
    #add empty columns for taskType and task names
    df['Title 4'] = ''
    df['Title 5'] = ''
    df['Remaining Work'] = ''
    

    #remove the columns as we do not need them anymore
    # del df['Requirement ID']
    # del df['Process reference']
    # del df['Title']

    #replace nulls with empty strings
    df.fillna('', inplace = True)
    
    def constructDict(epic, feature, story, areaPath, taskName, taskType):
        return {
                'Work Item Type'    : taskType,
                'Title 4'           : taskName,
                'Title 5'           : taskName,
                'Original Estimate' : 0,
                'Type of Work'      : 'Misc',
                'Title 1'           : epic,
                'Title 2'           : feature,
                'Title 3'           : story,
                'Area Path'         : areaPath
                }

    #adds task that are common to every feature
    def addCommonTasks(rowsList,  epic, feature, story, areaPath):
        rowsList.append(constructDict(epic, feature, story, areaPath, 'Process test' + ' - ' + story, 'User Story'))
        rowsList.append(constructDict(epic, feature, story, areaPath, 'Process test' + ' - ' + story, 'Task'))

        rowsList.append(constructDict(epic, feature, story, areaPath, 'Demo/Acceptance test' + ' - ' + story, 'User Story'))
        rowsList.append(constructDict(epic, feature, story, areaPath, 'Demo/Acceptance test' + ' - ' + story, 'Task'))
        
        rowsList.append(constructDict(epic, feature, story, areaPath, 'Training' + ' - ' + story, 'User Story'))
        rowsList.append(constructDict(epic, feature, story, areaPath, 'QRC - Quick Reference Cards' + ' - ' + story, 'Task'))
        rowsList.append(constructDict(epic, feature, story, areaPath, 'Training' + ' - ' + story, 'Task'))
        
        # commonTaskList = ['Process test', 'QRC - Quick Reference Cards', 'Training', 'Demo / Acceptance test']
        # for taskName in commonTaskList:
        #     tempDict = {
        #         'Work Item Type'    : 'Task',
        #         'Title 4'           : taskName + ' - ' + story,
        #         'Original Estimate' : 0,
        #         'Type of Work'      : 'Misc',
        #         'Title 1'           : epic,
        #         'Title 2'           : feature,
        #         'Title 3'           : story,
        #         'Area Path'         : areaPath
        #         }    
        #     rowsList.append(tempDict)
            
        return rowsList
            
    #adds task type per complexity and corresponding tasks with estimates
    def addRowsPerTaskType(rowsList, taskType, complexity,  epic, feature, story, areaPath):
        listOfTasks = taskTypesDict().get(taskType)
        
        #add tasktype 
        tempDict = {
            'Work Item Type'    : 'User Story',
            'Title 4'           : taskType + ' - ' + story,
            'Complexity'        : complexity,
            'Title 1'           : epic,
            'Title 2'           : feature,
            'Title 3'           : story  ,
            'Area Path'         : areaPath           
            }    
        rowsList.append(tempDict)
          
        
        for taskName in listOfTasks:
            # print (taskType + '-' + taskName + '-' + complexity)
            tempDict = {
                'Work Item Type'    : 'Task',
                'Title 4'           : taskType  + ' - ' + story,
                'Title 5'           : taskName + ' - ' + taskType + ' - ' + story,
                'Original Estimate' : estimates()[taskType][taskName][complexity], #add estimates
                'Type of Work'      : taskType,
                'Title 1'           : epic,
                'Title 2'           : feature,
                'Title 3'           : story,
                'Complexity'        : complexity,
                'Area Path'         : areaPath
                }    
            tempDict['Remaining work'] = tempDict.get('Original Estimate')
            rowsList.append(tempDict)
        
        return rowsList
    
    #calls addRowsPerTaskType if a complextiy is defined for the proposed solution
    def addTaskTYpes(rowList, rowSeries, epic, feature, story, areaPath):
        
        for taskTypeName in taskTypesDictionary.values():
            requirementComplexity = rowSeries[taskTypeName]
            # print(requirementComplexity)
            if (requirementComplexity != '' and requirementComplexity in complexities.values()):        
                rowList = addRowsPerTaskType(rowsList=rowList, taskType=taskTypeName, complexity=requirementComplexity, epic = epic, feature = feature, story = story, areaPath=areaPath)
        return rowList        
        
    #sets to group user stories under features and features under epics  
    processedEpics = set()
    processedFeatures = set()

    #for each row in requirements add a epic and feature if new, else nest under existing ones
    for rowIndex,row in df.iterrows():
        # print(rowIndex)
        if row['Work Item Type'] == 'Feature':           
            
            title1 = row['Title 1']
            if title1 not in processedEpics:
                tempDict = {
                    'Work Item Type': 'Process',
                    'Title 1': title1,
                    'Area Path': row['Area Path']
                    }
                rows_list.append(tempDict)
                processedEpics.add(title1)        
        
            title2 = row['Title 2']
            if title2 not in processedFeatures:
                tempDict = {
                    'Work Item Type': 'Epic',
                    'Title 2': title2,
                    'Area Path': row['Area Path']
                    }
                rows_list.append(tempDict)
                processedFeatures.add(title2)
            
            #add the requirement as story  
            row['Title 1'] = title1
            row['Title 2'] = title2
                                  
            rows_list.append(row.to_dict())        
            #add level4 and level 5 work items
            rows_list = addTaskTYpes(rows_list, row, title1, title2, row['Title 3'], row['Area Path'])  
            #add tasks common to every story at level 4
            rows_list = addCommonTasks(rows_list, title1, title2, row['Title 3'], row['Area Path'])
            
    #if no valid requirements found then skip furthur processing
    if (rows_list.__len__() == 0):
        return
    #dump the accumuated list to a dataframe            
    df2 = pa.DataFrame(rows_list)    
    #clean up nulls, replace with empty string
    df2['Original Estimate'].fillna(0, inplace=True)
    df2.fillna('', inplace = True)
        
    #remove complexity columns
    for taskTypeColumn in taskTypesDictionary.values():
        del df2[taskTypeColumn]
    
    df2['TaskTypeSumUpColumn'] = df2['Title 4']
    #Sum estimates by feature
    storySumUp = df2.groupby(['Title 3'])['Original Estimate'].sum()
    featureSumUp = df2.groupby(['Title 2'])['Original Estimate'].sum()
    epicSumUp = df2.groupby(['Title 1'])['Original Estimate'].sum()
    taskTypeSumUp = df2.groupby(['TaskTypeSumUpColumn'])['Original Estimate'].sum()
    
    #cleanup 
    df2.loc[df2['Work Item Type'] != 'Process', 'Title 1'] = ''
    df2.loc[df2['Work Item Type'] != 'Epic', 'Title 2'] = ''
    df2.loc[df2['Work Item Type'] != 'Feature', 'Title 3'] = ''    
    df2.loc[df2['Work Item Type'] != 'User Story', 'Title 4'] = ''  
    df2.loc[df2['Work Item Type'] != 'Task', 'Title 5'] = ''  
   
    for rowIndex,row in df2.iterrows():
        effort = 0
        if (row['Work Item Type'] == 'Process' and epicSumUp[row['Title 1']]):
            effort = epicSumUp[row['Title 1']]
        if (row['Work Item Type'] == 'Epic' and featureSumUp[row['Title 2']] != 0):
            effort = featureSumUp[row['Title 2']]
        if (row['Work Item Type'] == 'Feature' and storySumUp[row['Title 3']] != 0):
            effort = storySumUp[row['Title 3']]
        if (row['Work Item Type'] == 'User Story' and taskTypeSumUp[row['TaskTypeSumUpColumn']] != 0):
            effort = taskTypeSumUp[row['TaskTypeSumUpColumn']]
        if (row['Work Item Type'] == 'Task' and row['Title 5'] != ''):
            df2.at[rowIndex, 'Title 4'] = ''                        
            
        df2.at[rowIndex, 'Effort'] = effort
        
    #copy dataframe to a new new dataframe with columns arranged in proper order
    df3 = df2[outputColumnsList]        
    
    #print for UI feedback
    print ('creating output file:'+ 'C:\\temp\\forUpload - '+sheetName+'.csv')
    #create csv from dataframe, skip index column
    # print('Number of work items added to sheet:', df3.shape[0])
    df3.to_csv(r'C:\temp\forUpload - '+sheetName+'.csv', index=False)

#driver code

print('***********************************************************************************************************')        
print()
print('This program can only process .xlsx files with the following format:')
print()
print()
print('Column names(Order of columns does not matter):')
x = ','.join(inputColumnsList)
print(x)
print()
print()
print('Types of complexities:')
x = ','.join(complexities.values())
print(x)
print()
print()
print('!Please make sure there are no CR,LF or excess spaces in the column names and complexities before you press enter')
print()
print('************************************************************************************************************')        
print()
input('Press Enter to launch file picker...')
           
#read all sheets in excel
all_dfs = pa.read_excel (browseFiles(), sheet_name=None)
print('************************************************************************************************************')     
print('Finding sheets to process......')
toBeProcessed = {}  #All sheets with requirements
framesToBeProcessed = {} #All sheets with estimated requirements

for key in all_dfs.keys():    
    # Skip consolidated sheet
    if (key == 'AllData'):
        continue
    df = all_dfs.get(key)      
    # Reset column indexes
    df = df.T.reset_index(drop=True).T      
    colsList = list(df.columns.values)
    for rowIndex,row in df.iterrows():
        #print('Searching for header row in '+key)
        if (df.iloc[rowIndex][0] == 'Requirement ID'):            
            #print('Header found at row ', rowIndex)
            toBeProcessed.__setitem__(key, rowIndex)
            break

for key in toBeProcessed.keys():
    # print(key)
    df = all_dfs.get(key).iloc[toBeProcessed.get(key): , :]
    df.fillna('', inplace = True)
    
    # / is not allowed in field name in Dev ops
    df = df.replace('Fit/Gap', 'Fit or Gap')
    new_header = df.iloc[0] 
    
    if len(new_header) != 0:
        formattedHeaders = []
        for sub in new_header:
            # Replace any new line characters in column headers with spaces
            formattedHeaders.append(sub.replace('\n', ' '))
        
        
        # formattedHeaders = formattedHeaders.replace('Fit/Gap', 'Fit or Gap')
        
        df.columns = formattedHeaders
        df = df.reset_index(drop=True)
        
        df = df.iloc[1: , :] #Added columns, so remove first row
        
        # Correct typographical mistakes
        df = df.replace('S-Simple', 'S - Simple')
        df = df.replace('M-Medium', 'M - Medium')
        df = df.replace('C-Complex', 'C - Complex')
        df = df.replace('N.A.', '')
        # df = df.replace('Fit/Gap', '')        
        
        if (filterField in df.columns):
            df = df.loc[df[filterField] == filterValue]
            df = df[df['Referentie status'].isin(statusList)]

        if df.shape[0] > 1:            
            framesToBeProcessed.__setitem__(key, df)   
        else:
            print('Skipping sheet - '+key+'. No '+ 'requirements with '+filterField+" value-"+filterValue)
    
#check for data entry errors

for key in framesToBeProcessed.keys():
    validateSheet(framesToBeProcessed.get(key), key)
    
print('Validation complete')   
print('************************************************************************************************************')      
#process each sheet in excel to generate a seperate csv file
if (framesToBeProcessed.keys().__len__() == 0):
    print("No requirements found with "+filterField+" value-"+filterValue)
    
else:
    print('Sheets with requirements with '+filterField+" value-"+filterValue)
    print(framesToBeProcessed.keys())
    print('************************************************************************************************************')      
    print('Preparing sheets for processing....')
          
    for key in framesToBeProcessed.keys():
        if (key in framesToBeProcessed):
            processSheet(framesToBeProcessed.get(key), key)
        
print('Processing complete')   
print('************************************************************************************************************')      
