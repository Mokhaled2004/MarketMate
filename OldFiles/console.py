#!/usr/bin/python3
"""Defines the MarketMate console."""


import cmd
import sys  
import re
from shlex import split
from Models.engine.file_storage import FileStorage
from Models.base_model import BaseModel 
from Models.user import User
from Models.product import Product
from Models.review import Review
from Models.order import Order
from Models.market import Market

def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class MarketMateCommand(cmd.Cmd):
    
    """Defines the MarketMate command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """
    
    prompt = "(MarketMate) "
    
    __classes = {
        
        "BaseModel",
        "User",
        "Product",
        "Review",
        "Order",
        "Market"
        
    }
    
    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass
    
    
    def default(self, arg) :
        """Default behavior for cmd module when input is invalid"""
        
        
        argdict = {
        
        "all": self.do_all,
        "show": self.do_show,
        "destroy": self.do_destroy,
        "count" : self.do_count,
        "update": self.do_update,
        
        }
        
        match = re.search(r"\.",arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)",argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
                
        print("*** Unknown syntax: {}".format(arg))
        return False
    
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    
    
    def do_EOF(self, arg):
        """Quit command to exit the program"""
        print("")
        return True
    
    def do_create(self, arg):
        """Create a new instance of a class
        Create a new class instance and print its id."""
        
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
    
        elif argl[0] not in MarketMateCommand.__classes:
            print("** class doesn't exist **")
        
        else:
        
            print(eval(argl[0])().id)
        FileStorage.save(self)
        
    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """     
        
        argl = parse(arg)
        objdict = FileStorage.all(self)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in MarketMateCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])
            
            
    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id.
        """
        
        argl = parse(arg)
        objdict = FileStorage.all(self)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in MarketMateCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(argl[0], argl[1])]
            FileStorage.save(self)
        
    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects.
        """
        
        argl = parse(arg)
        if len(argl) > 0 and argl[0] not in MarketMateCommand.__classes:
            print("** class doesn't exist **")
            
        else:
            
            objl = []
            for obj in FileStorage.all(self).values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(str(obj.__str__()))
                elif len(argl) == 0:
                    objl.append(str(obj.__str__()))
            print(objl) 
            
            
    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Display the number of instances of a given class.
        """
        
        argl = parse(arg)
        count = 0
        for obj in FileStorage.all(self).values():
            if argl[0] == obj.__class__.__name__:
                count += 1
                        
        print(count)
        
        
    def do_update(self, arg):
        
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary.
        """
        
        argl = parse(arg)   
        objdict = FileStorage.all(self)
        
        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in MarketMateCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        
        
        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        FileStorage.save(self)
        
        
if __name__ == "__main__":
    MarketMateCommand().cmdloop()
        