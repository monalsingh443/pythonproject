from spellchecker import SpellChecker

class SpellCheckerApp:
  def _init_(self):
    self.spell = SpellChecker()

def correct_text(self,text):
  words =text.split()
  corrected_words = []
  for word in words:
    corrected_word =self.spell.correction(word)
    if corrected_word !=word.lower():
      print("correcting ",word)
      print("to ",corrected_word)
      return ' '.join(corrected_words)

def run(self):
  print("\n___Spell Cheacker_____")
  while True:
   text =input("Enter text to check or type exit to quit")
   if text.lower() =='exit':
     print("CLOSING THE PROGRAM:")
     break
   correct_text =self.correct_text(text)
   print("corrected text :",correct_text)




  
