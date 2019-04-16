
import difcalc
import CheckAndChange
import argparse

helper="""___o8o_____________________oo 
___8**o__________________o**88 
__$8*8888_____________88$8*_88 
__$8*888$888$$$$$$$$88888***$8 
__$8*8$$8888*******8$88***8$8 
__888$8****************888$8 
__*$8******************8888$8 
__$$********************8888$8_____oooooooo 
_8$8**8************8*****888$8___o$$$$$$8$$8888o 
_$$**8-8**********8-8*****88$8__$$88888********$$8 
_$$***$************$******88$8__$8888*********```$8 
_*$8****88***************88$$*__$888**********````$o 
__8$8**8$8**************88$8____$$8**********``````$8 
____8$88**********8**8888$8_____*$8**********``````$8 
______8$8$$$$$$$$$$$$$8*_________88*******8$$``8*88* 
______*$$**********$$$8ooo_______*$*******8$**8*_* 
_______8$**************$$$888___*$8******8$$* 
_______8$***8$8**88***$$$8$$$$$$$8*******8$* 
_______8$***$$8**$8*$$****$88$8$8*8**888888 
_____8$***$$$****8$$$******88*__*888888* 
______8888$$88888$$8888$$$88 
____________************* """
calculator=difcalc.ComplexCalc()
cheker=CheckAndChange.CandC()
parser = argparse.ArgumentParser(description='Calculation')
parser.add_argument('a', type=str, help='input your expression')
args = parser.parse_args()

try:
    
        if args.a!="--help":
        a=cheker.doAllCh(args.a)
        a=calculator.expressionSearch(args.a)
        
        else: print (helper)

except Exception as e:
        print("Error:  " + e)
else: print(a)


"""
while True:
        a=input()
        try:
                if a!="--help":
                        a=cheker.doAllCh(a)
                        a=calculator.expressionSearch(a)
        
                else: print (helper)

        except Exception as e:
                print("Error:  " + str(e))
        else: print(a)

"""
    
    
