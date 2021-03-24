from flask import Flask
from operators import Operatorss
from exception import *

app=Flask(__name__)

@app.route('/<methods>/<int:a>/<int:b>')
def login(methods, a, b):
    oa = Operatorss(a,b)
    if methods == 'add':
        try:
            if a<10 and b<10 :
                result = oa.add(a,b)
                return str(result)
            else:
                raise LargeNumberError("enter small number")
        except LargeNumberError as e:
            return str(e)

    if methods == 'sub':
        try:
            if a>b:
                result = oa.sub(a,b)
                return str(result)
            else:
                raise SubError("enter a value greater than b")
        except SubError as s:
            return str(s)

    if methods == 'mul':
        try:
            if a<10 and b<10:
                result = oa.mul(a,b)
                return str(result)
            else:
                raise MulError("enter a value greater than b")
        except MulError as m:
            return str(m)
    
    if methods == 'div':
        try:
            if b != 0:
                result = oa.div(a,b)
                return str(result)
            else:
                raise DivError("enter a value greater than 0")
        except DivError as d:
            return str(d)

        
if __name__ == '__main__':
    app.run(debug=True,port=5004)