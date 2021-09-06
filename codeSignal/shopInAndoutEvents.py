def shopInAndOutEvents(events):
    _map = dict()
    for event in events:
        person,signal = event
        if person not in _map:
            if signal != 'in':
                return False
            else:
                _map[person] = signal
        else:
            if _map[person] == 'in':
                if signal != 'out':
                    return False
                else:
                    _map[person] = signal
                
            else:# out
                if signal != 'in':
                    return False
                else:
                    _map[person] = signal
    print(_map)
    for p in _map:
        if _map[p] == 'in':
            return False
    return True

if __name__ == '__main__':
    test = [["John_0","in"], 
            ["Mary_0","in"], 
            ["John_0","out"], 
            ["Mary_0","out"]]
    ans = shopInAndOutEvents(test)
    print(ans)    