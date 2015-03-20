
import os

def parseLoggingConf():
    """
    To see this docstring:
    print parseLoggingConf.__doc__
    
    This function parses a logging.conf file used in support of python logging.
    USER WARNING: THIS IS VERY FRAGILE CODE!!!!
    This function expects the logging.conf file to be in a specific format so 
    that the arg for the RotatingFileHandler can be discovered easily.  In 
    finding this, the arg is parsed to give the path defined within the 
    logging.conf file to place the resultant log files.  
    
    The unfortunate reason for needing this parser is due to a circular 
    dependency resulting from needing the directory path to be created before
    it has been created when executing: 
    logging.config.fileConfig('logging.conf')
    
    To break this circular dependency, it is necessary to separately read and
    parse the logging.conf file by the main program prior to executing the
    logging.config.fileConfig('logging.conf') line.  By doing so, the necessary
    path structure can be put in place prior to needing it.
    
    Sorry about this - currently don't know of a better way around this issue.
    
    """
    f=open('logging.conf')
    #f.read()
    cntr=0
    for line in f:
        if "os.path.expanduser('~')" in line:
            #case we found the line we're looking for - now extract path info
            linePath=line
            cntr+=1
    #note that with this version of logging.conf, we expect to find two lines - second one is the one we want
    if cntr != 2:
        print "found incorrect number of entries - ambiguous result warning"
        
    #print linePath
    parse0=linePath.split()
    parse1=parse0[2].strip(',",')+')'
    
    getPath=eval(parse1)
    
    f.close()
    return(getPath)
    
def checkLogDirs(baseFilename):
    #extract directory name for logging
    logDir=os.path.dirname(baseFilename)
    #realize that logging is supporting multiple applications each using their own subdirectory
    tmp=os.path.split(logDir)
    #split the directory into the base directory name
    logBaseDir=tmp[0]
    #and into the log directory corresponding to this application
    logLogDir=tmp[1]
    #extract the filename from the logging.conf file too
    logFile=os.path.basename(baseFilename)    
    
    #Having the directory info, we can check if these directories exist or not.
    #check if the main .Logging directory exists - if not, create it
    createDirs=False
    if not os.path.exists(logBaseDir):
        os.mkdir(logBaseDir)
    #now check if the logging subdirectory for this applicaton exists, if not, create it
    if not os.path.exists(logDir):
        os.mkdir(logDir)  
        createDirs=True
        
    return(createDirs)