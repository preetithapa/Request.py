import requests
import json
url="http://saral.navgurukul.org/api/courses"
html_data=requests.get(url)
data=html_data.json()
with open("q.json","w")as file:
    json.dump(data,file,indent=4)
def nevigation(s,slug,slug_id,data1):
    while True:
        index=slug_id
        choice=input("eneter the choice up,next,back")
        if choice=="up":
            index-=1
            course1=requests.get("http://saral.navgurukul.org/api/courses/"+str(s)+"/exercise/getBySlug?slug="+str(slug[index]))
            inf=course1.json()
            print("content",inf["content"])
            print(index)
        elif choice=="next":  
            index+=1
            course1=requests.get("http://saral.navgurukul.org/api/courses/"+str(s)+"/exercise/getBySlug?slug="+str(slug[index-1]))
            inf=course1.json()
            print("content",inf["content"])
            print(index)
        elif choice=="back" :
              j=1
              for i in data1["data"]:
                print(j,i["name"])
                j+=1
                for child in i["childExercises"]:
                    print("    ",i,child["name"])
                    j+=1            
        else:
            break
def coures(): 
    c=1     
    print("SI.NO","","Name","","ID")
    for i in data["availableCourses"]:
        print(c,"",i["name"],"",i["id"])
        c+=1
    for dic in data["availableCourses"]:
        course_id=int(input("enter any id number"))
        s=data["availableCourses"][course_id-1]["id"]
        course=requests.get("http://saral.navgurukul.org/api/courses/"+str(s)+"/exercises")
        data1=course.json()
        # print(data1)
        slug=[]
        c1=1
        for i in data1["data"]:
            print(c1,i["name"])
            slug.append(i["slug"])
            c1+=1
            c2=1
            for child in i["childExercises"]:
                print("    ",c2,child["name"])
                slug.append(child["slug"])
                c2+=1
        slug_id=int(input("enter content of slug"))
        content_info=requests.get("http://saral.navgurukul.org/api/courses/"+str(s)+"/exercise/getBySlug?slug="+str(slug[slug_id-1]))
        data2=content_info.json()
        print(data2["content"])
        # with open("q1.json","w")as file:
        #     json.dump(data2,file,indent=4)
        nevigation(s,slug,slug_id,data1)
coures()    
