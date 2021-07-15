#1  Below are two lists convert it into a dictionary. (using a python
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

Keys_values={'Ten':10, 'Twenty':20, 'Thirty':30,}
print(Keys_values)



#2 Access the value of key ‘history’ from the dictionary below¶
sampleDict = {"class": {
               	 "student" : {
                   		 "name":"Mike",
                   		 "marks":{
                       			 "physics":70,
                      			  "history":80  } 
                            	}
                       	 }
             }

print(sampleDict['class']['student']['marks']['history'])
 
#3. Using the dictionary above, add a key value pair (of your choice) to the student dictionary
sampleDict['class']['student']['marks']['Biology']=60

print(sampleDict)




#4  Reverse this list
numbers = [100, 200, 300, 400, 500]
numbers = numbers[::-1]
print(numbers)


#5.  Return a new set of identical items from set1 $ set2
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.intersection(set2))


#6. Check if these two sets have any elements in common. If yes, display the common elements.
set1 = {10, 20, 30, 40, 50}
set3 = {60, 70, 80, 90, 10}
print(set1.union(set3))


#7. Correct this sentence
sentence = "One year has {} months, {} weeks and {} days.".format(52, 365, 12)
correct_sentence="One year has {} months, {} weeks and {} days.".format(12,52,365)
print(correct_sentence)

#8. What is the cube root of 8?

a = 8
b=a**(1/3)
print(b)


#9. Convert this sentence below to a proper sentence case
"""Hello from the Other side I must've called a thousand times To tell you I'm sorry for
EVERYTHING that I've done But when I call, You never seem to be Home"""


letter="Hello from the Other side I must've called a thousand times To tell you I'm sorry for EVERYTHING that I've done But when I call, You never seem to be Home".title()
print(letter)



