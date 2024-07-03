#Excited to share my first Python project!"
#Implemented multiple-choice questions with random selection.
#Designed a scoring system to track user performance.
#Added basic input validation for user responses.


questions = [
  [
    "Which animal is known as the 'Ship of the Desert'?", "Camel", "Goat", "Lion","Tiger", "None", 1],
  [
    "Which language was used to create facebook?", "Python", "French", "JavaScript","Php", "None", 4],
  [
    "How many consonants are there in the English alphabet?", "20", "12", "21", "22", "None", 3],
  [
    "Name the National bird of India?", "Peacock", "Cock", "Sparrow","Kingfisher", "None", 1],
  [
    "Name the national flower of India?", "Lotus", "Rose", "Jasmine","Sunflower", "None", 1],
  [
    "Who designed the National Flag of India?", "Picaso", "Chetan Pandey", "Pingali Venkayya","lionardo de vinci", "None", 3],
  [
    "Name the National river of India?", "Narmada", "Ganges", "Godavari","Kaveri", "None", 2],
  [
    "What is the capital of India?", "Jaipur", "Mumbai", "Delhi","Pune", "None", 3],
  [
    "Name the largest mammal?", "Whale", "Shark", "Blue whale","Dolphin", "None", 3],
  [
    "Name the largest planet of our Solar System?", "Jupiter", "Earth", "Mars","Saturn", "None", 1],
  [
    "Who is the first citizen of India?", "Prime Minister", "Minister", "President","Minister", "None", 3],
  [
    "How many Union Territories are there in India?", "8", "11", "6","9", "None", 1],
  [
    "Name the densest jungle in the world?", "Sahara", "Kaziranga", "African jungles","Amazon", "None", 4],
  [
    "Name the longest river on the Earth?", "Amazon", "Ganges", "Nile","Bori", "None", 3],
  [
    "Name a bird that lays the largest eggs?", "Emu", "Ostrich", "Chicken","Eagle", "None", 2],
  [
    "Name the National Heritage Animal of India?", "Royal Bengal Tiger", "One throne rhino", "Elephant","Dog", "None", 3],
  [
    "Which is the tallest mountain in the world?", "Mt. Fuji", "Mt. Everest", "Kalsubai","Sai Tekdi", "None", 2],
  [
    "Which festival is known as the festival of light?", "Diwali", "Dusherra", "Holi","Bhai-dujh", "None", 1],
  [
    "largest Democratic Country?", "Russia", "India", "china","U.S.A.", "None", 2],
  [
    "Which planet is known for its beautiful rings?", "Earth", "Neptune", "Saturn","Mars", "None", 3],
  [
    "Which gas makes up the majority of Earth's atmosphere?", "Nitrogen", "Oxygen", "Carbon Dioxide","Methane", "None", 1],
]


levels = [100,300,500,700,900,1100,1300,1500,1700,1900,2100,2300,2500,2700,2900,3100,3300,3500,3700,4000,4200,4400]
money = 0
for i in range(0, len(questions)+1):

  question = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(f"\nQuestion {i+1}: {question[0]}")

  print(f"1. {question[1]}          2. {question[2]} ")
  print(f"3. {question[3]}          4. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit: =  " ))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 4):
      money = 1000
    elif(i == 9):
      money = 3200
    elif(i == 14):
      money = 10000
  else:
    print("Wrong answer!")
    break 

print(f"Your take home money is {money}")