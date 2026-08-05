for lateral_error in [0,.2,.8,1.5,2.4]:
    penalty=1.5*abs(lateral_error)
    print(lateral_error,penalty)
