# अगर डेवलपमेंट फील्ड मे आना चाहते हो और समझ नहीं आ रहा है की कैसे क्या करू को तो मुझे कान्टैक्ट कर सकते हो heykyakaru@gmail.com पर और मैं कोसिस करूंगा सही गाइड करने की। क्योंकी बिना सही गाइड के कई बार हम काफी परेसान हो जाते हैं की क्या करे और कैसे करे और इससी चक्कर मे काफी समय और पैसे की बर्बादी कर देते हैं। इसके बाद काफी मानसिक तनाव का भी सामना करना पड़ता हैं तो इसी परेसानी को कम करने का छोटा सा प्रयास हैं। 

# साथ ही अपने ज्ञान को आपके साथ बांटने के लिए यूट्यूब चैनल शुरू किया हूँ और आपके साहियोग की जरूरत है इसे सही और जरूरत मंद स्टूडेंट्स और जो खुद से पढ़ पढ़ना चाहते हैं उन तक पहुचाने के लिए तो इस चैनल को उनके साथ जरूर शेयर करो जो वाकई मे पढ़ना चाहते है और खुद से कोसिस कर रहे हैं। 
# https://www.youtube.com/channel/UCphs2JfmIClR62wbyf76HDg

# HEY KYA KARU यूट्यूब चैनल के जरूरी लिंक 
# 1. Python Basic and Advance ट्यूटोरियल प्लेलिस्ट https://www.youtube.com/playlist?list=PLK6wiPavf7QikS9PMYrGZXz1HlE1KZLD3
# 2. PHP Projects प्लेलिस्ट https://www.youtube.com/playlist?list=PLK6wiPavf7QiEj6IPc3lkjz1wR4w9RM6B
# 3. GitHubट्यूटोरियल प्लेलिस्ट  https://www.youtube.com/watch?v=LUyVs2MTlTM&list=PLK6wiPavf7Qjydpc5v-hdIoqCx2V19pHP
# 4. Python Project https://www.youtube.com/watch?v=3lrbbB38zpU&list=PLK6wiPavf7Qj-NLJhbkxw9QfonweHafcN
# 5. Tips and Trick for Development: https://www.youtube.com/watch?v=vPL6ODrfcwI&list=PLK6wiPavf7QiVLYXrC2TW_fdcZp57MgMB


# set: set unindex form values

a = {3,4,5,6,7,8,97,7}
b = {4,4,3,3,32,3,4,5,6}

print('a: ',a)

# add()
a.add(8787)
print('a.add(8787): ',a)

# update()
a.update([37737,3434,3434])
print('a: ',a)

# len()
print('len: ',len(a))

# remove
# a.remove(37737)
# a.remove(37737)

a.discard(37737)
a.discard(37737)

# pop()
a.pop()

# clear
a.clear()

# del

print('final a: ',a)

print('\nb: ',b)
c = {34,343,4,5,5,4,5,484}
print('c: ',c)


uniq = b.union(c)
print('uniq: ',uniq)

common = b.intersection(c)
print('common: ',common)

diff = b.difference(c)
print('diff: ',diff)

b.intersection_update(c)
print('inter update: ',b)

b.difference_update(c)
print('diffupdate: ',b)

print('isdis: ',c.isdisjoint(b))

print('c.issubset(b): ',c.issubset(b))
b = {3,4,5,6,9}
c = {3,4,5,6,9,4,4555,6677,55}
print('c.issuperset(b): ',c.issuperset(b))


