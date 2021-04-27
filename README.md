# WorkItemParser

## Rules for input file:

#### Complexities have to be:
##### VS - Very Simple
##### S - Simple
##### M - Medium
##### C - Complex
##### VC - Very Complex

#### Mandatory columns, order is not important	
#####Requirement ID
#####Domain
#####Process reference
#####Title
#####Prio
#####Description
#####Detailed description
#####Requested by
#####Fit or Gap
#####Proposed Solution
#####Solution Mapping
#####F&O Config
#####F&O Development
#####CE Config
#####CE Development
#####PowerPlatform Config
#####Power Platform Development
#####Integration - Config (Internal)
#####Integration - Inbound ( DEV / EXTERNAL)
#####Integration - Outbound ( DEV / EXTERNAL)

#### if Process reference must starts with the format XXX.YYY.YYY.YYY where X => alphabet and Y=>0-9, Epic name will be XXX.YYY and Feature will be XXX.YYY.YYY
#### else, process reference will be copied as both the epic and feature names

### Output is always in directory C:\Temp, with a prefix 'forUpload -'

