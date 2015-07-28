class TransformTopText(object):
    
    def __init__(self, parent=None):
        self.parent = parent
                
        self.retrieveTextFromTopGui()
        self.retrievePrefixText()
        self.addPrefixToEachLine()

    def retrieveTextFromTopGui(self):
        self.input_text = str(self.parent.ui.textEditTop.toPlainText())

    def retrievePrefixText(self):
        self.prefix_text = self.parent.ui.prefixValue.text()
        
    def addPrefixToEachLine(self):
        text_array = self.input_text.split('\n')
        new_text_array = [str(self.prefix_text + ' ' + line) for line in text_array]
        new_text = '\n'.join(new_text_array)
        self.parent.ui.textEditBottom.setText(new_text)
        
    