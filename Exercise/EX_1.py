temperature_MIN = 29.5
temperature_MAX = 46.5

temperature_health_MIN = 35.5
temperature_health_MAX = 37.5

def convert_temp_f(temp_c):
    return  temp_c*1.8+32

def extra_message_print(temp_f):
    if (temp_c>temperature_MAX) or (temp_c<temperature_MIN):
        extra_message = f"Abnormal temperature {temp_f}. Check your thermometr!"
    else:
        if (temp_c<=temperature_health_MIN) and (temp_c>=temperature_health_MAX):
            extra_message = f"Temperature {temp_f} is noraml"
        elif (temp_c<temperature_health_MIN):
            extra_message = f"Temperature {temp_f} is lower. Call your doctor"
        elif (temp_c>temperature_health_MAX):
            extra_message = f"Temerature {temp_f} is higher. Call yoy doctor"

    return extra_message

temp_c = float(input("Input temperure in C :")) 

print (f"Temperature in F {convert_temp_f(temp_c)}:")
#extra_message = ""

print (extra_message_print(convert_temp_f(temp_c)))

