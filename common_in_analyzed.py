from docopt import docopt

def get_topics(f):
    topics = []
    with open(f, "r") as i:
        for line in i:
            if line.startswith("("):
                topics.append(set(line.replace("(","").replace(")","").replace("\n","").replace("'","").split(", ")[5].split()))
    return topics         

def main():
    args = docopt("""
    Usage:
        xxx.py [options] <analyzed-files> ...

    Options:
        --minimum NUM    Minimum overlap percentage between clusters to count [default: 0.5]
    """)

    files = args["<analyzed-files>"]
    if len(files) < 2:
        raise Exception("Need more than one file")
    minimum = float(args["--minimum"])

    in_all = get_topics(files[0])

    for f in files[1:]:
        to_remove = []
        for assumed_common_topic in in_all:
            any_match = False
            for topic in get_topics(f):
                common = topic.intersection(assumed_common_topic)
                if float(len(common))/len(topic) > minimum:
                    any_match = True
                    break
            if not any_match:
                to_remove.append(assumed_common_topic)
        for bad_topic in to_remove:
            in_all.remove(bad_topic)

    for x in in_all:
        print(x)

    

if __name__ == '__main__':
    main()