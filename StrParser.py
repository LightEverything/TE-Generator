import PngWriter

def ColorStrToTuple(colorStr):
    s = colorStr.strip("()")
    parts = s.split(",")
    result = tuple(map(int, parts))
    
    return result

class StrParse:
    args = ""
    
    def __init__(self, args) -> None:
        self.args = args
    
    def SetArgs(self, args):
        self.args = args
    
    def ProcessArgsAndWrite(self):
        args = self.args.replace(" ", "")
        
        try:
            writer = PngWriter.PngWriter()
            argsList = args.split("|")
            for arg in argsList:
                # 检查是不是文本
                if arg.find(":") != -1:
                    key, value = arg.split(":")
                    
                    if key == "color":
                        writer.color = ColorStrToTuple(value)
                    elif key == "fontSize":
                        writer.fontSize = int(value)
                    elif key == "font":
                        writer.font = value
                    elif key == "bgColor":
                        writer.bgColor = ColorStrToTuple(value)
                    elif key == "blankBorderSize":
                        writer.blankBorderSize = int(value)
                    elif key == "fileName":
                        writer.filename = value
                    else:
                        raise Exception("指令错误")
                    
                else:
                    writer.text = arg
            return writer
        except:
            print("命令错误，请检查你的命令")
        return None