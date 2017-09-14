import wpf
import clr
clr.AddReference("System.Drawing")
clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import Application, Button, Form, Label

from System.Windows import Application, Window

class MyWindow(Window):
    
    def __init__(self):
        wpf.LoadComponent(self, 'WpfApplication1.xaml')
        self.txtNumeros.Text = "0"
        self.firstNumber = None
        self.secondNumber = None
        self.operationType = None
    
    def Operation_Click(self, sender, e):
        self.operationType = sender.Tag


    def Button_Click(self, sender, e):
        if sender.Name == "uno":
            if self.firstNumber is None:
                self.firstNumber = "1"
                self.txtNumeros.Text = self.firstNumber
            elif self.firstNumber is not None and self.operationType is None:
                self.firstNumber += sender.Tag
                self.txtNumeros.Text = self.firstNumber
            elif self.operationType is not None:
                self.txtNumeros.Text = ""
                self.secondNumber = "1"
        elif sender.Name == "dos":
            self.firstNumber = "2"

        elif sender.Name == "tres":
            self.firstNumber = "3"

        elif sender.Name == "cuatro":
            self.firstNumber = "4"

        elif sender.Name == "cinco":
            self.firstNumber = "5"

        elif sender.Name == "seis":
            self.firstNumber = "6"

        elif sender.Name == "siete":
            self.firstNumber = "7"

        elif sender.Name == "ocho":
            self.firstNumber = "8"

        elif sender.Name == "nueve":
            self.firstNumber = "9"

        elif sender.Name == "cero":
            self.firstNumber = "0"

    def result():
        result = int(firstNumber) + operationType + int(secondNumber)
        txtNumeros.Text = str(result)
    
if __name__ == '__main__':
    Application().Run(MyWindow())


    