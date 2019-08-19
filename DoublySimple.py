"""
   _______________________________________________________________________________________________

	**************************************************************************************

	Component:	DoublySimple

        Description:	Simple function library managing a doubly linked list

	    Assumptions:	Python ver. 2.7.14 or higher.
                        All entries in a doubly linked list constitute a Python dictionary.
                        Each element of the dictionary is a list containing the following:
    
                        a.  next-entry key value ('' if last entry)
                        b.  prior-entry key value ('' if first entry)
                        c.  data content

	Author:		T. Freund

	Version:	DoublySimple.2019.06
	
	**************************************************************************************

    MIT License
    
	Copyright 2019 by Dig.y.SoL LLC

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

	**************************************************************************************

"""

"""
	addlink:		    add an entry to a linked list

	arguments:			1. a dictionary representing the doubly linked list
	                    
	                    2. a list consisting of 2 elements:
	                    
	                        1 - the key representing the link address
	                        2 - a 2-element list consisting of:
	                            1.  the key address for the next entry in the list
                                    (NOTE: the last entry in the list has a value of '')
                                2.  the data content for this link
                                

	return value:		0   -   entry addition went OK
	                    -1  -   first argument is not a dictionary
	                    -2  -   second argument is not a list with 2 elements
	                    -3  -   first element of second argument is an existing key address in the linked list
	
"""

def addlink(lst,lnk):
    # if the first argument is a dictionary ....
    if isinstance(lst,dict):
        # if the second argument is a 2-element list ....
        if isinstance(lnk,list) and len(lnk) == 2:
            k = lnk[0]   # the key for this link
            val = lnk[1] # the data content for this link
            # if the key is not in the linked list ....
            if k not in lst.keys():
                pr = ''
                # if the linked list is not empty (first entry)
                if len(lst) > 0:
                    pr = listend(lst)
                    # set the the key address for the current last entry in the list to the key address of the new entry
                    lst[pr][0] = k
                # add the new entry as a the last entry in the list
                lst[k] = ['',pr,val]
                return 0
            else:
                return -3
        else:
            return -2
    else:
        return -1

"""
	chglink:		    change the data content of an entry in a linked list

	arguments:			1. a dictionary representing the doubly linked list
	                    
	                    2. a list consisting of 2 elements:
	                    
	                        1 - the key address of the entry to be changed
	                        2 - the new data content for this link
                                

	return value:		0   -   entry addition went OK
	                    -1  -   first argument is not a dictionary
	                    -2  -   second argument is not a list with 2 elements
	                    -3  -   first element of second argument is not an existing key address in the linked list
	
"""

def chglink(lst,val):
    # if the first argument is a dictionary ....
    if isinstance(lst,dict):
        # if the second argument is a 2-element list ....
        if isinstance(val,list) and len(val) == 2:
            # if the key is in the linked list ....
            if val[0] in lst:
                # replace the entry data content with the new data content
                lst[val[0]][2] = val[1]
                return 0
            else:
                return -3
        else:
            return -2
    else:
        return -1

"""
	remlink:		    remove an entry in a linked list

	arguments:			1. a dictionary representing the doubly linked list
	                    
	                    2. the key address of the entry to be removed
                                

	return value:		0   -   entry data content change went OK
	                    -1  -   first argument is not a dictionary
	                    -2  -   key address is a list or dictionary
	                    -3  -   key address does not exist in the linked list
	
"""
        
def remlink(lst,k):
    # if the first argument is a dictionary ....
    if isinstance(lst,dict):
        # if the second argument is not a list or dictionary ....
        if all([not isinstance(k,list), not isinstance(k,dict)]):
            # if the key is in the linked list ....
            if k in lst.keys():
                nxt = lst[k][0] # record the next-entry address in the entry to be removed
                pr = lst[k][1] # record the prior-entry address in the entry to be removed
                # if the entry to be removed is not the last one ...
                if nxt <> '':
                    # record the prior entry for the entry to be removed
                    # as the prior entry for the entry following the one to be removed
                    lst[nxt][1] = pr
                else:
                    # record the next-entry address for the entry prior to the one being removed
                    # as the last one in the linked list 
                    lst[pr][0] = ''
                # if the entry to be removed is not the first one ...
                if pr <> '':
                    # record the next entry for the entry to be removed
                    # as the next entry for the entry preceeding the one to be removed
                    lst[pr][0] = nxt
                else:
                    # record the prior-entry address for the entry following to the one being removed
                    # as the first one in the linked list 
                    lst[nxt][1] = ''
                lst.pop(k)   # remove the target entry 
                return 0            
            else:
                return -3
        else:
            return -2
    else:
        return -1

"""
	remwho:		        remove entries in a doubly linked list containing a particular data content value

	arguments:			1. a dictionary representing the doubly linked list
	                    
	                    2. the value being searched in the data content
                                

	return value:		0   -   all list items with the target value removed
	                    -1  -   first argument is not a dictionary
	                    other non-zero - some list items were no removed
	
"""
def remwho(lst,val):
    # search for all keys containing the value being sought
    klst = listsearch(lst,val)
    return sum([remlink(lst,x) for x in klst]) 

"""
	addbatch:		    add a list of objects to a linked list

	arguments:			1. a dictionary representing the doubly linked list
	                    
	                    2. a list of scalar values to be added as entries to the doubly linked list
                                

	return value:		0   -   entry additions went OK
	                    -1  -   first argument is not a dictionary
	                    -2  -   second argument is not a list
	
"""

def addbatch(lst,vals):
    # if the first argument is a dictionary ....
    if isinstance(lst,dict):
        # if the second argument is a list ....
        if isinstance(vals,list):
            # if the doubly linked list is already populated ....
            maxk = int(max(lst.keys())) + 1 if len(lst) > 0 else 0
            # add all the objects in this list to the linked list with
            # a key based on the occurrence of the value in the input list
            return sum([addlink(lst,[str(vals.index(x)+maxk),x]) for x in vals]) 
        else:
            return -2 
    else:
        return -1

"""
	showlist:		    show a linked list in linkage order

	arguments:			a dictionary representing the doubly linked list
                                
                                
    return value:		list of the entries based on the order in which the next-entry addresses occur
	
"""
        
def showlist(lst):
    # get the very first entry in the linked list
    frst = [y for y in [x for x in lst] if y not in [lst[x][0] for x in lst if lst[x][0] <> '']][0]
    # initialize the resultant list with the first entry and its key address
    fnl = [[frst,lst[frst]]]
    # get the next-entry address for the first entry
    nxt = lst[frst][0]
    # while this is not the last entry ....
    while nxt <> '':
        # add the next entry and its key address to the resultant list
        fnl.append([nxt,lst[nxt]])
        # get the next-entry address for this entry
        nxt = lst[nxt][0]
    return fnl

"""
	liststart:		    show start node of a linked list

	arguments:			a dictionary representing the doubly linked list
                                
                                
    return value:		key address of the start node
                        Null string - no start node found
	
"""
            
def liststart(lst):
    r = [x for x in lst if lst[x][1] == '']
    return r[0] if len(r) > 0 else ''

"""
	listend:		    show end node of a linked list

	arguments:			a dictionary representing the doubly linked list
                                
                                
    return value:		key address of the end node
                        Null string - no end node found
	
"""
            
def listend(lst):
    r = [x for x in lst if lst[x][0] == '']
    return r[0] if len(r) > 0 else ''

"""
	listflatten:		convert a list of lists, dictionaries, and scalar values to just a list of scalar values

	arguments:			a hybrid list or dictionary
                                
                                
    return value:		a "flattened" list
	
"""
    
def listflatten(lst):
    r = []
    for x in lst:
        z = lst[x] if isinstance(lst,dict) else x
        if isinstance(z,list):
            for y in z:
                if isinstance(y,list) or isinstance(y,dict):
                    r += listflatten(y)
                else:
                    r.append(y)
        elif isinstance(z,dict):
            for y in z:
                if isinstance(z[y],list) or isinstance(z[y],dict):
                    r += listflatten(z[y])
                else:
                    r.append(z[y])
        else:
            r.append(z)
    return r
    
"""
	listsearch:		    show all key addresses that contain a scalar value in their content

	arguments:			a dictionary representing the doubly linked list
	                    a scalar value to be searched for
                                                                
    return value:		list of key addresses containing a matching scalar value
    
    assumptions:        linked list is assumed to have at least 2 entries
	
"""
    
def listsearch(lst,val):
    nxtnode = liststart(lst)   # get the start node of the linked list
    keylst = []
    
    # while this is not the end node ....
    while nxtnode <> '':
        nxtval = lst[nxtnode][2]    # get the content of this node
        if isinstance(nxtval,list) or isinstance(nxtval,dict): # if the content is a list or dictionary ....
            if val in listflatten(nxtval):
                keylst.append(nxtnode)
        else:   # if the content is a scalar value (string,number,or boolean)
            if isinstance(val,str) and val in nxtval:
                keylst.append(nxtnode)
            elif val == nxtval:
                keylst.append(nxtnode)
        nxtnode = lst[nxtnode][0]
    return keylst
    
"""
	getcontent:		    retrieve the data content of a list entry

	arguments:			a dictionary representing the doubly linked list
	                    key address of an entry in the list
                                                                
    return value:		data contents of the entry
                        None - if the list is not a dictionary or there is no entry for the key value
	
"""

def getcontent(lst,thekey):
    return lst[thekey][2] if isinstance(lst, dict) and thekey in lst.keys() else None
        
