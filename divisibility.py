class Div:
  
  """ Divisibility criteria by two, three and four. 
  Function invocation: divisible_by(Parameter1, Parameter2)
  where Parameter1 can be any natural number and Parameter2 can be 'two', 'three' or 'four'."""
  
  even_numbers = ['0','2','4','6','8']
  multiples_of_three = ['0','3','6','9']
    
  def divisible_by_two(self, number):
    last_figure = str(number)[-1]
    return last_figure in Div.even_numbers 
    
  def remove_mod_three_figures(self, number):
    figures = list(str(number))
    not_mod_three_figures = list(str(number))
    for i in range(len(figures)):
      if figures[i] in Div.multiples_of_three:
        not_mod_three_figures.remove(figures[i])
    return not_mod_three_figures
    
  def sum_elements(self, string_list):
    int_list = []
    for i in range(len(string_list)):
      int_list = int_list + [int(string_list[i])]
    return sum(int_list)
  
  def divisible_by_three(self, number):
	   not_mod_three_figures = Div.remove_mod_three_figures(self,number)
	   if len(not_mod_three_figures) >1:
	    addition = Div.sum_elements(self, not_mod_three_figures)
	    return Div.divisible_by_three(self,addition)							
	   else:
	    return len(not_mod_three_figures)==0
		
  def divisible_by_four(self,number):
	  extended_figures = ['0'] + list(str(number))							# It adds an extra figure to have always two digits at least
	  units = extended_figures[-1]
	  tens = extended_figures[-2]
	  if tens in Div.even_numbers:
	    return units in ['0','4','8']
	  else:
	    return units in ['2','6']
	    
  functions_dict = {2:divisible_by_two, 3:divisible_by_three, 4:divisible_by_four}
	
  def divisible_by(self, number, divider):
    return Div.functions_dict[divider](self,number)