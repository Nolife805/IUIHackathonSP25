import requests
from datetime import datetime 

def csc_info():
    """
    Returns a nested dictionary of all the washers / dryers on IUI campus and their statuses, as well as summary info for each laundry room
    """
    iteration = {}
    current = datetime.now()
    for n in range(0, 3):

        # 001 - Ball
        # 002 - Tower
        # 003 - North
        url = "https://mycscgo.com/api/v3/location/acaabe28-c929-4ac5-826f-0e9869307df6/room/19262-00"
        m = requests.get(url = url + str(n+1) + "/machines")
        s = requests.get(url = url + str(n+1) + "/summary")
        machines = m.json()
        summary = s.json()

        detailed = {}
        for i in machines:
            detailed.update({
                    i['stickerNumber'] : {
                        "type" : i['type'],
                        "available" : i['available'],
                        "timeRemaining" : i['timeRemaining'],
                    }
            })

        iteration.update({
            summary["roomLabel"] : {
                "washersFree" : summary['washers']['available'],
                "washersTotal" : summary['washers']['total'],
                "dryersFree" : summary['dryers']['available'],
                "dryersTotal" : summary['dryers']['total'],
                "machines" : detailed
            }
        })
    
    output = {
        'time' : str(current),
        "rooms" : iteration
    }

    return output




        


