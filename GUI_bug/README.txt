Explanation of the BUG !

the top lineEditField triggers an event when modified.... OK
the button on its right trigger an event when pushed ... ok
if the user hits ENTER in the lineEditField... the event of the button is triggered !!!!! WRONG !
if the event of this button in disconnected from the button, it is not called anymore when hitting ENTER in the GUI.



