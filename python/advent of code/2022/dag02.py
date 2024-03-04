def solutionA(lines):
   result = 0
   for game in lines :
        A = rock
        B = paper
        C = scissors

        h = line.spilt('')
        modstanderens_træk = h[0]
        vores_modtræk = h[1]

        m = set()

        # if a:

        # if b:

        # if c: 

        if winning:
            points = n + 6

      a = set()

      points = 

    
    result = result + points   
return result    



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
