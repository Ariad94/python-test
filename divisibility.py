class Div:
  
  """ Divisibility criteria by two, three and four. 
  Function invocation: divisible_by(Parameter1, Parameter2)
  where Parameter1 can be any natural number and Parameter2 can be 2, 3 or 4."""
  
  even_numbers = ['0','2','4','6','8']
  multiples_of_three = ['0','3','6','9']
    
  def divisible_by_two(self, number):
    last_digit = str(number)[-1]
    return last_digit in Div.even_numbers 
    
  def remove_mod_three_digits(self, number):
    digits = list(str(number))
    not_mod_three_digits = list(str(number))
    for i in range(len(digits)):
      if digits[i] in Div.multiples_of_three:
        not_mod_three_digits.remove(digits[i])
    return not_mod_three_digits
    
  def sum_elements(self, string_list):
    int_list = []
    for i in range(len(string_list)):
      int_list = int_list + [int(string_list[i])]
    return sum(int_list)
  
  def divisible_by_three(self, number):
	   not_mod_three_digits = Div.remove_mod_three_digits(self,number)
	   if len(not_mod_three_digits) >1:
	    addition = Div.sum_elements(self, not_mod_three_digits)
	    return Div.divisible_by_three(self,addition)							
	   else:
	    return len(not_mod_three_digits)==0
		
  def divisible_by_four(self,number):
	  extended_digits = ['0'] + list(str(number))			# It adds an extra digit to have always two digits at least
	  units = extended_digits[-1]
	  tens = extended_digits[-2]
	  if tens in Div.even_numbers:
	    return units in ['0','4','8']
	  else:
	    return units in ['2','6']
	    
  functions_dict = {2:divisible_by_two,
                    3:divisible_by_three, 
                    4:divisible_by_four}
	
  def divisible_by(self, number, divider):
    return Div.functions_dict[divider](self,number)
