sub = "QWITJSYHXCNDFERMUKGOPVALBZ"
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

sentence = r'Hjkjpmre Djykqet qkrgj, axoh q ykqvj qet goqojdb qxk, qet wkrpyho fj ohj wjjodj skrf q ydqgg iqgj xe ahxih xo aqg jeidrgjt. Xo aqg q wjqpoxspd giqkqwqjpg, qet, qo ohqo oxfj, penerae or eqopkqdxgog—rs irpkgj q ykjqo mkxzj xe q gixjeoxsxi mrxeo rs vxja. Ohjkj ajkj oar krpet wdqin gmrog ejqk rej jlokjfxob rs ohj wqin, qet q drey rej ejqk ohj rohjk. Ohj giqdjg ajkj jlijjtxeydb hqkt qet ydrggb, axoh qdd ohj qmmjqkqeij rs wpkexghjt yrdt. Ohj ajxyho rs ohj xegjio aqg vjkb kjfqknqwdj, qet, oqnxey qdd ohxeyg xeor iregxtjkqoxre, X irpdt hqktdb wdqfj Cpmxojk srk hxg rmxexre kjgmjioxey xo.'

flag = 'Ohj sdqy xg: pgowOYA{AS3CK3DOU_4774OQ5_4S3_O001_6B0659AH}'

fixsent = ''
fixflag = ''
#print(len(sub))
#print(len(alpha))


for word in sentence.upper():
    if not word.isalpha():
        fixsent += word
        continue
    for i, each in enumerate(sub):
        if word == each:
            fixsent += alpha[i]
            continue

for word in flag.upper():
    if not word.isalpha():
        fixsent += word
        continue
    for i, each in enumerate(sub):
        if word == each:
            fixsent += alpha[i]
            continue

print(fixflag)
print('\n')
print(fixsent)