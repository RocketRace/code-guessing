def entry(h,n):import re;r="|".join((i*".").join([f"({n[0]})",*n[1:]])for i in range(len(h)));s=re.search(r,h);return s and(s.start(),s.groups().index(n[0]))#nested loop is shorter
#like and comment below with your favorite esolang                                                                                                           #long live regis regex
#dont' forget to ring that [shuffle] button!
