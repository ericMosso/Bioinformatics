# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 15:48:18 2023

"""

def de_bruijn_ize ( st, k ) :
    
    """ Return a list holding, for each k-mer, its left
        k-1-mer and its right k-1-mer in a pair """
        
    edges = []
    
    nodes = set ()
    
    for i in range ( len ( st ) - k + 1 ) :
        
        edges . append ( ( st [ i : i + k - 1 ], st [ i + 1 : i + k ] ) )
        
        nodes . add ( st [ i : i + k - 1 ] )
        
        nodes . add ( st [ i + 1 : i + k ] )
        
    return nodes, edges
