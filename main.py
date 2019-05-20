import math
import cmath
import datetime
import random
import itertools
import time

##the purpose of this application is to generate a dictionary of words customized to some particular user inputs
##For the purpose of penetration testing WPA/WPA2 against
##------------------------------------------Created By: Wulfic---------------------------------------------------
##
##Needs to use leet speak and be able to convert words the user inputs to leet speak
##Needs to be able to combine any of the answers to reach the target min-max character values
##Needs to be able to add in random values inbetween answers
##
##Would be cool if program was able to scrape a facebook page to gather information about what the target likes
##
##Take user inputs and create a dictoary

   

def pw_details(self):
  ##Total length of the password
  pw_ln_min = raw_input('What is the Minimum length of the desired password?(Usually 8)')##PW minimum length
  pw_ln_max = raw_input('What is the Maximum length of the desired password?(Typically no higher than 12)')##PW maximum length
  use_leet = raw_input('Use leet speak for your iterations?')
  if use_leet == 'y':
    iteratation_enabled = raw_input('[Here you can choose the type of leet speak iterations you can use!]\n[1 - Lowercase]\n[2 - Uppercase]\n[3 - Upper/Lowercase]\n\n[Please Enter your choice]: ')
    if iteration_enabled == '1':
      leet_lower()
      print '[Using lowercase leet speak against the dictionary!]'
    if iteration_enabled == '2':
      leet_upper()
      print '[Using uppercase leet speak against the dictionary!]'
    if iteration_enabled == '3':
      leet()
      print '[Using upper/lowercase combo against the dictionary!]'
    else:
      pass
  if use_leet == 'Y':
    iteratation_enabled = raw_input('[Here you can choose the type of leet speak iterations you can use!]\n[1 - Lowercase]\n[2 - Uppercase]\n[3 - Upper/Lowercase]\n\n[Please Enter your choice]: ')
    if iteration_enabled == '1':
      leet_lower()
      print '[Using lowercase leet speak against the dictionary!]'
    if iteration_enabled == '2':
      leet_upper()
      print '[Using uppercase leet speak against the dictionary!]'
    if iteration_enabled == '3':
      leet()
      print '[Using upper/lowercase combo against the dictionary!]'
    else:
      pass
  if use_leet == 'n':
    print '[Leet speak will not be used...]'
    pass
  if use_leet == 'N':
    print '[Leet speak will not be used...]'
    pass
  
##-------------------------------------------------------------------------------------------------------
##should be given a choice about how many questions to be asked. as there will be a TON of possible 
##questions in order to make this process more speedy also include the option to input specific words
##about the target
##Make the questions intelligent and dynamic

def target_questions(self):
  print'[Now we will ask some questions about the target. Answer as many questions as possible]'
  print '[Questions will be asked in the form that YOU are the Target]'
  q01 = raw_input('[What was the house number and street name you lived on as a child?]: ')
  q02 = raw_input('[What were the last four digits of your childhood telephone number?]: ')
  q03 = raw_input('[What primary school did you attend?]: ')
  q04 = raw_input('[In what town or city was your first full time job?]: ')
  q05 = raw_input('[In what town or city did you meet your spouse/partner?]: ')
  q06 = raw_input('[What is the middle name of your oldest child?]: ')
  q07 = raw_input('[What is the middle name of your youngest child?]: ')
  q08 = raw_input('[What is your drivers licence number?(As many characters as you have available)]: ')
  q09 = raw_input('[What is your grandmothers(Mothers Side) maiden name?]: ')
  q10 = raw_input('[What is your grandmothers(Fathers Side) maiden name?]: ')
  q11 = raw_input('[In what town or city did your mother and father meet?]: ')
  q12 = raw_input('[What time of the day were you born?(hh:mm)]: ')
  q13 = raw_input('[What time of the day was your first child born?(hh:mm)]: ')
  q14 = raw_input('[What was the name of your first pet?]: ')
  q15 = raw_input('[What was the name of your 5th grade teacher?]: ')
  q16 = raw_input('[What is your grandfathers(mothers side) first name?]: ')
  q17 = raw_input('[What is your grandfathers(fathers side) first name?]: ')
  q18 = raw_input('[What street did you grow up on?]: ')
  q19 = raw_input('[What is your birthday?(DD:MM:YYYY)]: ')
  q20 = raw_input('[What is your favorite food?]: ')
  q21 = raw_input('[What is your favorite movie?]: ')
  q22 = raw_input('[What is your favorite show?]: ')
  q23 = raw_input('[What is your dream car?]: ')
  q24 = raw_input('[Who is your favoite band?]: ')
  q25 = raw_input('[What is a meaningful number to you?]: ')
  ##Children names  VVVVVVV
  q26 = raw_input('[How many children do you have?(0-6)]: ')##make the questions intelligent
  if q26 == '1':
    child1 = raw_input('[What is your first childs name?]: ')
    childbd1 = raw_input('[What is your first childs birthday?(DD:MM:YYYY)]: ')
  if q26 == '2':
    child1 = raw_input('[What is your first childs name?]: ')
    childbd1 = raw_input('[What is your first childs birthday?(DD:MM:YYYY)]: ')
    child2 = raw_input('[What is your second childs name?]: ')
    childbd2 = raw_input('[What is your second childs birthday?(DD:MM:YYYY)]: ')
  if q26 == '3':
    child1 = raw_input('[What is your first childs name?]: ')
    childbd1 = raw_input('[What is your first childs birthday?(DD:MM:YYYY)]: ')
    child2 = raw_input('[What is your second childs name?]: ')
    childbd2 = raw_input('[What is your second childs birthday?(DD:MM:YYYY)]: ')
    child3 = raw_input('[What is your third childs name?]: ')
    childbd3 = raw_input('[What is your third childs birthday?(DD:MM:YYYY)]: ')
  if q26 == '4':
    child1 = raw_input('[What is your first childs name?]: ')
    childbd1 = raw_input('[What is your first childs birthday?(DD:MM:YYYY)]: ')
    child2 = raw_input('[What is your second childs name?]: ')
    childbd2 = raw_input('[What is your second childs birthday?(DD:MM:YYYY)]: ')
    child3 = raw_input('[What is your third childs name?]: ')
    childbd3 = raw_input('[What is your third childs birthday?(DD:MM:YYYY)]: ')
    child4 = raw_input('[What is your fourth childs name?]: ')
    childbd4 = raw_input('[What is your fourth childs birthday?(DD:MM:YYYY)]: ')
  if q26 == '5':
    child1 = raw_input('[What is your first childs name?]: ')
    childbd1 = raw_input('[What is your first childs birthday?(DD:MM:YYYY)]: ')
    child2 = raw_input('[What is your second childs name?]: ')
    childbd2 = raw_input('[What is your second childs birthday?(DD:MM:YYYY)]: ')
    child3 = raw_input('[What is your third childs name?]: ')
    childbd3 = raw_input('[What is your third childs birthday?(DD:MM:YYYY)]: ')
    child4 = raw_input('[What is your fourth childs name?]: ')
    childbd4 = raw_input('[What is your fourth childs birthday?(DD:MM:YYYY)]: ')
    child5 = raw_input('[What is your fifth childs name?]: ')
    childbd5 = raw_input('[What is your fifth childs birthday?(DD:MM:YYYY)]: ')
  if q26 == '6':
    child1 = raw_input('[What is your first childs name?]: ')
    childbd1 = raw_input('[What is your first childs birthday?(DD:MM:YYYY)]: ')
    child2 = raw_input('[What is your second childs name?]: ')
    childbd2 = raw_input('[What is your second childs birthday?(DD:MM:YYYY)]: ')
    child3 = raw_input('[What is your third childs name?]: ')
    childbd3 = raw_input('[What is your third childs birthday?(DD:MM:YYYY)]: ')
    child4 = raw_input('[What is your fourth childs name?]: ')
    childbd4 = raw_input('[What is your fourth childs birthday?(DD:MM:YYYY)]: ')
    child5 = raw_input('[What is your fifth childs name?]: ')
    childbd5 = raw_input('[What is your fifth childs birthday?(DD:MM:YYYY)]: ')
    child6 = raw_input('[What is your sixth childs name?]: ')
    childbd6 = raw_input('[What is your sixth childs birthday?(DD:MM:YYYY)]: ')
  else:
    pass
  ##Children names^^^^^
  q27 = raw_input('[What is your dogs name?]: ')
  q28 = raw_input('[What is your cats name?]: ')
  q29 = raw_input('[What year were you married?(YYYY)]: ')
  q30 = raw_input('[Who is your favorite band?]: ')
  
  q40 = []
  q40 = raw_input('[Finally Please input any additional information seprated by commas]: ')
  qmaster = [[q01],[q02],[q03],[q04],[q05],[q06],[q07],[q08],[q09],[q10],[q11],[q12],[q13],[q14],[q15],[q16],[q17],[q18],[q19],[q20],[q21],[q22],[q23],[q24],[q25],[q26],[q27],[q28],[q29],[q30]]
  print qmaster##should print the list of objects to be combined
  

  ##Make a length index of the words in the list and call upon them to match thedisreced word length
  ##x = [q01,q02,q03,q04,q05,q06,q07,q08,q09,q10]
  ##for index in x
  ##fetch_len = len(x[0])
  
  #i = 0
  #x = i+1
  #for word in qmaster:
  #  print(word)
  #  len_index == len(word):
  #    for len(word[i]) in word:


#  for word in self:
#      for match in target_questions:
#        if len(qmaster[0]=<pw_ln_min)
            
       
#  return list(itertools.product(*l))

##---------------------------------------------------------------------------------------------------------------



##This section of code is intended to make words into 1337 speak


##----------------------------------------------------------------------------------------------------------------
##This section is used for converting regular text into its "LEET Speak" version of itself
## a,A = 4 or @ | b = 6 | c,C = ( | g,G = & | h,H = # | i,I = ! or 1 | o,O = 0 | s,S = $ or 5 | t,T = 7 | x,X = %
## |||WORDS / PHRASES ||| ate = 8
##----------------------------------------------------------------------------------------------------------------
##Adding the option to choose between different leet speek versions
##Need to add support for writing to file as well as adding in support for sentences
##would also like to create a feature to jumble the word entirely(although this isnt nessasary)
##-----------------------------------------------------------------------------------------------------------------
def file_write(self):
  new_file = raw_input('[Please Enter a file name]: ')
  f= open( new_file + '.txt','w+')
  f.write('%s' + '.txt')

def leet_upper(self):
  ##makes use of uppercase only
  leet_upper = [['A','@','4'],['B','8'],['C','('],['D'],['E','3'],['F'],['G','&','8','6'],['H','#'],['I','!','1'],['J'],['K'],['L'],['M'],['N'],['O','0'],['P'],['Q'],['R'],['S','$','5'],['T','7'],['U'],['V'],['W'],['X','%'],['Y'],['Z','2']]
  l = []
  for letter in self:
      for match in leet_upper:
          if match[0] == letter:
              l.append(match)
  return list(itertools.product(*l))

def leet_lower(self):
  ##makes use of lower case only
  leet_lower = [['a','4','@'],['b','6'],['c','('],['d'],['e','3'],['f'],['g','&','8'],['h','#'],['i','1','!'],['j'],['k'],['l'],['m'],['n'],['o','0'],['p'],['q'],['r'],['s','5','$'],['t','7'],['u'],['v'],['w'],['x','%'],['y'],['z','2']]
  l = []############################## List that holds the returned appended data from itertools
  for letter in self:################# For a letter in the defenition of leet_lower
      for match in leet_lower:######## for a match in itself
          if match[0] == letter:###### If there is a match of the letter then
              l.append(match)######### Append the match to the '"l" list 
  return list(itertools.product(*l))## And start over using the next available match and repeat going through the list one match at a time

def leet(self):
  ##makes use of all capitals and lowercase
  leet_matches = [['a','4','@','A'],['b','8','6','B'],['c','(','C'],['d','D'],['e','3','E'],['f','F'],['g','6','&','8','G'],['h','#','H'],['i','1','!','I'],['j','J'],['k','K'],['l','L'],['m','M'],['n','N'],['o','0','O'],['p','P'],['q',"Q"],['r','R'],['s','5','$','S'],['t','7','T'],['u','U'],['v','V'],['w','W'],['x','%','X'],['y','Y'],['z','2','Z'],['A','4','@','a'],['B','8','6','b'],['C','(','c'],['D','d'],['E','3','e'],['F','f'],['G','6','&','8','g'],['H','#','h'],['I','1','!','i'],['J','j'],['K','k'],['L','l'],['M','m'],['N','n'],['O','0','o'],['P','p'],['Q','q'],['R','r'],['S','5','$','s'],['T','7','t'],['U','u'],['V','v'],['W','w'],['X','%','x'],['Y','y'],['Z','2','z']]
  l = []
  for letter in self:
      for match in leet_matches:
          if match[0] == letter:
              l.append(match)
  return list(itertools.product(*l))

while True:
  intro = raw_input('[Welcome! This program will allow you to make iterations of words you input into leet speak. Please select the type of permutation you would like]\n[1 - Uppercase Characters ONLY]\n[2 - Lowercase Characters ONLY]\n[3 - Upper+Lower Mix]\n\n[Choice]: ')
  if intro == '1':
    word = leet_upper(raw_input('[Please Input word to iterate]: '))## this calls the leet_upper() defenition and the run within its own segment of code
    print '[There are ' + str(len(word)) + ' iterations to process! Continue?]: '
    time.sleep(0.5)
    while True:
      confirm = raw_input('[Y] or [N]: ')
      if confirm == 'y':
        print word
        pass
      if confirm == 'Y':
        print word
      if confirm == 'n':
        break
      if confirm == 'N':
        break
      else:
        print '[Please enter a Valid input [y] or [n]]'
        pass
  if intro == '2':
    word = leet_lower(raw_input('[Please Input word to iterate]: '))## this calls the leet_lower() defenition and the run within its own segment of code
    print '[There are ' + str(len(word)) + ' iterations to process! Continue?]: '
    time.sleep(0.5)
    while True:
      confirm = raw_input('[Y] or [N]: ')
      if confirm == 'y':
        print word
        break
      if confirm == 'Y':
        print word
        break
      if confirm == 'n':
        break
      if confirm == 'N':
        break
      else:
        print 'Please enter a Valid input [y] or [n]'
        pass
  if intro == '3':
    word = leet(raw_input('[Please Input word to iterate]: '))## this calls the leet() defenition and the run within its own segment of code
    print '[There are ' + str(len(word)) + ' iterations to process! Continue?]: '
    time.sleep(0.5)
    while True:
      confirm = raw_input('[Y] or [N]: ')
      if confirm == 'y':
        print word
        break
      if confirm == 'Y':
        print word
        break
      if confirm == 'n':
        break
      if confirm == 'N':
        break
      else:
        print 'Please enter a Valid input [y] or [n]'
        pass
  else:
    pass
  
  
##End of iterations code

