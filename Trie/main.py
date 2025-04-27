# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 19:26:30 2021

@author: coderzparadise

Fastest time to implement code and explain Data Structure: Trie
    -7 minutes
"""

from Trie import Trie

if __name__ == "__main__":
    
    # Example on how to use Data Strucutre: Trie
    t = Trie()
    
    t.insert('soccer')
    t.insert('socks')
    
    # Check string if in Data Structure: Trie
    t1 = 'socks'
    t2 = 's'
    t3 = 'a'
    t4 = 'soccerteam'
    
    
    print(f"Is {t1} in Trie?...", t.search_word( t1 ) )
    print(f"Is {t2} in Trie?...", t.search_word( t2 ) )
    print(f"Is {t3} in Trie?...", t.search_word( t3 ) )
    print(f"Is {t4} in Trie?...", t.search_word( 'soccerteam' ) )
    
    print()
    
    print(f"Is {t1} in Trie?...", t.is_prefix( t1 ) )
    print(f"Is {t2} in Trie?...", t.is_prefix( t2 ) )
    print(f"Is {t3} in Trie?...", t.is_prefix( t3 ) )
    print(f"Is {t4} in Trie?...", t.is_prefix( 'soccerteam' ) )
    
    print('\nEnd')
    