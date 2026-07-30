set_sports_student_list={"Sahil","Rohit","Ankit","Ramesh","Suresh","Ravi","Amit","Vikram","Karan","Arjun"}
set_music_student_list={"Rohit","Ankit","Ramesh","Suresh","Ravi","Amit","Vikram","Karan","Arjun","Rahul"}
print("Students who play both sports and music are:",set_sports_student_list.intersection(set_music_student_list))
print("Students who play either sports or music are:",set_sports_student_list.union(set_music_student_list))
print("Students who play sports but not music are:",set_sports_student_list.difference(set_music_student_list))