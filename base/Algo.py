import random
from .models import QuizQuestion, Job

def algo(current_quiz_questions,rating):
     factors_values=[{"Artistic_fact":0},
                {"Conventional_fact":0},
                {"Enterprising_fact":0},
                {"Social_fact":0},
                {"Investigative_fact":0},
                {"Realistic_fact":0}
               ]
     Artistic_fact=0
     Conventional_fact=0
     Enterprising_fact=0
     Investigative_fact=0
     Realistic_fact=0
     Social_fact=0
     for question in current_quiz_questions:
        print(question["Question"]+':')
        pop_element=rating.pop(0)
        choice=pop_element
        choice=int(choice)
        print(question["primaryfact"])
        match question["primaryfact"]:
            case 'a':

                match choice:

                    case 5:
                        Artistic_fact+=5
                        Conventional_fact+=.10
                        Enterprising_fact+=.10
                        Investigative_fact+=.10
                        Realistic_fact+=.10
                        Social_fact+=.10
                    case 4:
                        Artistic_fact+=2.5
                        Conventional_fact+=.10
                        Enterprising_fact+=.10
                        Investigative_fact+=.10
                        Realistic_fact+=.10
                        Social_fact+=.10
                    case 3:
                        Artistic_fact+=0.5
                        Conventional_fact+=.10
                        Enterprising_fact+=.10
                        Investigative_fact+=.10
                        Realistic_fact+=.10
                        Social_fact+=.10
                    case 2:
                        Artistic_fact+=0.10
                        Conventional_fact+=.10
                        Enterprising_fact+=.10
                        Investigative_fact+=.10
                        Realistic_fact+=.10
                        Social_fact+=.10
                    case 1:
                        Artistic_fact+=0
                        Conventional_fact+=.10
                        Enterprising_fact+=.10
                        Investigative_fact+=.10
                        Realistic_fact+=.10
                        Social_fact+=.10

            case 'c':

                match choice:

                    case 5:
                        Artistic_fact+=.10
                        Conventional_fact+=5
                        Enterprising_fact+=.10
                        Investigative_fact+=.10
                        Realistic_fact+=.10
                        Social_fact+=.10
                    case 4:
                        Artistic_fact+=.10
                        Conventional_fact+=2.5
                        Enterprising_fact+=.10
                        Investigative_fact+=.10
                        Realistic_fact+=.10
                        Social_fact+=.10
                    case 3:
                        Artistic_fact+=0.10
                        Conventional_fact+=.5
                        Enterprising_fact+=.10
                        Investigative_fact+=.10
                        Realistic_fact+=.10
                        Social_fact+=.10
                    case 2:
                        Artistic_fact+=0.10
                        Conventional_fact+=.10
                        Enterprising_fact+=.10
                        Investigative_fact+=.10
                        Realistic_fact+=.10
                        Social_fact+=.10
                    case 1:
                        Artistic_fact+=0.10
                        Conventional_fact+=0
                        Enterprising_fact+=.10
                        Investigative_fact+=.10
                        Realistic_fact+=.10
                        Social_fact+=.10

            case 'e':

                match choice:

                    case 5:
                        Artistic_fact+=.10
                        Conventional_fact+=.10
                        Enterprising_fact+=5
                        Investigative_fact+=.10
                        Realistic_fact+=.10
                        Social_fact+=.10
                    case 4:
                        Artistic_fact+=.10
                        Conventional_fact+=.10
                        Enterprising_fact+=2.5
                        Investigative_fact+=.10
                        Realistic_fact+=.10
                        Social_fact+=.10
                    case 3:
                        Artistic_fact+=0.10
                        Conventional_fact+=.10
                        Enterprising_fact+=.5
                        Investigative_fact+=.10
                        Realistic_fact+=.10
                        Social_fact+=.10
                    case 2:
                        Artistic_fact+=0.10
                        Conventional_fact+=.10
                        Enterprising_fact+=.10
                        Investigative_fact+=.10
                        Realistic_fact+=.10
                        Social_fact+=.10
                    case 1:
                        Artistic_fact+=0.10
                        Conventional_fact+=.10
                        Enterprising_fact+=0
                        Investigative_fact+=.10
                        Realistic_fact+=.10
                        Social_fact+=.10

            case 'i':

                match choice:

                    case 5:
                        Artistic_fact+=.10
                        Conventional_fact+=.10
                        Enterprising_fact+=.10
                        Investigative_fact+=5
                        Realistic_fact+=.10
                        Social_fact+=.10
                    case 4:
                        Artistic_fact+=.10
                        Conventional_fact+=.10
                        Enterprising_fact+=.10
                        Investigative_fact+=2.5
                        Realistic_fact+=.10
                        Social_fact+=.10
                    case 3:
                        Artistic_fact+=0.10
                        Conventional_fact+=.10
                        Enterprising_fact+=.10
                        Investigative_fact+=.5
                        Realistic_fact+=.10
                        Social_fact+=.10
                    case 2:
                        Artistic_fact+=0.10
                        Conventional_fact+=.10
                        Enterprising_fact+=.10
                        Investigative_fact+=.10
                        Realistic_fact+=.10
                        Social_fact+=.10
                    case 1:
                        Artistic_fact+=0.10
                        Conventional_fact+=.10
                        Enterprising_fact+=.10
                        Investigative_fact+=0
                        Realistic_fact+=.10
                        Social_fact+=.10

            case 'r':

                match choice:

                    case 5:
                        Artistic_fact+=.10
                        Conventional_fact+=.10
                        Enterprising_fact+=.10
                        Investigative_fact+=.10
                        Realistic_fact+=5
                        Social_fact+=.10
                    case 4:
                        Artistic_fact+=.10
                        Conventional_fact+=.10
                        Enterprising_fact+=.10
                        Investigative_fact+=.10
                        Realistic_fact+=2.5
                        Social_fact+=.10
                    case 3:
                        Artistic_fact+=0.10
                        Conventional_fact+=.10
                        Enterprising_fact+=.10
                        Investigative_fact+=.10
                        Realistic_fact+=.5
                        Social_fact+=.10
                    case 2:
                        Artistic_fact+=0.10
                        Conventional_fact+=.10
                        Enterprising_fact+=.10
                        Investigative_fact+=.10
                        Realistic_fact+=.10
                        Social_fact+=.10
                    case 1:
                        Artistic_fact+=0.10
                        Conventional_fact+=.10
                        Enterprising_fact+=.10
                        Investigative_fact+=.10
                        Realistic_fact+=0
                        Social_fact+=.10

            case 's':

                match choice:
                    case 5:
                        Artistic_fact+=.10
                        Conventional_fact+=.10
                        Enterprising_fact+=.10
                        Investigative_fact+=.10
                        Realistic_fact+=.10
                        Social_fact+=5
                    case 4:
                        Artistic_fact+=.10
                        Conventional_fact+=.10
                        Enterprising_fact+=.10
                        Investigative_fact+=.10
                        Realistic_fact+=.10
                        Social_fact+=2.5
                    case 3:
                        Artistic_fact+=0.10
                        Conventional_fact+=.10
                        Enterprising_fact+=.10
                        Investigative_fact+=.10
                        Realistic_fact+=.10
                        Social_fact+=.5
                    case 2:
                        Artistic_fact+=0.10
                        Conventional_fact+=.10
                        Enterprising_fact+=.10
                        Investigative_fact+=.10
                        Realistic_fact+=.10
                        Social_fact+=.10
                    case 1:
                        Artistic_fact+=0.10
                        Conventional_fact+=.10
                        Enterprising_fact+=.10
                        Investigative_fact+=.10
                        Realistic_fact+=.10
                        Social_fact+=0
   
     factors_values[0]["Artistic_fact"]=Artistic_fact
     
     factors_values[1]["Conventional_fact"]=Conventional_fact
     
     factors_values[2]["Enterprising_fact"]=Enterprising_fact
     
     factors_values[3]["Social_fact"]=Social_fact
     
     factors_values[4]["Investigative_fact"]=Investigative_fact
     
     factors_values[5]["Realistic_fact"]=Realistic_fact
     for i in range(6):
         for j in range(6):
             if(list(factors_values[i].values())[0]>=list(factors_values[j].values())[0]):
                 temp=factors_values[i]
                 factors_values[i]=factors_values[j]
                 factors_values[j]=temp
                 
     
     
     threelettercode=[]
     joblist=[]
     suggested_job=[]
     
     threelettercode.append((str(list(factors_values[0].keys())))[2])
     threelettercode.append((str(list(factors_values[1].keys())))[2])
     threelettercode.append((str(list(factors_values[2].keys())))[2])
    
     job_objects=Job.objects.all()
     for job in job_objects:
         data={
             'Interest Code':job.interest_code,
             'Occupation':job.occupation
         }
         joblist.append(data)  
     match threelettercode[0]:
         case 'S':
             for i in joblist:
                 if (threelettercode[0] and threelettercode[1] and threelettercode[2]) in i["Interest Code"]:
                     suggested_job.append(i["Occupation"])
         case 'E':
             for i in joblist:
                 if (threelettercode[0] and threelettercode[1] and threelettercode[2]) in i["Interest Code"]:
                     suggested_job.append(i["Occupation"])
         case 'A': 
              for i in joblist:
                  if (threelettercode[0] and threelettercode[1] and threelettercode[2]) in i["Interest Code"]:
                      suggested_job.append(i["Occupation"])
         case 'C': 
              for i in joblist:
                  if (threelettercode[0] and threelettercode[1] and threelettercode[2]) in i["Interest Code"]:
                      suggested_job.append(i["Occupation"])
         case 'I': 
              for i in joblist:
                  if (threelettercode[0] and threelettercode[1] and threelettercode[2]) in i["Interest Code"]:
                      suggested_job.append(i["Occupation"])
         case 'R': 
              for i in joblist:
                  if (threelettercode[0] and threelettercode[1] and threelettercode[2]) in i["Interest Code"]:
                      suggested_job.append(i["Occupation"])
        
                  #like this for other cases
     
     five_suggestions=[]
     
     for i in range(5):
         job=random.choice(suggested_job)
         five_suggestions.append(job)
     
     
     
     return five_suggestions
          
     



      
