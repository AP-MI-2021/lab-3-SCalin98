'''
Acesta este fisierul main.cpy pentru laboratorul nr. 3
'''
import sys
import copy

def is_prime(n:int)-> bool :
    if n <= 1 : return False
    elif n == 2 : return True
    for divisor in range(2,n) :
       if n%divisor == 0 :
         return False
    return True

def get_longest_product_is_odd(lst: list[int]) -> list[int]:
  '''
  Genereaza o lista cu cea mai lunga subsecventa cu proprietatea ca produsul membrilor sai este numar impar
  :param lst: Furnizeaza lista din care va fi extrasa subsecventa
  :return: Lista cu elemente numere intregi care contine subsecventa cu proprietatea ceruta.
  '''
  returnLst = []
  returnListIndex1 = 0
  returnListIndex2 = 0
  currentListIndex1 = 0
  currentListIndex2 = 0
  for mainListElement in lst :
      currentListIndex2 = currentListIndex2 + 1
      if((mainListElement%10)%2 != 0):
        if(currentListIndex2 - currentListIndex1 >= returnListIndex2 - returnListIndex1) :
          returnListIndex1 = currentListIndex1
          returnListIndex2 = currentListIndex2
      else :
        currentListIndex1 = currentListIndex2
  for indexRetListCopy in range (returnListIndex1,returnListIndex2):
       returnLst.append(lst[indexRetListCopy])
  return returnLst

def get_longest_concat_is_prime(lst: list[int]) -> list[int]:
    '''
    Determina si construieste cea mai lunga subsecventa cu proprietatea ca membrii sai, concatenati, formeaza un numar prim
    :param lst: Lista cu elemente numere intregi din care va fi preluata subsecventa
    :return: Lista cu numere intregi care contine subsecventa
    '''
    returnLst = []
    returnListIndex1 = 0
    returnListIndex2 = 0
    retListIsNotEmpty = False
    for currentListIndex1 in range (0,len(lst)) :
        lstMemToStr = ' '
        if lst[currentListIndex1] != 0 :
            for currentListIndex2 in range(currentListIndex1,len(lst)) :
                 lstMemToStr = lstMemToStr + str(lst[currentListIndex2])
                 isPrime = is_prime(int(lstMemToStr))
                 if isPrime :
                      retListIsNotEmpty = True
                      if currentListIndex2 - currentListIndex1 >= returnListIndex2 - returnListIndex1 :
                         returnListIndex1 = currentListIndex1
                         returnListIndex2 = currentListIndex2
    if retListIsNotEmpty :
         for indexRetListCopy in range(returnListIndex1, returnListIndex2+1):
              returnLst.append(lst[indexRetListCopy])
    return returnLst


def test_get_longest_product_is_odd() :
   assert get_longest_product_is_odd([]) == [], 'Lista fara elemente are subsecventa'
   assert get_longest_product_is_odd([0]) == [], 'Lista cu doar elementul 0 are subsecventa 0'
   assert get_longest_product_is_odd([1,3,7]) == [1,3,7], 'Lista 1,3,7 nu are subsecventa identica cu ea'

def test_get_longest_concat_is_prime() :
   assert get_longest_concat_is_prime([]) == [], 'Lista fara elemente are subsecventa'
   assert get_longest_concat_is_prime([2,2,7,2]) == [2,2,7], 'Cea mai lunga subsecventa nu este 2,2,7'
   assert get_longest_concat_is_prime([0,0,0,0]) == [], '0,0,0,0 e subsecventa'
   assert get_longest_concat_is_prime([0, 0, 4, 0]) == [], '4 e subsecventa'

def use_get_longest_product_is_odd(lst : list[int]) :
    retList = get_longest_product_is_odd(lst)
    if (len(retList) > 0):
        print(*retList)
    else:
        print("Nu exista subsecventa")
def use_get_longest_concat_is_prime(lst : list[int]) :
    retList = get_longest_concat_is_prime(lst)
    if(len(retList) > 0) : print (*retList)
    else : print("Nu exista subsecventa")

def main():
  test_get_longest_concat_is_prime()
  test_get_longest_product_is_odd()
  # Interfata de tip consola aici
  alegereUtilizator = -1
  lst = []
  while alegereUtilizator != 4 :
      print ('1.Introduce elemente lista. Apasati enter pentru a termina introducerea elementelor.')
      print ('2.Afisati subsecventa cu prima proprietate.')
      print ('3.Afisati subsecventa cu a doua proprietate.')
      print ('4.Iesiti din program')
      alegereUtilizator = int(input("Alegerea dvs : "))
      if(alegereUtilizator == 1) :
          strAlegere = '-'
          lst.clear()
          elemIndex = 1
          while strAlegere != '' :
                print ('Lista[',elemIndex,'] = ')
                strAlegere = input()
                if strAlegere != '' : lst.append(int(strAlegere))
                elemIndex = elemIndex + 1
      elif(alegereUtilizator == 2) : use_get_longest_product_is_odd(lst)
      elif(alegereUtilizator == 3) : use_get_longest_concat_is_prime(lst)


if __name__ == '__main__':
  main()
