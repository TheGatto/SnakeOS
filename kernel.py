
from Files.sys.kernel.module import *

#Test
def createDir(directory:str):
    try:
        os.mkdir(directory)
    except Exception as message:
        pass

class Boot:
    def makeDirectories():
        createDir(selectedDir+'/Files')
        dir = selectedDir+'/Files'
        createDir(dir+'/prgmdir')
        createDir(dir+'/User')
        createDir(dir+'/sys')
        dir += '/sys'
        createDir(dir+'/snkAssets')
        createDir(dir+'/kernel')
        dir = dir.replace('/sys','')
        dir += '/User/'
        try:
            with open(dir+'Shortcuts.snk','x') as f:
                f.close()
        except:
            pass


def getKernelData(auth:str,version:float):
    hostName = getKernel()
    hostIP = getIP(auth)
    timeNow = datetime.now()
    return ["SnakeOS TERMINAL [V"+str(version)+"]" + '[' + str(timeNow) + ']','Ker: ' + hostName,'IP: ' + hostIP]

def crash():
    import ctypes
    p = ctypes.pointer(ctypes.c_char.from_address(1))
    p[0] = b'x' # noqa


def returnTo(data:str, location:str = 'TER'):
    if location == 'TER':
        print(data)
    elif location == 'CLIP':
        pyperclip.copy(data)
    else:
        print("Invalid location")

def getIP(auth:str):
    if len(auth.split('›')) > 2:
        return 'Incorrect Password'
    auth = auth.split('›')
    if checkEncryption(auth[0], int(auth[1])):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(("8.8.8.8", 80))
            hostIP = (s.getsockname()[0])
        except:
            hostIP = ('No Internet Connection')
        return hostIP
    else:
        return 'Incorrect Password'

def getKernel():
    return socket.gethostname()


def encryptWord(text):
    def encryptLetter(realText, step):
        outText = []
        cryptText = []
        uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z']
        lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']
        for eachLetter in realText:
            if eachLetter in uppercase:
                index = uppercase.index(eachLetter)
                crypting = (index + step) % 26
                cryptText.append(crypting)
                newLetter = uppercase[crypting]
                outText.append(newLetter)
            elif eachLetter in lowercase:
                index = lowercase.index(eachLetter)
                crypting = (index + step) % 26
                cryptText.append(crypting)
                newLetter = lowercase[crypting]
                outText.append(newLetter)
            else:
                outText.append(eachLetter)
        return outText
    orgword=text
    word=list(orgword)
    code=""
    count=1
    for i in range (0,len(orgword)):
        if i % 2==0:
            code = code+"".join(encryptLetter(word[i], i-count))
            count+=2
        elif i % 3==0:
            code = code + "".join(encryptLetter(word[i], i))
            count-=1
        else:
            if count%2==0:
                code = code + "".join(encryptLetter(word[i], i+count))
                count+=1
            else:
                code = code + "".join(encryptLetter(word[i], i-count))
                count-=2

    return code





def createEncryptedUserFile(password:str,key:int):
    alphabetLower = list(map(chr, range(97, 123)))
    alphabetUpper = [x.upper() for x in alphabetLower]
    symbols = ['!','@','#','$','%','^','&','*','(',')','-','_','+']
    numbers = list(a for a in range (10))
    numbers = [str(x) for x in numbers]
    enc = encryptWord(password)
    file = []
    previous = None
    for i in range(0,key):
        if previous != 3:
            selection = randint(0, 4)
            if selection == 1 or selection == 0:
                file.append(alphabetLower[randint(0, 25)])
                previous = None
            elif selection == 2:
                file.append(alphabetUpper[randint(0, 25)])
                previous = None
            elif selection == 3:
                file.append(numbers[randint(0,9)])
                previous = 3
            else:
                if randint(0,2) > 1:
                    selection = randint(1, 3)
                    if selection < 2:
                        file.append(alphabetLower[randint(0, 25)])
                        previous = None
                    elif selection == 2:
                        file.append(alphabetUpper[randint(0, 25)])
                        previous = None
                    else:
                        file.append(numbers[randint(0, 9)])
                        previous = 3
                else:
                    file.append(symbols[randint(0,12)])
                    previous = None
        else:
            if randint(0,10) < 2:
                file.append(numbers[randint(0, 9)])
                previous = 3
            else:
                selection = randint(0, 4)
                if selection == 1 or selection == 0:
                    file.append(alphabetLower[randint(0, 25)])
                    previous = None
                elif selection == 2:
                    file.append(alphabetUpper[randint(0, 25)])
                    previous = None
                elif selection == 3:
                    file.append(numbers[randint(0, 9)])
                    previous = 3
                else:
                    if randint(0, 2) > 1:
                        selection = randint(1, 3)
                        if selection < 2:
                            file.append(alphabetLower[randint(0, 25)])
                            previous = None
                        elif selection == 2:
                            file.append(alphabetUpper[randint(0, 25)])
                            previous = None
                        else:
                            file.append(numbers[randint(0, 9)])
                            previous = 3
                    else:
                        file.append(symbols[randint(0, 12)])
                        previous = None
    file.append(enc)
    next = round((key*3)/4)
    for i in range(next):
        selection = randint(-4, 4)
        if selection < 2:
            file.append(alphabetLower[randint(0, 25)])
        elif selection == 2:
            file.append(alphabetUpper[randint(0, 25)])
        elif selection == 3:
            file.append(numbers[randint(0,9)])
        else:
            if randint(0,2) > 1:
                selection = randint(1, 3)
                if selection < 2:
                    file.append(alphabetLower[randint(0, 25)])
                elif selection == 2:
                    file.append(alphabetUpper[randint(0, 25)])
                elif selection == 3:
                    file.append(numbers[randint(0, 9)])
            else:
                file.append(symbols[randint(0,12)])

    with open('/Users/home/PycharmProjects/SnakeOSFinal/Files/User/Encrypt.txt','w') as f:
        f.write(''.join(file))


def checkEncryption(inputtedPassword:str, key:int):
    encInput = encryptWord(inputtedPassword)
    with open('/Users/home/PycharmProjects/SnakeOSFinal/Files/User/Encrypt.txt','r') as f:
        data = f.readlines()
        data = str(data)
    next = round((key*3)/4)
    passlength = round(len(data)-(next+key))
    encPass = data[key+2:passlength+key-2]
    if encInput == encPass:
        return True
    return False

def openFile(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])



def startupProtocol(version:float,professional:bool,shortCommands:bool):
    d = json.load(open('Files/User/Shortcuts.snk'))
    json.dump(d, open("/Users/home/PycharmProjects/SnakeOSFinal/Files/sys/snkAssets/snkShcut.txt", 'w'))
    sleep(0.5)
    #os.system(f"say {'Snake OS v'+str(__version__)}")
    print('Booting __version__ '+str(version)+'...')
    sys.path.append('/Files/prgmdir')
    global selectedDir
    global shCommands
    shCommands = False
    #Create the sdir
    selectedDir = '/Users/home/PycharmProjects/SnakeOSFinal'
    #Make directories and check if presen
    global shortcuts
    shortcuts = json.load(open("/Users/home/PycharmProjects/SnakeOSFinal/Files/sys/snkAssets/snkShcut.txt"))
    Boot.makeDirectories()
    if shortCommands:
        shCommands = True
    if not professional:
        playsound('Files/sys/snkAssets/Startup.mp3')
        print('Welcome User')
        return
    selectedDir = '/Users/home/PycharmProjects/SnakeOSFinal/Files/prgmdir'


def readShortcutData(key:str):
    ...


def playsound(file:str):
    try:
        os.system('afplay '+file)
    except:
        print('Error Occured')

def ping(host:str, number:str):
    param = '-n' if platform.system() == 'windows' else '-c'
    call = ['ping', param, number, host]
    return subprocess.call(call)


def address(data, position:int):
    return data[position]


def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')



def createUser(name:str, encpass:str, key:int):
    createEncryptedUserFile(encpass, key)
    name = address(name,0).upper()+name[1:]
    try:
        os.mkdir('Files/'+name)
    except:
        print('Error occured, this may have occured due to directory tampering')


def register(key):
    print("No current user was detected, registration required.")
    userCheck = False
    password = ''
    while not userCheck:
        name = input("Input username ")
        if len(name) in range(4, 12):
            userCheck = True
        else:
            print('Username must be inbetween 4 and 8 characters!')
    passCheck = False
    while not passCheck:
        password = passW("Input Password ")
        if " " in password:
            print("Password cannot have spaces!")
        elif password.isalpha() or password.isnumeric():
            print("Password must be alphanumerical!")
        elif len(password) < 5:
            print("Password must be more than 4 characters long!")
        elif len(password) > 18:
            print("Password cannot be longer than 18 characters long!")
        elif [password] == name:  # noqa
            print("Your password cannot be the same as your username!")
        else:
            passCheck = True
    createUser(name, password, key)
    password = None
    print('Registration Successful!')




def mainLoop(key:int):
    global selectedDir, shCommands
    commands = ('sdir', 'ip', 'user', 'kernel', 'help', 'sd','clear','ldir','udir','crash')
    commandsArg = ('cdir', 'echo', 'run', 'qkrun','open', 'touch')
    commandsArg2 = ('return',)
    enteredInput = input(">>>")
    if len(enteredInput) < 2 :
        return
    identifier = address(enteredInput,0)
    if not shCommands:
        code = enteredInput[1:]
    else:
        code = enteredInput
    if identifier != '!' and not shCommands:
        print("Command '"+enteredInput+"' does not exist")
        return
    code = code.split()
    arguments = len(code)-1
    command = code[0]

    if command in commands:
        if len(code) == 1:
            if command == 'sdir':
                returnTo(selectedDir, 'TER')
            if command == 'ip':
                print(getIP(passW('Input Password ')+'›'+str(key)))
            if command == 'sd':
                playsound('Files/sys/snkAssets/Shutdown.mp3')
                exit()
            if command == 'user':
                print('Not Implemented')
            if command == 'help':
                print(commands+commandsArg+commandsArg2)
            if command == 'kernel':
                print(getKernel())
            if command == 'clear':
                clearScreen()
            if command == 'ldir':
                print(os.listdir(selectedDir))
            if command == 'udir':
                print((os.path.dirname(selectedDir)))
            if command == 'crash':
                playsound('Files/sys/snkAssets/Error.mp3')
                crash()
        else:
            print("Unexpected Arguments (Expected None)")
    elif command in commandsArg:
        if arguments == 1:
            if command == 'cdir':
                if os.path.exists(code[1]):
                    selectedDir = code[1]
                    selectedDir = os.path.abspath(selectedDir)
                else:
                    if code[1] == 'udir':
                        selectedDir = os.path.dirname(selectedDir)
                    else:
                        print("Path '"+code[1]+"' does not exist")
            if command == 'run':
                if not code[1].endswith('.py'):
                    code[1] += '.py'
                if os.path.isfile(selectedDir + '/' + code[1]):
                    try:
                        subprocess.run(['python', selectedDir + '/' + code[1]])
                    except KeyboardInterrupt:
                        print("\nProgram Forcequitted")
                    print("Process Finished")
                else:
                    print("No file named '",code[1],"' in ",selectedDir + '/' )
            if command == 'qkrun':
                if code[1].lower() in shortcuts:
                    argument = code[1].lower()
                    cmd = os.path.join(os.getcwd(), shortcuts[argument])
                    os.system('{} {}'.format('python', cmd))
                    print("Process finished")
                else:
                    print("No shortcut named '"+code[1]+"'")
            if command == 'echo':
                print(code[1])
            if command == 'open':
                if os.path.isfile(selectedDir+'/'+code[1]):
                    openFile(selectedDir+'/'+code[1])
                else:
                    print("No file named '",code[1],"' in ",selectedDir + '/' )
            if command == 'touch':
                try:
                    with open(code[1],'x') as file:
                        pass
                except:
                    print("File already exists.")
        else:
            if arguments >1:
                print("Unexpected arguments (One Expected)")
            else:
                print("Argument Expected (One Expected)")
    elif command in commandsArg2:
        if arguments == 2:
            if command == 'return':
                returnTo(code[1],code[2])
        else:
            if arguments > 2:
                print("Unexpected arguments (Two Expected)")
            else:
                print("Argument Expected (Two Expected)")
    else:
        if shCommands:
            print("Command '"+ command + "' does not exist")
        else:
            print("Command '"+identifier+command+"' does not exist")
