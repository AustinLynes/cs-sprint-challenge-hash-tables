#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def find_next_stop(table, list):
    sorted_arr = []

    for i in range(len(table)):
        if i+1 < len(table):
            if table[i][0] == "NONE":
                sorted_arr.append(table[i][1])

            elif table[i][1] != "NONE":
                table[i], table[i+1] = table[i+1], table[i]

    return sorted_arr


def reconstruct_trip(tickets, length):

    # """
    # YOUR CODE HERE
    # """
    table = {}
    route = [None] * length


    for i in range(length):
        table[i] = (tickets[i].source, tickets[i].destination)

        if table[i][0] == "NONE":
            route[0] = table[i][1]

    # for k, v in table.items():
    i = 1
    r = 0
    print(table)
    while r < length and i < length:
        if route[r-1] != None:
            if route[r-1] == table[i][0]:  
                route[r] = table[i][1]
                i = 0
            else:
                i += 1
                r -= 1

        print(i , r)
        r += 1




            
    print(f"\n{route}")
    return route
    # cur = 0
    # fast = 1

    # def find_next(cur, fast):
    #     _source = table[fast][0]
    #     _dest = table[cur][1]

    #     if _source == _dest:
    #         _dest, _source = _source, _dest
    #         current_ticket = route[cur]
    #         swapped = True
    #     else:
    #         print("recursing")
    #         _source = table[fast + 1][0]
    #         _dest = table[cur + 1][1]
    #         find_next(_source, _dest)

    # for i in range(len(tickets)):
    #     route.append(table[i][1])

    # while cur < len(table) and fast < len(table):

    #     # LOOK FOR BEGINING OF LIST
    #     # once found SWAP with the first index
    #     current_ticket = None

    #     swapped = False

    #     # if the tickets source is NONE
    #     if route[0] != "NONE":
    #         # move it to the front of the list
    #         route[cur], route[0] = route[0], route[cur]
    #         current_ticket = table[cur]
    #         # tell program that swapping has happened
    #         swapped = True
    #         # move the pointers to the right -->

    #     # if the ticket we are looking ats destination is NONE
    #     elif route[length-1] != "NONE":
    #         # move it to the end of the list
    #         swapped = True
    #         route[cur], route[length-1] = route[length-1], route[cur]

    #     else:
    #         find_next(cur, fast)

    #     cur += 1
    #     fast += 1

    #     if cur == len(tickets)-1 and swapped == True:
    #         cur = 0

    #     print(f"\t{route}")
        # return route
