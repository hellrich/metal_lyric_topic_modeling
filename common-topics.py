from docopt import docopt
from collections import OrderedDict


def get_topic_keys(f, examples=20):
    topics2keys = {}
    with open(f, "r") as topics:
        for topic in topics:
            topic = topic.split()
            _id = int(topic[0])
            keys = topic[2:examples + 2]
            topics2keys[_id] = keys
    return topics2keys


def get_common(files, minimum):
    in_all = get_topic_keys(files[0]).values()

    for f in files[1:]:
        to_remove = []
        for assumed_common_topic in in_all:
            any_match = False
            for topic in get_topic_keys(f).values():
                common = set(topic).intersection(set(assumed_common_topic))
                if float(len(common)) / len(topic) > minimum:
                    any_match = True
                    break
            if not any_match:
                to_remove.append(assumed_common_topic)
        for bad_topic in to_remove:
            in_all.remove(bad_topic)
    return [(_id, _set) for _id, _set in get_topic_keys(files[0]).items() if _set in in_all]


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

    common = get_common(files, minimum)
    for x in common:
        print(x[0], " ".join(x[1]))


if __name__ == '__main__':
    main()
