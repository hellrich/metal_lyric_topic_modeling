from docopt import docopt
from collections import OrderedDict 

def get_topic_keys(f,examples=10):
    topics2keys = {}
    with open(f, "r") as topics:
        for topic in topics:
            topic = topic.split()
            _id = int(topic[0])
            keys = topic[2:examples+2]
            topics2keys[_id] = keys
    return topics2keys

def get_doc_topics(f):
    albums = 0
    books = 0
    topics2type = OrderedDict()
    with open(f, "r") as docs:
        for doc in docs:
            doc = doc.split()
            _id = doc[0]
            name = doc[1].split("/")[-1:][0].replace(".html.txt","")
            _type = "album" if name.startswith("TYPE_ALBUM") else "book"
            if _type == "album":
                name = name.replace("TYPE_ALBUM","")
                albums += 1
            else:
                books += 1
                name = name.replace("TYPE_BOOK","")
            topics = doc[2:]

            for topic, value in enumerate(topics):
                if not topic in topics2type:
                     topics2type[topic] = {"album":0, "book":0}
                topics2type[topic][_type] += float(value)
    #normalize entries
    for topic in topics2type:
        topics2type[topic]["album"] /= albums
        topics2type[topic]["book"] /= books
    return topics2type

def main():
    args = docopt("""
    Usage:
        xxx.py [options] <doc-topics> <topic-keys>

    Options:
        --minimum NUM    Minimum probability for both book and album to show [default: 0.01]
        --examples NUM      Number of exmaple words to show [default: 10]
    """)

    topics2type = get_doc_topics(args["<doc-topics>"])
    topics2keys = get_topic_keys(args["<topic-keys>"], int(args["--examples"]))
    minimum = float(args["--minimum"])

    print("high in both")
    for topic in topics2type:
        if topics2type[topic]["album"] >= minimum and topics2type[topic]["book"] >= minimum:
            print(topic,"album:",topics2type[topic]["album"],"book:",topics2type[topic]["book"]," ".join(topics2keys[topic]))

    top = []
    for topic in topics2type:
        top.append((topics2type[topic]["book"], topics2type[topic]["album"], str(topic)+" "+" ".join(topics2keys[topic])))
    print("top book")
    for x in sorted(top, key=lambda y: y[0], reverse=True)[:10]:
        print(x[2])
    print("top metal")
    for x in sorted(top, key=lambda y: y[1], reverse=True)[:10]:
        print(x[2])

if __name__ == '__main__':
    main()