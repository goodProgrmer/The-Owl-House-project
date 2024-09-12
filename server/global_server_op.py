import protocols_answer.login_protocol_op
import protocols_answer.game_protocol_op
import socket
import select
from collections import deque
import time
import threading
from protocols_answer.sendingOperations import*
from Crypto.PublicKey import RSA

def OnConect(username,sock,IP):
    """called when new socket conect to the server.
    :param username: the username of the user of the socket. NOTE: each socket must have unique username, if this user haven't loged in, the username must be generated beffore calling this fanction.
                     in this server, I use numbers to unloged in usernames.
    :param sock: the conected socket
    :param IP: users IP address. NOTE: it assume that each conected user use another IP address.
    :type username: string
    :type sock: socket.socket"""
    global sock_username
    global sock_q_dict

    signed_in_usernames[username]= True
    #other praparations
    sock_username[sock]=username
    protocols_answer.game_protocol_op.OnConect(username,sock,IP)
    protocols_answer.login_protocol_op.OnConect(sock,IP)
    #?/! maseges
    
    t= threading.Thread(target= lambda: presence_check(sock))
    t.start()
    

def GExit(sock):
    """called when the given socket exit the game
    :param sock: the socket that exited the game
    :param del_conect_info: does it need to the information that presence_check use for intarnet conection check
        (if it will not be restored, the this function will asume that the user exited the game itself)
    :type sock: socket.socket"""
    global sock_username
    global anlogined_userNames
    user= sock_username[sock]
    print(user, "exited the game")
    try:
        int(user)
    except:
        #the username is loged in
        protocols_answer.login_protocol_op.GExit(sock)

    #poping the user out of the global dictioneries
    sock_username.pop(sock)
    if sock in sock_connect_msg:
        sock_connect_msg.pop(sock)
    else:
        sock_connect_msg[sock]= False
    
    try:
        sending_sock_key.pop(sock)
        sending_sock_signature.pop(sock)
    except:
        pass
    
    protocols_answer.game_protocol_op.GExit(user)
    try:
        int(user) #check is this is unlogined user (his username generated by the server and is number)
        anlogined_userNames.append(user)
    except:
        pass
    
    print(anlogined_userNames)

def presence_check(sock):
    """check does one socket still conected (in case of internate problems). NOTE: it supposed to be used as thread, and run until the socket don't conected.
    it make the socket exit the game if necessary.
    :param sock: the socket to check
    :type sock: socket.socket"""
    global sock_connect_msg

    print("presence_check start")
    for i in range(15):
        time.sleep(1)
        if done:
            print("presence_check threading out")
            return
    #so the server will have time to get user public key
    if sock in sock_connect_msg:
        sock_connect_msg.pop(sock)
        return
    else:
        sock_connect_msg[sock]= False
    try:
        sendMesegTCP(sock,"?")
    except:
        return
    conected= True
    while conected:
        print("while start")
        for i in range(15):
            time.sleep(1)
            if done:
                print("presence_check threading out")
                return
        if sock in sock_connect_msg:
            #print(sock_connect_msg[sock])
            if sock_connect_msg[sock]:
                #the user send conection answer
                sock_connect_msg[sock]= False
                try:
                    sendMesegTCP(sock,"?")
                except:
                    pass
            else:
                #the user haven't send the meseg
                #print("have no conection----\n",sock,sock_username[sock])
                GExit(sock)
                conected= False
            #print(sock_connect_msg[sock])
        else:
            #the user disconected from the game himself
            conected= False
            #print("the user exited itself----\n",e)
    print("disconnected")

def choose_unloged_username():
    """choose username for user that didn't loged in"""
    global next_anlogined_userName
    username= str(next_anlogined_userName)
    
    if len(anlogined_userNames)!=0:
        username= anlogined_userNames.pop(-1)
    else:
        next_anlogined_userName+=1

    return username

def init():
    """initialize any global variable"""
    global server_socket
    global anlogined_userNames
    global next_anlogined_userName
    global sock_username
    global sock_connect_msg
    global signed_in_usernames
    global online_matches
    global done
    
    protocols_answer.login_protocol_op.init()
    sending_data_init()

    server_socket = socket.socket()
    server_socket.bind(("0.0.0.0", 8820)) 
    server_socket.listen()

    anlogined_userNames=[] #just the temp ones
    next_anlogined_userName=1

    sock_username={}

    sock_connect_msg= {}
    #key- any socket that connected to the server (if socket isn't key of this dictionery, then he isb't conected to the server)
    #value has the server recived ! meseg from this user
    #sock_last_contect_q=deque()
    #save for eny user that sent to him ? array with the following indexes meaning:
    #[0]- the time by which the server supposed to resive ! maseg from the user
    #[1]- his socket
    #[2]- had the server resived ! meseg from him
    #[3]- is still conected

    #sock_q_dict= {} #store for every socket, pointer to its lst in sock_last_contect_q

    signed_in_usernames= {} #including the temple ones

    #for statistic
    online_matches=0

    #for quiting the program
    done= False
