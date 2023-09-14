def wwp2(word):
    temp=''
    count=1
    for i in word:
        if count <len(word):
            temp+=i
        else:
            temp+=str(int(i)+2)
        count+=1
    return temp

def gotourl(url):
    url_split=url.split('!')
    urllist=[[None,None,None,None,None,
             None,None,None,None,None,
             None,None,None,],
             [None,None,None,None,None,
             None,None,None,None,None,
             None,None,None,]]
    urllist[0][10]=[3,4,5,6,7,8,10,11,9]
    urllist[1][10]=[3,4]
    urllist[0][8]=[1,2,3,4,5,6,8,9,7]
    urllist[1][8]=[1,2]
    urllist[0][12]=[1,2,3,4,5,6,7,8,9,12,13,10,11]
    urllist[1][12]=[1,5]
    urlsplit_no=len(url_split)
    url_split.append('9m1')
    url_split.append('1b1')
    #print(url_split)
    head=url_split[0]
    for i in urllist[0][urlsplit_no]:
        if i ==urllist[1][urlsplit_no][0] or i==urllist[1][urlsplit_no][1]:
            head=head+'!'+wwp2(url_split[i])
        else:
            head=head+'!'+url_split[i]
    #print(urllist[0][urlsplit_no])
    #print(urllist[1][urlsplit_no][0])
    #print(urllist[1][urlsplit_no][1])
    return head
#call: gotourl('https://...!..!..!')
#return: 'https://...!..!..!'