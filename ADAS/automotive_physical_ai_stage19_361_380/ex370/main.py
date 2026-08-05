for distance,error in [(5,.2),(.4,.2),(5,2.6)]:
    collision=distance<=.5
    lane_departure=abs(error)>=2.5
    terminated=collision or lane_departure
    print(distance,error,terminated)
