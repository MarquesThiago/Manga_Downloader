HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
REDEFINED = "\033[0;0m"
PROCESS = "\033[1;37;42m"



def message_information(text):
    print(OKBLUE + str(text) + REDEFINED)
    
def message_sucess(text):
    print(OKGREEN +  str(text) + REDEFINED)

def message_failed(text):
    print(FAIL +  str(text)  + REDEFINED)

def message_warning(text):
    print(WARNING +  str(text) + REDEFINED)

def process(text):
    print(PROCESS + f" {text} " + REDEFINED)

