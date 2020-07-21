# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    dump = []
    filtered = []
    _filtered = False

    # looking through
    result = []
    # print(len(queries))

    for i in range(len(queries)):
        if queries[i].__contains__("nofile"):
            filtered.append(queries[i])
            _filtered = True

    print(f"filtered {filtered}")
    
    for i in range(len(files)):
        t = files[i].split("/")
        dump.append(t[len(t)-1])
    
    for i in range(len(queries)):
        if queries[i] == dump[i]:
            result.append(files[i])
    
    print(result)
    return result


if __name__ == "__main__":
    files = []

    for i in range(500000):
        files.append(f"/dir{i}/file{i}")

    for i in range(500000):
        files.append(f"/dir{i}/dirb{i}/file{i}")

    queries = []

    for i in range(1000000):
        queries.append(f"nofile{i}")

    queries += [
        "file3490",
        "file256",
        "file999999",
        "file8192"
    ]

    result = finder(files, queries)
    print(result)
