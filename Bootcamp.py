#If statements/ Boolean variables.
def dave_check(user_name):
  if user_name == "Dave":
    return "Get off my computer Dave!"
  if user_name == "angela_catlady_87":
   return "I know it is you Dave! Go away!"
  
# Enter a user name here, make sure to make it a string
user_name = "Dave"

print(dave_check(user_name))
#Rational Operators.
def greater_than(x,y):
  if x > y:
    return(x)
  if y > x:
    return (y)
  if x == y:
    return ("These numbers are the same")

def graduation_reqs(credits):
  if (credits >= 120):
    return("You have enough credits to graduate!")
  if (credits < 120):
    return ("You do not have enough credits to graduate!")
print(graduation_reqs(120))

#Exercise w/ and booleans.
statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)

statement_two = (4 * 2 <= 8) and (7 - 1 == 6)


def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"

#Exercise w/ or booleans.
statement_one = (2 - 1 > 3) or (-5 * 2 == -10)

statement_two = (9 + 5 <= 15) or (7 != 4 + 3)

def graduation_mailer(gpa, credits):
  if gpa >= 2.0 or credits >= 120:
    return(True)

#Exercise w/ not booleans.
statement_one = not(4+5<=9)

statement_two = not(8*2)!=20-4

def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and not (credits >= 120):
    return("You do not have enough credits to graduate.")
  if (credits >= 120) and not (gpa >=2.0):
    return("Your GPA is not high enough to graduate.")
  if not (credits >= 120) and not (gpa >= 2.0):
    return("You do not meet either requirement to graduate!")

print("testing code")

#Else Statements
def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and not (credits >= 120):
    return "You do not have enough credits to graduate."
  if not (gpa >= 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  else:
    return("You do not meet the GPA or the credit requirement for graduation.")

#Elif statements.

def grade_converter(gpa):
  if gpa >= 4.0:
    return ("A")
  elif gpa >= 3.0:
    return ("B")
  elif gpa >= 2.0:
    return ("C")
  elif gpa >= 1.0:
    return ("D")
  else:
    return ("F")
#else statements don't need conditions to be met.
#Review Conditionals.
def applicant_selector(gpa,ps_score,ec_count):
  if (gpa >= 3.0) and (ps_score >= 90) and (ec_count >= 3):
    return("This applicant should be accepted.")
  elif(gpa >= 3.0) and (ps_score >= 90) and not (ec_count >= 3):
    return("This applicant should be given an in-person interview.")
  else:
    return("This applicant should be rejected.")
