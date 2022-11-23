import random
def random_string():
    random_list=[
          " I am unable to understand, please ask again.","Samjh nahi ayi, dobara type karein!",
          "Sorry, I am unable to understand","Unable to answer, ask me something else.",
          ]
    
    list_count=len(random_list)
    random_item=random.randrange(list_count)
    
    return random_list(random_item)
    
    