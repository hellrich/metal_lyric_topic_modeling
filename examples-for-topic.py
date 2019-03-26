from docopt import docopt
from collections import OrderedDict

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

def harmonic_mean(a,b):
    return (2 * a * b) / (a+b)

def main():
    args = docopt("""
    Usage:
        xxx.py [options] <doc-topics> <topic>

    Options:
        --format  Other formatting [default: False]
        --bonusTopic TOPIC  Second topic
    """)

    formated = args["--format"]

    docs_and_topics = get_doc_topics(args["<doc-topics>"])
    topic = int(args["<topic>"])
    bonusTopic = int(args["--bonusTopic"]) if args["--bonusTopic"] else False

    if formated:
        if not bonusTopic:
            print(" ".join([x[0] for x in sorted(docs_and_topics, key=lambda y: y[1][topic], reverse=True)[:5]]))
    else:
        if not bonusTopic:
            for x in sorted(docs_and_topics, key=lambda y: y[1][topic], reverse=True)[:50]:
                print(x[0] + " " + str(x[1][topic]))
        else:
            for x in sorted(docs_and_topics, key=lambda y: harmonic_mean(y[1][topic],y[1][bonusTopic]), reverse=True)[:50]:
                print(x[0] + " " + str(x[1][topic])+" "+ str(x[1][bonusTopic]))

if __name__ == '__main__':
    main()