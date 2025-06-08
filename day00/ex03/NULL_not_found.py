def NULL_not_found(object: any) -> int:
    try:
        if object is None:
            print('Nothing: None', type(object))
        elif type(object) is float:
            print('Cheese: ', object, type(object))
        elif object == 0 and type(object) is int:
            print('Zero:', object, type(object))
        elif type(object) is str:
            if not object:
                print('Empty:', type(object))
            else:
                raise Exception()
        elif type(object) is bool:
            print('Fake:', object, type(object))
        return 0
    except Exception:
        print('Type not Found')
        return 1
