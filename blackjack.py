import random
import os


class Card:

   def __init__(self, card_face, value, symbol):
       self.card_face = card_face
       self.value = value
       self.symbol = symbol


def show_cards(cards, hidden):
   s = ''
   for card in cards:
       s = s + '\t ________________'
   if hidden:
       s += '\t ________________'
   print(s)

   s = ''
   for card in cards:
       s = s + '\t|                |'
   if hidden:
       s += '\t|                |'
   print(s)

   s = ''
   for card in cards:
       if card.card_face in ['J', 'Q', 'K', 'A']:
           s = s + '\t|  {}             |'.format(card.card_face)
       elif card.value == 10:
           s = s + '\t|  {}            |'.format(card.value)
       else:
           s = s + '\t|  {}             |'.format(card.value)

   if hidden:
       s += '\t|                |'
   print(s)

   s = ''
   for card in cards:
       s = s + '\t|                |'
   if hidden:
       s += '\t|      * *       |'
   print(s)

   s = ''
   for card in cards:
       s = s + '\t|                |'
   if hidden:
       s += '\t|    *     *     |'
   print(s)

   s = ''
   for card in cards:
       s = s + '\t|                |'
   if hidden:
       s += '\t|   *       *    |'
   print(s)

   s = ''
   for card in cards:
       s = s + '\t|                |'
   if hidden:
       s += '\t|   *       *    |'
   print(s)

   s = ''
   for card in cards:
       s = s + '\t|       {}        |'.format(card.symbol)
   if hidden:
       s += '\t|          *     |'
   print(s)

   s = ''
   for card in cards:
       s = s + '\t|                |'
   if hidden:
       s += '\t|         *      |'
   print(s)

   s = ''
   for card in cards:
       s = s + '\t|                |'
   if hidden:
       s += '\t|        *       |'
   print(s)

   s = ''
   for card in cards:
       s = s + '\t|                |'
   if hidden:
       s += '\t|                |'
   print(s)

   s = ''
   for card in cards:
       s = s + '\t|                |'
   if hidden:
       s += '\t|                |'
   print(s)

   s = ''
   for card in cards:
       if card.card_face in ['J', 'Q', 'K', 'A']:
           s = s + '\t|            {}   |'.format(card.card_face)
       elif card.value == 10:
           s = s + '\t|           {}   |'.format(card.value)
       else:
           s = s + '\t|            {}   |'.format(card.value)
   if hidden:
       s += '\t|        *       |'
   print(s)

   s = ''
   for card in cards:
       s = s + '\t|________________|'
   if hidden:
       s += '\t|________________|'
   print(s)
   print()