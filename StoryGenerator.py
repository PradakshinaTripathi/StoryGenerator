import random
when = ['Once upon a time','A year ago','Long Long ago','Today','Yesterday','A decade ago','On a beautiful day of July']
who = ['a merchant', 'a farmer', 'a tiger','a mother','a hero','a man','a girl','a boy']
name = ['Suresh','Ram','Satya','Combo','Shriya','Mikha']
where = ['India','kingdom','Spain','Jungle','village']
did = ['struggled hard to earn','used to eat sandwiches','was fond of cooking food','walked miles and miles in search of food','enjoyed the job']
def story():
    print("--- Your Story ---")
    print(random.choice(when)+", " + "there was "+ random.choice(who)+" named "+random.choice(name) +" who lived in " + random.choice(where)+" and "+random.choice(did)+".")
story()

while True:
   answer = input('Do you want to continue?:')
   if answer.lower().startswith("y"):
      story()
   elif answer.lower().startswith("n"):
      print("ok, see you soon!")
      exit()




