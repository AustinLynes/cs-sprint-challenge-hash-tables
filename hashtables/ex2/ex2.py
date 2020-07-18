#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """

    route = []
    # look at each ticket
    c = 1
    for ticket in tickets:
        # if the 
     
        
        # if ticket.source == "NONE":
        #     print('found one')
        #     route.append(ticket.destination)

        if ticket.destination == tickets[c].source:
            route.append(ticket.destination)


        if ticket.destination == "NONE" and len(route) is len(tickets) - 1:
            route.append(ticket.destination)
        
        if c + 1 < len(tickets):
            c += 1

    
        if ticket == tickets[len(tickets)-1] and len(route) is not len(tickets):
                ticket = tickets[0]
                c = 1

        
    print(route)
    return route
