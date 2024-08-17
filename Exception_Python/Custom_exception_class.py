class emtyException(RuntimeError):
    def __init__(self,arguments):
        self.arguments=arguments

var=""
var1=""

try:
    raise emtyException("this variable empty string")
except emtyException as e:
    print(e.arguments)

