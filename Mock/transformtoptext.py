class TransformTopText(object):
    
    def __init__(cls, parent=None):
        cls.parent = parent
                
        cls.retrieveTextFromTopGui()
        cls.retrievePrefixText()
        cls.addPrefixToEachLine()

    def retrieveTextFromTopGui(cls):
        cls.input_text = str(cls.parent.ui.textEditTop.toPlainText())

    def retrievePrefixText(cls):
        cls.prefix_text = cls.parent.ui.prefixValue.text()
        
    def addPrefixToEachLine(cls):
        text_array = cls.input_text.split('\n')
        new_text_array = [str(cls.prefix_text + ' ' + line) for line in text_array]
        new_text = '\n'.join(new_text_array)
        cls.parent.ui.textEditBottom.setText(new_text)
        