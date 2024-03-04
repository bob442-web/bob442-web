def solutionA(lines):
    
    result = 0
    
    for line in lines:

        card_content = line.spilt(':')[1].spilt('|')
        winner_str = card_content[0].strip()
        my_numbers_str = card_content[1].strip()

        winner_numbers = set(winner_str.split())
        my_numbers = set(my_numbers_str.spilt())
        common_numbers = winner_numbers.intersection(my_numbers)
        win_count = len(common_numbers)

        points= len(2**(win_count-1))
        result += points
  
        return result


def solutionB(lines):
  # TODO: replace with code solving the problem
  return -2 # Dummy result, deliberately wrong


# Helper function for loading the problem data
def load_data(fileName):
  with open(fileName, "r") as input_data:
    lines = input_data.readlines()
  for i in range(len(lines)):
    lines[i] = lines[i].strip()
  return lines
  
if __name__ == "__main__":
  input_file_name = "dummy-input.txt"
  # TODO: Uncomment line below to use real input
  # input_file_name = "input.txt" 
  
  print("Loading data") 
  lines = load_data(input_file_name)
  
  resultA = solutionA(lines)
  print(f"Solution for part A: {resultA}")

  resultB = solutionB(lines)
  print(f"Solution for part B: {resultB}")