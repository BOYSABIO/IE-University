def get_phone(file, client):
    try:
        f = open(file, "r")
    except FileNotFoundError:
        return("The file ", + file + " does not exist")
    else:
        directory = f.readlines() # Where the information will be stored
        f.close()
        directory = dict([tuple(line.split(",")) for line in directory]) 
        if client in directory:
            return directory(client)
        else:
            return("The client", client, "does not exist")

def add_phone(file, client, telf):
    try:
        f = open(file, "a")
    except FileNotFoundError:
        return("The file ", + file + " does not exist")
    else:
        f.write(client + "," + telf + "\n")
        f.close()
        return("The telephone has been added")
    
def remove_phone(file, client):
    try:
        f = open(file, "r")
    except FileNotFoundError:
        return("The file ", + file + " does not exist")
    else:
        directory = f.readlines()
        f.close()
        directory = dict([tuple(line.split(",")) for line in directory])
        if client in directory:
            del directory[client]
            f = open(file, "w")
            for name, telf in directory.items():
                f.write(name + "," + telf)
            f.close()
            return("Client has been removed")
        else:
            return("The client", client, "does not exist")