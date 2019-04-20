import re
import pycalc.operators as operators


class Calculator():


    def __calculation(self,expr):    
        expr=self.__degree(expr)
       
        place=re.search(r'/|\*|%|&',expr)

        while place!=None:
            #регульрное выражение с конца строки есть вроде
                findBefore=re.search(r'[0-9]+([.][0-9]*)?|[.][0-9]+',expr[place.start()::-1])
                findAfter=re.search(r'[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)',expr[place.start():])
           

                if findAfter==None or findAfter.start()!=1 or  findBefore==None or findBefore.start()!=1:
                    raise Exception("the expression should be written in the following form 'number operator number'")
               
                rezult= '{:.14f}'.format( operators.operators[place[0]](float(findBefore[0][::-1]),float(findAfter[0])))
                begin=expr[:place.start()-len(findBefore[0])]
                expr=begin+rezult+expr[findAfter.end()+place.start():]
                place=re.search(r'/|\*|%|&',expr)
                #добавить сравнение после суммы
        return self.__sum(expr)                 

    def __sum(self,expr):

        if expr[-1]=="+" or expr[-1]=="-":
            raise Exception("'+' or '-'mustn' be the last even in brackets")
    
        splitted=list()

        while expr!="":
            find=re.search(r'[0-9]+([.][0-9]*)?|[.][0-9]+',expr)
            l=expr[:find.end()]
            if l.count("-")%2==1:
                splitted.append(float("-"+find[0]))
            else: splitted.append(float(find[0]))
            expr=expr[find.end():]

        return '{:.14f}'.format((sum(splitted)))
    

    def calculate(self,expr):

       
        while "(" in expr:
        
            end=expr.find(")")
            if end!=len(expr)-1 and expr[end+1] not in operators.operators:
                Exception("no operator after brackets")

        
            begin=expr[:end].rfind("(")
            if begin!=0 and expr[begin-1] not in operators.operators and expr[begin-1]!='-' and expr[begin-1]!='+' :
                raise Exception("no operators before brackets")

            rezult=self.__calculation(expr[begin+1:end])
            expr=expr[:begin]+str(rezult)+expr[end+1:]  

        
        rezult=self.__calculation(expr)

        return rezult

    def __degree (self,expr):
        place=expr.rfind("^")
        #совместить часть вычислений с остальными выражениями

        while place!=-1:

            findBefore=re.search(r'[0-9]+([.][0-9]*)?|[.][0-9]+',expr[place::-1])
            findAfter=re.search(r'[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)',expr[place:])           

            if findAfter==None or findAfter.start()!=1 or  findBefore==None or findBefore.start()!=1:
                raise Exception("the expression should be written in the following form 'number operator number'")
           
            rezult= '{:.14f}'.format( operators.operators["^"](float(findBefore[0][::-1]),float(findAfter[0])))
            begin=expr[:place-len(findBefore[0])]
            expr=begin+rezult+expr[findAfter.end()+place:]
            place=expr.rfind("^")

        return expr


    