def all_thing_is_obj(object: any) -> int:
    name_str = type(object).__name__
    otype = type(object)
    match name_str:
        case "str":
            print(object, "is in the kitchen :", otype)
        case "set":
            print("Set :", otype)
        case "dict":
            print("Dict :", otype)
        case "list":
            print("List :", otype)
        case "tuple":
            print("Tuple :", otype)
        case _:
            print("Type not found")
    return 42
