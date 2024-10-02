def NULL_not_found(object: any) -> int:
    if not object or (object != object):
        name_str = type(object).__name__
        otype = type(object)
        match name_str:
            case "NoneType":
                print("Nothing:", object, otype)
            case "bool":
                print("Fake:", object, otype)
            case "str":
                print("Empty:", object, otype)
            case "float":
                print("Cheese:", object, otype)
            case "int":
                print("Zero:", object, otype)
        return (0)
    else:
        print("Type not Found")
        return (1)
