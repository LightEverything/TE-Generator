import StrParser


if __name__ == "__main__":
    args = input("请输入指令:\n")
    parser = StrParser.StrParse(args)
    
    writer = parser.ProcessArgsAndWrite()
    
    if writer:
        writer.SaveImage()
        writer.CopyToClipboard()