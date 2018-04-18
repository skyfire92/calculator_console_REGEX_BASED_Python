import re

def fast_sanity_check(inputstring):
	
	regex_pattern_extract_mult_and_div = 	"(\\+|-?[0-9]+(\\.[0-9]+)?)(\\*|/)(\\+|-?[0-9]+(\\.[0-9]+)?)"
	
	regex_pattern_extract_add_and_subtr = "(\\+|-?[0-9]+(\\.[0-9]+)?)(\\+|-)(\\+|-?[0-9]+(\\.[0-9]+)?)"

	if (re.search(regex_pattern_extract_mult_and_div, inputstring) or re.search(regex_pattern_extract_add_and_subtr, inputstring)) and not re.search(".*(\\+{2})|(-{2}).*", inputstring):
		return True
	else:
		return False

def	calculate_mult_and_div(inputstring):

	regex_pattern_extract_mult_and_div = 	"(\\+|-?[0-9]+(\\.[0-9]+)?)(\\*|/)(\\+|-?[0-9]+(\\.[0-9]+)?)"

	while re.search(regex_pattern_extract_mult_and_div, inputstring):
		m=re.search(regex_pattern_extract_mult_and_div, inputstring)

		group_before_calculation_mult_and_div = m.group(0)
		operand1 = float(m.group(1))
		operand2 = float(m.group(4))
		operation_sign = m.group(3)

		if (operand2 == 0) and (operation_sign == '/'):
			return "error"
		
		def mult(operand1, operand2):
			operation_result = operand1 * operand2
			return operation_result

		def div(operand1, operand2):
			operation_result = operand1 / operand2
			return operation_result

		options = {
					'*':mult,
				    '/':div
				  }
		
		operation_result = options[operation_sign](operand1,operand2)

		inputstring = inputstring.replace(group_before_calculation_mult_and_div, str(operation_result))	

	return inputstring;


def calculate_add_and_subtr(inputstring):

	regex_pattern_extract_add_and_subtr = "(\\+|-?[0-9]+(\\.[0-9]+)?)(\\+|-)(\\+|-?[0-9]+(\\.[0-9]+)?)"

	while re.search(regex_pattern_extract_add_and_subtr, inputstring):
		m=re.search(regex_pattern_extract_add_and_subtr, inputstring)

		group_before_calculation_add_and_subtr = m.group(0)

		operand1 = float(m.group(1))
		operand2 = float(m.group(4))
		operation_sign = m.group(3)						

		def add(operand1, operand2):
			operation_result = operand1 + operand2
			return operation_result

		def subtract(operand1, operand2):
			operation_result = operand1 - operand2
			return operation_result

		options = {
					'+':add,
				    '-':subtract
				  }
		
		operation_result = options[operation_sign](operand1,operand2)
	
		inputstring = inputstring.replace(group_before_calculation_add_and_subtr, str(operation_result))	
	
	return inputstring


def find_and_calculate_parentheses(inputstring):
	
	regex_pattern_extract_parenthesis = "(\\()([^\\(]+?)(\\))"

	while re.search(regex_pattern_extract_parenthesis, inputstring):
		m=re.search(regex_pattern_extract_parenthesis, inputstring)

		group_before_parentheses_extraction = m.group(0)
		matched_group = m.group(2)

		matched_group = calculate_mult_and_div(matched_group)
		if matched_group == "error":
		
			return "error";
		
		matched_group = calculate_add_and_subtr(matched_group)

		inputstring = inputstring.replace(group_before_parentheses_extraction, str(matched_group))
	
	return inputstring


input_expression = input("Enter arithmetic expression: (enter q to exit)\n")

while input_expression != "q":

	if (input_expression == "error"):
		input_expression = input("Enter arithmetic expression: (enter q to exit)\n")
		continue

	input_expression = ''.join(input_expression.split()) #delete spaces in input string

	if fast_sanity_check(input_expression):

		input_expression = find_and_calculate_parentheses(str(input_expression))
		if (input_expression == "error"):
			print("Division by zero error")
			continue

		input_expression = calculate_mult_and_div(str(input_expression))
		if (input_expression == "error"):
			print("Division by zero error")
			continue

		input_expression = calculate_add_and_subtr(str(input_expression))
		print("Result is {0}".format(input_expression))
		input_expression = input("Enter arithmetic expression: (enter q to exit)\n")
	else:
		print("Wrong input")
		input_expression = input("Enter arithmetic expression: (enter q to exit)\n")
print("Finished")






