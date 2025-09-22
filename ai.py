data = open('l.txt', encoding='UTF-8').read()
from random import randint


w = data.split()
print("All Words: ",len(w))


tokens = [line.split() for line in open("l.txt", encoding="utf-8").read().splitlines()]
print("All Sen..: ",len(tokens))



from gensim.models import Word2Vec



model = Word2Vec(
    sentences=tokens,
    vector_size=100,
    window=5,
    min_count=2,
    workers=4
    )


while True:
    prompt = str(input("Write Your Word/Sent: "))
    deep = int(input("Write number of deep: "))

    if len(prompt.split()) > 1:
        for k in prompt.split():
            try:
                q=(model.wv.most_similar(k))
                print(q)
                print("============deep===========")
                for p in range(deep):
                    n=randint(0,4)
                    q=(model.wv.most_similar(k))
                    print(q[n][0],'',q[n][1])
                    k=q[n][0]
            except:
                print(f"Application can't find anything for {k}!")

    else:
        try:
            q=(model.wv.most_similar(prompt))
            print(q)
            print("============deep===========")
            for p in range(deep):
                n=randint(0,4)
                q=(model.wv.most_similar(prompt))
                print(q[n][0],'',q[n][1])
                prompt=q[n][0]
        except:
            print("Application can't find anything!")
    
