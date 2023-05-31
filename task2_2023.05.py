import re

def extractfiledirnamext(text_str):
    try:
        regpat = r"""
            (?P<directory>(?:[a-zA-Z]:)?(?:[\\/][^\\/]+)*[\\/])?  
            (?P<name>(?:(?!\.)[\w-]+|\.(?!\.)[\w-]+)*)        
            (?P<extension>(?:\.(?!\btxt\b|\bbat\b)[\w-]+)?)?     
            $                                                      
        """
        regexpr = re.compile(regpat, re.VERBOSE)
    
        file_info = []
        for line in text_str.splitlines():
            match = regexpr.match(line)
            if match:
                directory = match.group("directory")
                name = match.group("name")
                extension = match.group("extension")
                if not directory and not name:
                    directory = None
                elif not directory and name:
                    directory = ""
                elif directory and not directory.endswith(("/", "\\")):
                    directory += "/"
                if extension == "":
                    extension = None
                file_info.append((directory, name, extension))
            else:
                file_info.append(None)
        
        return file_info
    except Exception as e:
        print(f"Error found: {e}")
        return None
