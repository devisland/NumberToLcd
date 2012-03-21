import unittest

def numberToLcd(num):
    
    dicionario = {
        0 : [" - ",
             "| |",
             "   ",
             "| |",
             " - "],
        1 : ["   ",
             " | ",
             "   ",
             " | ",
             "   "],
        2 : [" - ",
             "  |",
             " - ",
             "|  ",
             " - "],
        3 : [" - ",
             "  |",
             " - ",
             "  |",
             " - "],
        4 : ["   ",
             "| |",
             " - ",
             "  |",
             "   "],
        5 : [" - ",
             "|  ",
             " - ",
             "  |",
             " - "],
        6 : [" - ",
             "|  ",
             " - ",
             "| |",
             " - "],
        7 : [" - ",
             "  |",
             "   ",
             "  |",
             "   "],
        8 : [" - ",
             "| |",
             " - ",
             "| |",
             " - "],
        9 : [" - ",
             "| |",
             " - ",
             "  |",
             " - "]
    }
    
    linha1 = ""
    linha2 = ""
    linha3 = ""
    linha4 = ""
    linha5 = ""
    
    for caracter in str(num):
        numero_atual = int(caracter)
        
        linha1 = linha1 + dicionario[numero_atual][0]
        linha2 = linha2 + dicionario[numero_atual][1]
        linha3 = linha3 + dicionario[numero_atual][2]
        linha4 = linha4 + dicionario[numero_atual][3]
        linha5 = linha5 + dicionario[numero_atual][4]

    return [linha1, linha2, linha3, linha4, linha5]

class TestNumberToLcd(unittest.TestCase):
    def testDeveExibirONumeroZeroCorretamente(self):
        zero = [" - ",
                "| |",
                "   ",
                "| |",
                " - "]
        
        assert numberToLcd(0) == zero

    def testDeveExibirONumeroUmCorretamente(self):
        um = ["   ",
              " | ",
              "   ",
              " | ",
              "   "]
    
        assert numberToLcd(1) == um

    def testDeveExibirONumeroDoisCorretamente(self):
        dois = [" - ",
                "  |",
                " - ",
                "|  ",
                " - "]
        
        assert numberToLcd(2) == dois
    
    def testDeveExibirONumeroTresCorretamente(self):
        tres = [" - ",
                "  |",
                " - ",
                "  |",
                " - "]
        
        assert numberToLcd(3) == tres

    def testDeveExibirONumeroQuatroCorretamente(self):
        quatro = ["   ",
                  "| |",
                  " - ",
                  "  |",
                  "   "]
    
        assert numberToLcd(4) == quatro

    def testDeveExibirONumeroCincoCorretamente(self):
        cinco = [" - ",
                 "|  ",
                 " - ",
                 "  |",
                 " - "]
    
        assert numberToLcd(5) == cinco

    def testDeveExibirONumeroSeisCorretamente(self):
        seis = [" - ",
                "|  ",
                " - ",
                "| |",
                " - "]
    
        assert numberToLcd(6) == seis

    def testDeveExibirONumeroSeteCorretamente(self):
        sete = [" - ",
                "  |",
                "   ",
                "  |",
                "   "]
    
        assert numberToLcd(7) == sete

    def testDeveExibirONumeroOitoCorretamente(self):
        oito = [" - ",
                "| |",
                " - ",
                "| |",
                " - "]
    
        assert numberToLcd(8) == oito

    def testDeveExibirONumeroNoveCorretamente(self):
        nove = [" - ",
                "| |",
                " - ",
                "  |",
                " - "]

        assert numberToLcd(9) == nove
    
    def testDeveExibirONumeroDezCorretamente(self):
        dez = ["    - ",
               " | | |",
               "      ",
               " | | |",
               "    - "]
        
        assert numberToLcd(10) == dez

    def testDeveExibirONumeroQuinzeCorretamente(self):
        quinze = ["    - ",
                  " | |  ",
                  "    - ",
                  " |   |",
                  "    - "]

        assert numberToLcd(15) == quinze

    def testDeveExibirONumeroDaBest(self):
        besta = [" -  -  - ",
                 "|  |  |  ",
                 " -  -  - ",
                 "| || || |",
                 " -  -  - "]

if __name__ == '__main__':
    unittest.main()

