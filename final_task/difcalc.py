import re
import easyCalculation 
import math

class ComplexCalc():
   
    calc=easyCalculation.Calculator()

    math_functions = {attr:getattr(math, attr) for attr in dir(math) if callable(getattr(math, attr))}


    const={
    "pi":math.pi,
    "e":math.e
    }


    def expressionSearch(self,expr):

        while True:

            func=re.search(r'[A-ZAa-z]+1?0?',expr)

            if func==None:
                return self.calc.calculate(expr)
        
            afterExpr=func.end()
            k=func.start()
            if func[0] in ComplexCalc.const:

                s=ComplexCalc.const[func[0]]
                expr=expr[:k]+str(s)+expr[afterExpr:]
                continue
            
            searcher=0
            count=1
            for one in expr[afterExpr+1:]:

                searcher+=1
                if one ==")":
                    count-=1
                if one=="(":
                    count+=1
                if count==0:
                    break
            end=searcher+afterExpr
        #выкинуть если конец строки
            if expr[afterExpr] != '(':
           
                raise Exception("the expression must be written in the following way 'function(expression)'")

            else: 
           
                a=self.__findreplacement(func[0],expr[afterExpr+1:end])
                expr=expr[:k]+a+expr[end+1:]


    def __findreplacement(self,func,expr):

        if  func in ComplexCalc.math_functions:
            l=expr.split(",")
            
            k=[]
            for each in l:               
                k.append(float(self.expressionSearch(each)))

            a=round(ComplexCalc.math_functions[func](*k),8)      

        else: 
    
            raise Exception("Indefined function")
        return str(a)

 
