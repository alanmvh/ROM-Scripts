import htttp_request
import playsound


try:
    # In case that another item is needed
    # item = input("Enter refine and item to search e.g: +4 Dagger\n")
    item = "+9 Elven Ears"
    obj1 = htttp_request.request_poring(item)
    if(obj1.get_stock() < 2):
        playsound.playsound('alarm.mp3')
    else:
        print("Items with more than one unit: " + str(obj1.get_stock()))
        exit()
except:
    print("Something has occurred")