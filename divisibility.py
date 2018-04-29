class Div:
  
  even_numbers = ['0','2','4','6','8']
  multiples_of_three = ['0','3','6','9']
  
  def divisible_by_two_v1(self, number):
    return number/2 == int(number/2)
    
  def divisible_by_two_v2(self, number):
    last_figure = int(str(number)[-1])
    while last_figure > 1:
      last_figure = last_figure - 2
    return last_figure == 0	
    
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
	   significant_figures = Div.remove_mod_three_figures(self,number)
	   if len(significant_figures) >1:
	    addition = Div.sum_elements(self, significant_figures)
	    return Div.divisible_by_three(self,addition)
	   else:
	    return len(significant_figures)==0
	     
  def divisible_by_four(self,number):
	  extended_figures = ['0'] + list(str(number))
	  last_figure = extended_figures[-1]
	  second_last_figure = extended_figures[-2]
	  if second_last_figure in Div.even_numbers:
	    return last_figure in ['0','4','8']
	  else:
	    return last_figure in ['2','6']
	   
	     
	 
	 