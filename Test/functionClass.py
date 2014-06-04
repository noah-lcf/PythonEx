#! /usr/bin/env python

http://www.cnblogs.com/wentingtu/archive/2012/05/23/2514776.html

"""
This code demostrates how easy to imprement an object orientated system on a functional programming language.
It only requires a nested hash table.
"""


def Cls(cls=None, **key):
    """ making a new class"""
    key['class'] = cls
    return key

def new(cls, **key):
    """ making an instance """
    key['class'] = cls
    return key


def geta(obj, attr):
    """ getting the attribute of object """
    if attr in obj:
        return obj[attr]
    elif(obj['class']):
        return geta(obj['class'], attr)
    else:
        return None

def tell(obj, method, *av):
    """ tell object do something"""
    fun=geta(obj, method)
    if callable(fun):
        return fun(obj, *av)

if __name__=='__main__':

    def it_work(self, n):
        """This funciton demonstrates how IT engineers work.
           Notice that arguments of thie function is identical to the method 'work' in workers.py"""

        if geta(self, 'position') == 'web creator':
            w = 'makes web site'
        elif geta(self, 'position') == 'server administrator':
            w = 'checks the trafic'
        elif geta(self, 'position') == 'programmer':
            w = 'writes programs'

        print '%s %s for %d, hours using %s on %s' %(geta(self, 'name'), w, n, geta(self, 'language'), geta(self, 'OS'))

    workers = Cls() # dummy class    
    it_workers = Cls(workers, OS='winNT', work=it_work) # class of IT workers    

    henley = new(it_workers, language='PHP', name='henley',    
                 position='web creator', email='henley@livegate.com', age=32, salary=700)    
    thomas = new(it_workers, language='Python', name='Thomas',    
                 position='server administrator', email='thomas@livegate.com', age=37, salary=900)    
    gates  = new(it_workers, language='C', name='Gates',    
                 position='programmer', email='gates@livegate.com', age=42, salary=1200)    
    henley['OS'] = 'Mac'    
    thomas['OS'] = 'Linux'    
    print henley
    tell(henley, 'work', 8)    
    tell(thomas, 'work', 7)    
    tell(gates, 'work', 10)