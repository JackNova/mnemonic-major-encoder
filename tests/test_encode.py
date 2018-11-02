from mnemonic_major_encoder import encoder
import pytest

EXAMPLES = [
    ("ciao mondo!", "6 321!"),
    ("il Signore è mia luce e mia salvezza...", "5 024  3 56  3 0580..."),
    ("Il mattino ha\nl'oro in bocca", "5 312 \n5'4 2 97"),
    ("Jack", "67")
]
TEST_INPUT_PATH = 'tests/fixtures/brodo_caldo_per_lanima'
TEST_OUTPUT_PATH = 'tests/fixtures/brodo_caldo_per_lanima_converted'

BOOK = """Ho un amico di nome Monty Robers che possiede una tenuta con allevamento di cavalli a San Ysidro. Mi lascia usare la sua casa per organizzare manifestazioni volte a raccogliere fondi per programmi a favore dei giovani a rischio.
L'ultima volta che ero lì mi presentò dicendo: "Voglio spiegarvi perché lascio che Jack usi la mia casa".
Tutto risale alla storia di un giovane che era figlio di un addestratore di cavalli itinerante, il quale andava di scuderia in scuderia, di pista in pista, di fattoria in fattoria e di allevamento in allevamento per addestrare i cavalli. Di conseguenza la frequenza scolastica del ragazzo alle superiori veniva continuamente interrotta. Quando fu all'ultimo anno, gli fu assegnato un compito su cosa volesse fare da grande.
Quella sera scrisse un tema di sette pagine descrivendo il suo obiettivo di possedere un giorno un allevamento di cavalli.
Descrisse con dovizia di particolari il suo sogno e addirittura disegnò lo schema di una tenuta di ottanta ettari, indicando l'ubicazione di tutti gli edifici, delle scuderie e della pista. Poi disegnò la pianta dettagliata di una casa di quattrocento metri quadri da inserire nella tenuta di sogno di ottanta ettari.
Elaborò con passione il progetto e il giorno successivo lo consegnò all'insegnante. Due giorni dopo il compito gli fu riconsegnato. Sulla prima pagina vi era in rosso una insufficienza con un appunto che diceva: "Vieni da me dopo la lezione".
Il ragazzo che aveva un sogno andò dall'insegnante dopo la lezione e domandò: "Perché ho preso un' insufficienza?".
L'insegnante rispose: "È un sogno troppo irrealistico per un ragazzo come te. Non hai soldi. Provieni da una famiglia itinerante.
Non hai risorse. Possedere un allevamento di cavalli richiede un sacco di soldi. Devi acquistare il terreno. Devi pagare le fattrici e poi spendere molti soldi per gli stalloni. Non hai nessuna possibilità di farcela".
Poi l'insegnante aggiunse: "Se riscrivi il compito con un obiettivo più realistico, rivedrò il tuo voto".
Il ragazzo andò a casa e ci pensò su a lungo. Domandò a suo padre cosa fare. Il padre rispose: "Guarda, figliolo, devi decidere da solo. Tuttavia penso che sia una decisione importante per te".
Infine, dopo una settimana di riflessione, il ragazzo riconsegnò lo stesso compito, senza alcun cambiamento, dichiarando: "Può tenersi l'insufficienza, io mi terrò il mio sogno".
Monty si rivolse poi al gruppo riunito e disse: "Vi racconto questa storia perché voi vi trovate nella mia casa di quattrocento metri quadri in mezzo alla mia tenuta di ottanta ettari. Ho ancora quel compito di scuola incorniciato sopra il caminetto".
Aggiunse: "La parte più bella della storia è che due estati fa, quello stesso insegnante portò trenta ragazzi in campeggio nella mia tenuta per una settimana. Nell'andarsene, l'insegnante mi disse: "Vedi, Monty, adesso posso dirtelo. Quando ero il tuo insegnante ero una specie di ladro di sogni. In quegli anni ho rubato molti sogni ai ragazzi. Fortunatamente tu hai avuto abbastanza coraggio da seguire il tuo".
Non lasciate che vi rubino i sogni. Ascoltate il vostro cuore, accada quel che accada.
"""

ENCODED_BOOK = """ 2 37 1 23 321 4940 7 901 2 121 72 58321 1 785  02 014. 3 50 04 5 0 70 94 47204 3280102 851  4754 821 94 94743  884 1 682  407.
5'513 851 7 4 5 3 94021 1621: "85 09748 947 50 7 67 0 5 3 70".
11 405 5 014 1 2 682 7 4 85 1 2 101414 1 785 12421, 5 75 218 1 0714 2 0714, 1 901 2 901, 1 814 2 814  1 58321 2 58321 94 10144  785. 1 720720 5 84720 075017 15 470 5 0944 828 7212321 2141. 721 8 5'513 2, 5 8 021 2 7391 0 70 850 84 1 7421.
75 04 0740 2 13 1 01 962 1074821 5 0 918 1 9014 2 642 2 58321 1 785.
10740 72 180 1 941754 5 0 02  1414 102 5 073 1 2 121 1 121 14, 21721 5'9702 1 11 5 186, 15 0714  15 901. 9 102 5 921 1151 1 2 70 1 714621 314 714 1 2044 25 121 1 02 1 121 14.
594 72 902 5 9461  5 642 0608 5 7202 5'20221. 1 642 19 5 7391 5 8 472021. 05 943 962 8 4 2 40 2 208620 72 2 921 7 168: "82 1 3 19 5 502".
5 470 7 88 2 02 21 15'20221 19 5 502  1321: "947  940 2' 208620?".
5'20221 4090: " 2 02 149 45017 94 2 470 73 1. 22  051. 9482 1 2 835 12421.
22  4040. 9014 2 58321 1 785 471 2 07 1 051. 18 7014 5 142. 18 974 5 8146  9 09214 351 051 94 5 0152. 22  202 90951 1 8465".
9 5'20221 620: "0 40748 5 7391 72 2 918 9 45017, 4814 5 1 81".
5 470 21  70  6 920 0  527. 1321  0 914 70 84. 5 914 4090: "741, 855, 18 1614 1 05. 118 920 7 0 2 1602 394121 94 1".
282, 19 2 0132 1 48502, 5 470 47202 5 010 7391, 020 572 739321, 17421: "9 1240 5'208620,  3 14 5 3 02".
321 0 4850 9 5 749 421  10: "8 4721 701 014 947 8 8 1481 25 3 70 1 714621 314 714 2 30 5 3 121 1 121 14.  274 75 7391 1 075 274261 094 5 7321".
620: "5 941 9 95 15 014  7 1 011 8, 75 010 20221 941 1421 470 2 7396 25 3 121 94 2 0132. 25'21402, 5'20221 3 10: "81, 321, 10 90 1415. 721 4 5 1 20221 4 2 096 1 514 1 02. 2 75 2  491 351 02  470. 84121321 1  81 90120 746 1 074 5 1".
22 501 7 8 492  02. 07511 5 8014 74, 71 75 7 71.
"""

def test_encode():
    for text, expected in EXAMPLES:
        assert encoder.encode(text) == expected

def test_encode_book():
    assert encoder.encode(BOOK) == ENCODED_BOOK
