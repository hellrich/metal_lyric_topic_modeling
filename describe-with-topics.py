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

def get_band_vector(band,doc_topics,allowed_topics):
    for b,vector in doc_topics:
        if band == b:
            return [(topic, value) for topic, value in enumerate(vector) if topic in allowed_topics]
    raise Exception("Band not in corpus")

def main():
    args = docopt("""
    Usage:
        xxx.py [options] <doc-topics> <band>

    Options:
        --minimum NUM    Mimimum value of topics to show [default: 0.1]
    """)

    doc_topics = get_doc_topics(args["<doc-topics>"])
    band=args["<band>"]
    minimum=float(args["--minimum"])

    allowed_topics = [4,8,9,38,31,13,22,29,45,39,46,34,48,40,36,16]
    vector = get_band_vector(band, doc_topics, allowed_topics)
    above_vector = [(topic, value) for topic, value in vector if value > minimum]
    for topic,value in sorted(above_vector, key=lambda x: x[1], reverse=True):
        print(topic,value)

if __name__ == '__main__':
    main()