# class interface(object): #假设这就是一个接口，接口名可以随意定义，所有的子类不需要实现在这个类中的函数  
#     def Lee(self):
#         pass  
      
#     def Marlon(self):  
#         pass  
   
# class Realaize_interface(interface):  
#     def __init__(self):  
#         pass  
#     def Lee(self):  
#         print ("实现接口中的Lee函数")  
          
          
# class Realaize_interface2(interface):  
#     def __init__(self):  
#         pass  
#     def Marlon(self):  
#         print ("实现接口中的Marlon函数" ) 
       
# obj=Realaize_interface()  
# obj.Lee()  
  
  
# obj=Realaize_interface2()  
# obj.Marlon()  


class Father(object):
    def __init__(self, name):
        self.name=name
        print ( "name: %s" %( self.name) )
    def getName(self):
        return 'Father ' + self.name
 
class Son(Father):
    def getName(self):
        return 'Son '+self.name
 