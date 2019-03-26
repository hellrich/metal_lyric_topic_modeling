from docopt import docopt
from collections import OrderedDict 
from math import sqrt

def get_doc_topics(f):
    results = []
    with open(f, "r") as docs:
        for doc in docs:
            doc = doc.split()
            _id = doc[0]
            name = doc[1].split("/")[-1:][0].replace(".html.txt","")
            topics = [float(i) for i in doc[2:]]
            results.append((name, topics))
    return results

def get_band_vector(band,doc_topics):
    for b,v in doc_topics:
        if band == b:
            return v
    raise Exception("Band not in corpus")

def similarity(v1, v2):
    s = sum([i1 * i2 for i1, i2 in zip(v1, v2)])
    s /= sqrt(sum([i**2 for i in v1]))
    s /= sqrt(sum([i**2 for i in v2]))
    return s

def main():
    args = docopt("""
    Usage:
        xxx.py [options] <doc-topics> <band>

    Options:
        --bands NUM    Number of close bands to show [default: 10]
    """)

    doc_topics = get_doc_topics(args["<doc-topics>"])
    band=args["<band>"]
    bands = int(args["--bands"])

    vector = get_band_vector(band, doc_topics)

    band_sim = []
    for b,v in doc_topics:
        if b != band:
            band_sim.append((b, similarity(vector,v)))

    for b,v in sorted(band_sim, reverse=True, key=lambda y: y[1])[:bands]:
        print(b,v)
     

if __name__ == '__main__':
    main()