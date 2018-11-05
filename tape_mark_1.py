#!/usr/bin/env python

import random
import sys
 
versi = \
[[" l accecante   /  globo  /  di fuoco  ", "1/4", "2/3", "1"],\
[" si espande   /  rapidamente  ", "1/2", "3/4", "1"],\
[" trenta volte  / piu luminoso  / del sole ", "2/3", "2/4", "1"],\
[" quando  raggiunge / la stratosfera  ", "3/4", "1/2", "1"],\
[" la  sommita  /  della nuvola ", "1/3", "2/3", "1"],\
[" assume   / la ben nota forma  / di fungo ", "2/4", "3/4", "1"], \

[" la testa / premuta  / sulla spalla  ", "1/4", "2/4", "2"],\
[" i  capelli   /  tra le labbra ", "1/4", "2/4", "2"],\
[" giacquero  /   immobili / senza parlare ", "2/3", "2/3", "2"],\
[" finche non mosse  /  le dita  / lentamente    ", "3/4", "1/3", "2"],\
[" cercando / di afferrare  ", "3/4", "1/2", "2"],\

[" mentre la moltitudine  /  delle cose  /   accade   ", "1/2", "1/2", "3"],\
[" io contemplo  /  il loro ritorno    ", "2/3", "3/4", "3"],\
[" malgrado / che le cose  /  fioriscano    ", "1/2", "2/3", "3"],\
[" esse tornano  / tutte    / alla loro radice   ", "2/3", "1/4", "3"]]

#~ gruppo "1", 0-5: Diario di Hiroshima, di Michihito Hachiya
#~ gruppo "2", 6-10: Il Mistero dell'ascensore, di Paul Goldwin
#~ gruppo "3", 11-14: Tao te King, di Lao Tse

random.shuffle(versi)
strofa_uno = [None] * 10
strofa_uno[0] = versi[0]
versi.remove(strofa_uno[0])


try:
    i = 0 ; j = 0
    while j < 9:
        if (versi[i][1][0] == strofa_uno[j][2][0] \
        or versi[i][1][2] == strofa_uno[j][2][0] \
        or versi[i][1][2] == strofa_uno[j][2][2]) \
        and versi[i][3] != strofa_uno[j][3]:
            # se le strofe "stanno bene insieme"
            # e non appartengono allo stesso gruppo
            strofa_uno[j+1] = versi[i]
            versi.remove(versi[i])
            i = 0
            j += 1
        # altrimenti, esamina l'elemento successivo
        else:
            i += 1
            continue

# se la combinazione in esame non soddisfa le condizioni, viene scartata
except: sys.exit()


strofa = []
for k in xrange(len(strofa_uno)):
	strofa.append(strofa_uno[k][0])

s = '/'.join(strofa).split("/")

print ""

for k in xrange(len(s)):
	
	if k == (len(s) - 1): sys.stdout.write(s[k].upper())
	else: sys.stdout.write(s[k].upper())

    # senza la seguente istruzione l'output di una strofa
    # viene formattato come nel tabulato originale, senza 'a capo'
    
	# if k > 0 and (k+1)%4 == 0: print ""
	
print ""


#~ ---------------------------------------------------------------------
#~ Tape Mark I

#~ La testa premuta sulla spalla, trenta volte
#~ piu' luminoso del sole, io contemplo il loro ritorno
#~ finche' non mosse le dita lentamente e, mentre la moltitudine
#~ delle cose accade, alla sommita' della nuvola
#~ esse tornano tutte, alla loro radice, e assumono
#~ la ben nota forma di fungo cercando di afferrare.
#~ 
#~ I capelli tra le labbra, esse tornano tutte
#~ alla loro radice, nell'accecante globo di fuoco
#~ io contemplo il loro ritorno, finche' non muove le dita
#~ lentamente, e malgrado che le cose fioriscano
#~ assume la ben nota forma di fungo, cercando
#~ di afferrare mentre la moltitudine delle cose accade.
#~ 
#~ Nell'accecante globo di fuoco io contemplo
#~ il loro ritorno quando raggiunge la stratosfera mentre la moltitudine
#~ delle cose accade, la testa premuta
#~ sulla spalla: trenta volte piu' luminose del sole
#~ esse tornano tutte alla loro radice, i capelli
#~ tra le labbra assumono la ben nota forma di fungo.
#~ 
#~ Giacquero immobili senza parlare, trenta volte
#~ piu' luminosi del sole essi tornano tutti
#~ alla loro radice, la testa premuta sulla spalla
#~ assumono la ben nota forma di fungo cercando
#~ di afferrare, e malgrado che le cose fioriscano
#~ si espandono rapidamente, i capelli tra le labbra.
#~ 
#~ Mentre la moltitudine delle cose accade nell'accecante
#~ globo di fuoco, esse tornano tutte
#~ alla loro radice, si espandono rapidamente, finche' non mosse
#~ le dita lentamente quando raggiunse la stratosfera
#~ e giacque immobile senza parlare, trenta volte
#~ piu' luminoso del sole, cercando dibetter white afferrare.
#~ 
#~ Io contemplo il loro ritorno, finche' non mosse le dita
#~ lentamente nell'accecante globo di fuoco:
#~ esse tornano tutte alla loro radice, i capelli
#~ tra le labbra e trenta volte piu' luminosi del sole
#~ giacquero immobili senza parlare, si espandono
#~ rapidamente cercando di afferrare la sommita'.
