#!/usr/bin/python

#AppStyleSheet.py

#This program illustrates how to make changes to the application presentation
#utilizing PyQt StyleSheet.  It handles three cases:
# default - no changes made
# global - sets parameters for all widgets to use
# custom - enables setting each widget class independently

# Note that here the global selection can detect the operating system and 
# provide the means to change the global font size for each OS.  This reduces
# the need for having to tweak widget sizes to accommodate fonts as they seem
# to render different sizes on different platforms.

#For more examples, see here: 
# http://doc.qt.digia.com/4.6/stylesheet-examples.html
# http://qt.developpez.com/doc/4.2/stylesheet/

#import utility modules
import sys, os

#import PyQt modules
from PyQt4 import QtGui, QtCore, Qt

#include this try/except block to remap QString needed when using IPython
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

#import GUI components generated from Qt Designer .ui file
from ui_AppTemplate import *

class AppTemplateMain(QtGui.QMainWindow):
    
    #initialize app
    def __init__(self, parent=None):
        #setup main window
        QtGui.QMainWindow.__init__(self, parent)

        self.ui = Ui_MainWindow() #defined in ui_AppTemplate.py
        self.ui.setupUi(self)
        self.setWindowTitle("App Template Main")
    
        #add action exit for File --> Exit menu option
        self.connect(self.ui.actionExit, QtCore.SIGNAL('triggered()'), self.confirmExit)
        #add signal/slot connection for pushbutton exit request
        self.connect(self.ui.pushButtonExit, QtCore.SIGNAL('clicked()'), self.confirmExit)
        
        lst=['Default','Global','Custom']
        sel,ok = QtGui.QInputDialog.getItem(self,"Available Workspaces","Select from the list:",lst)
        
        
        if sel==lst[0] or ok==False:
            #case to use default style that comes without doing anything
            pass
        elif sel==lst[1]:
            #case to use global style sheet
            style="""
                border: 1px solid black;
                border-radius: 1px;
                background-color: rgb(200,200,200);
                font-weight: Bold;
                font-style: italic; /* normal italic or oblique */
            """
            
            #set global font style by system type as point size seem to be different on different platforms - mitigates the need for resizing widgets to fit fonts on different platforms
            if os.sys.platform == 'win32':
                #set for windows
                style=style+"""font-size: 12pt; font-family: "Comic Sans MS"; font-weight: Normal;"""
            elif os.sys.platform == 'linux2':
                #set for Linux
                style=style+"""font-size: 11pt; font-family: Ariel;"""
            elif os.sys.platform == 'darwin':
                #mac
                style=style+"""font-size: 12pt; font-family: Ariel;"""
            else:
                #otherwise...
                style=style+"""font-size: 11pt; font-family: Ariel;"""
            #example how to do global using one line:
            #self.setStyleSheet('font-size: 16pt ; font-family: Ariel;')
            
            self.setStyleSheet(style)
            
        elif sel==lst[2]:
        #case to use custom stylesheet
            self.setStyleSheet("""
                .QWidget{ /* the . (dot) in front of QWidget specifies only QWidget is affected but not sub-classes of QWidget.  Remove the dot to also affect the sub-classes. */
                /*Found in this example that removing the . caused parts of QMessageBox to show colors from QWidget, thus kept it as .QWidget. */
                background-color: cyan; 
                }
                QMenuBar{
                background-color: blue; 
                color: coral;
                font-weight: Bold;
                font-family: Courier;
                font-size: 12pt; 
                border: 1px solid black;
                border-radius: 1px;
                spacing: 3px; /* spacing between menu bar items */
                }
                QMenu{
                background-color: #ff9999; 
                color: white;
                font-size: 11pt; 
                margin: 3px;  /*puts space between border and outside edge */
                border: 2px inset solid black; /*gives menu item a border */
                border-radius: 10px; /*curves corners */
                padding: 0 60px;  /*shape size of menu item */
                }
                QMenu::item {
                    /* sets background of menu item. set this to something non-transparent
                        if you want menu color and menu item color to be different */
                background-color: red;
                }
                QMenu::item:selected { /* when user selects item using mouse or keyboard */
                background-color: #654321;
                }
                QStatusBar{
                background-color: #6495ED; 
                color: violet;
                }            
                QPushButton{
                background-color: #7FFF00; 
                color: #9932CC;
                font-weight: Bold;
                font-size: 14pt; 
                border: 1px solid black;
                border-radius: 1px;
                }
                QPushButton::pressed{ 
                background-color: gold 
                }
                QMessageBox{
                background-color: green; 
                color: green;
                font-weight: Normal;
                font-size: 12pt; 
                }
            """)
        else:
            #undefined case
            pass
                
        
        """
        As a reference, including some options for use above:
        font-family:
            #font.serif          : Bitstream Vera Serif, New Century Schoolbook, Century Schoolbook L, Utopia, ITC Bookman, Bookman, Nimbus Roman No9 L, Times New Roman, Times, Palatino, Charter, serif
            #font.sans-serif     : Bitstream Vera Sans, Lucida Grande, Verdana, Geneva, Lucid, Arial, Helvetica, Avant Garde, sans-serif
            #font.cursive        : Apple Chancery, Textile, Zapf Chancery, Sand, cursive
            #font.fantasy        : Comic Sans MS, Chicago, Charcoal, Impact, Western, fantasy
            #font.monospace      : Bitstream Vera Sans Mono, Andale Mono, Nimbus Mono L, Courier New, Courier, Fixed, Terminal, monospace
        
        font-weight options:
            Light
            Normal
            DemiBold
            Bold
            Black
        
        font colors:
        cnames = {
            'aliceblue':            '#F0F8FF',
            'antiquewhite':         '#FAEBD7',
            'aqua':                 '#00FFFF',
            'aquamarine':           '#7FFFD4',
            'azure':                '#F0FFFF',
            'beige':                '#F5F5DC',
            'bisque':               '#FFE4C4',
            'black':                '#000000',
            'blanchedalmond':       '#FFEBCD',
            'blue':                 '#0000FF',
            'blueviolet':           '#8A2BE2',
            'brown':                '#A52A2A',
            'burlywood':            '#DEB887',
            'cadetblue':            '#5F9EA0',
            'chartreuse':           '#7FFF00',
            'chocolate':            '#D2691E',
            'coral':                '#FF7F50',
            'cornflowerblue':       '#6495ED',
            'cornsilk':             '#FFF8DC',
            'crimson':              '#DC143C',
            'cyan':                 '#00FFFF',
            'darkblue':             '#00008B',
            'darkcyan':             '#008B8B',
            'darkgoldenrod':        '#B8860B',
            'darkgray':             '#A9A9A9',
            'darkgreen':            '#006400',
            'darkkhaki':            '#BDB76B',
            'darkmagenta':          '#8B008B',
            'darkolivegreen':       '#556B2F',
            'darkorange':           '#FF8C00',
            'darkorchid':           '#9932CC',
            'darkred':              '#8B0000',
            'darksage':             '#598556',
            'darksalmon':           '#E9967A',
            'darkseagreen':         '#8FBC8F',
            'darkslateblue':        '#483D8B',
            'darkslategray':        '#2F4F4F',
            'darkturquoise':        '#00CED1',
            'darkviolet':           '#9400D3',
            'deeppink':             '#FF1493',
            'deepskyblue':          '#00BFFF',
            'dimgray':              '#696969',
            'dodgerblue':           '#1E90FF',
            'firebrick':            '#B22222',
            'floralwhite':          '#FFFAF0',
            'forestgreen':          '#228B22',
            'fuchsia':              '#FF00FF',
            'gainsboro':            '#DCDCDC',
            'ghostwhite':           '#F8F8FF',
            'gold':                 '#FFD700',
            'goldenrod':            '#DAA520',
            'gray':                 '#808080',
            'green':                '#008000',
            'greenyellow':          '#ADFF2F',
            'honeydew':             '#F0FFF0',
            'hotpink':              '#FF69B4',
            'indianred':            '#CD5C5C',
            'indigo':               '#4B0082',
            'ivory':                '#FFFFF0',
            'khaki':                '#F0E68C',
            'lavender':             '#E6E6FA',
            'lavenderblush':        '#FFF0F5',
            'lawngreen':            '#7CFC00',
            'lemonchiffon':         '#FFFACD',
            'lightblue':            '#ADD8E6',
            'lightcoral':           '#F08080',
            'lightcyan':            '#E0FFFF',
            'lightgoldenrodyellow': '#FAFAD2',
            'lightgreen':           '#90EE90',
            'lightgray':            '#D3D3D3',
            'lightpink':            '#FFB6C1',
            'lightsage':            '#BCECAC',
            'lightsalmon':          '#FFA07A',
            'lightseagreen':        '#20B2AA',
            'lightskyblue':         '#87CEFA',
            'lightslategray':       '#778899',
            'lightsteelblue':       '#B0C4DE',
            'lightyellow':          '#FFFFE0',
            'lime':                 '#00FF00',
            'limegreen':            '#32CD32',
            'linen':                '#FAF0E6',
            'magenta':              '#FF00FF',
            'maroon':               '#800000',
            'mediumaquamarine':     '#66CDAA',
            'mediumblue':           '#0000CD',
            'mediumorchid':         '#BA55D3',
            'mediumpurple':         '#9370DB',
            'mediumseagreen':       '#3CB371',
            'mediumslateblue':      '#7B68EE',
            'mediumspringgreen':    '#00FA9A',
            'mediumturquoise':      '#48D1CC',
            'mediumvioletred':      '#C71585',
            'midnightblue':         '#191970',
            'mintcream':            '#F5FFFA',
            'mistyrose':            '#FFE4E1',
            'moccasin':             '#FFE4B5',
            'navajowhite':          '#FFDEAD',
            'navy':                 '#000080',
            'oldlace':              '#FDF5E6',
            'olive':                '#808000',
            'olivedrab':            '#6B8E23',
            'orange':               '#FFA500',
            'orangered':            '#FF4500',
            'orchid':               '#DA70D6',
            'palegoldenrod':        '#EEE8AA',
            'palegreen':            '#98FB98',
            'paleturquoise':        '#AFEEEE',
            'palevioletred':        '#DB7093',
            'papayawhip':           '#FFEFD5',
            'peachpuff':            '#FFDAB9',
            'peru':                 '#CD853F',
            'pink':                 '#FFC0CB',
            'plum':                 '#DDA0DD',
            'powderblue':           '#B0E0E6',
            'purple':               '#800080',
            'red':                  '#FF0000',
            'rosybrown':            '#BC8F8F',
            'royalblue':            '#4169E1',
            'saddlebrown':          '#8B4513',
            'salmon':               '#FA8072',
            'sage':                 '#87AE73',
            'sandybrown':           '#FAA460',
            'seagreen':             '#2E8B57',
            'seashell':             '#FFF5EE',
            'sienna':               '#A0522D',
            'silver':               '#C0C0C0',
            'skyblue':              '#87CEEB',
            'slateblue':            '#6A5ACD',
            'slategray':            '#708090',
            'snow':                 '#FFFAFA',
            'springgreen':          '#00FF7F',
            'steelblue':            '#4682B4',
            'tan':                  '#D2B48C',
            'teal':                 '#008080',
            'thistle':              '#D8BFD8',
            'tomato':               '#FF6347',
            'turquoise':            '#40E0D0',
            'violet':               '#EE82EE',
            'wheat':                '#F5DEB3',
            'white':                '#FFFFFF',
            'whitesmoke':           '#F5F5F5',
            'yellow':               '#FFFF00',
            'yellowgreen':          '#9ACD32'}        
        """        
        
    def confirmExit(self):
        reply = QtGui.QMessageBox.question(self, 'Message',
        "Are you sure to quit?", QtGui.QMessageBox.Yes | 
        QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        
        if reply == QtGui.QMessageBox.Yes:
        #close application
            self.close()
        else:
        #do nothing and return
            pass     
    
if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = AppTemplateMain()
    myapp.show()

    exit_code=app.exec_()
    #print "exit code: ",exit_code
    sys.exit(exit_code)