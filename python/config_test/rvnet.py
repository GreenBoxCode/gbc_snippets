import os
import socket

wifi_flag = False
ethernet_flag = False
cell_flag = False
StarLink_flag = False
connection_flag = False
config_dict = {}


def get_inet_status():
    if connection_flag:
        print("Internet connection is available.")
    else:
        print("No internet connection. Finding connection...")
        connect()


def connect():
    # from config_dist find the first main key that has an available value of true
    # if no available value is true then return false
    # if available value is true then set the inuse value to true and return true
    for key, value in config_dict.items():
        if value["Available"]:
            # Psudeo code
            # Start connection process for key eg. INET_WIFI
            # if connection is successful then set the inuse value to true and return true
            value["INUSE"] = True
            print(f"Connecting to {key}")
            # set all other available values to false
            for key2, value2 in config_dict.items():
                if key2 != key:
                    value2["INUSE"] = False
                    sort_config(config_dict)
                    print_inet_status()
            return True
    pass


def init_config(config_dict):
    # The order of the keys in the dictionary is important
    # The first key with an available value of true will be used
    # The keys are checked in order
    # The cost of use increases from top to bottom ethernet -> wifi -> cell -> StarLink
    config_dict["INET_WIFI"] = {"INUSE": False, "Available": False, "Cost": 1}
    config_dict["INET_ETHERNET"] = {"INUSE": False, "Available": True, "Cost": 2}
    config_dict["INET_CELL"] = {"INUSE": False, "Available": False, "Cost": 3}
    config_dict["INET_StarLink"] = {"INUSE": False, "Available": False, "Cost": 4}
    # Save the config_dict to a file
    try:
        with open("RvNet.cnf", "w") as config_file:
          for key, value in config_dict.items():
            config_file.write(f"{key} {value}\n")
    except  Exception as e:
        print(f"Error saving config_dict to file: {str(e)}")
        return False
    """ # Read the config_dict from a file
    with open("RvNet.cnf", "r") as config_file:
        for line in config_file:
            key, value = line.split(" ", 1)
            config_dict[key] = value  # convert value to dict """


def sort_config(config_dict):
    # sort the config_dict by cost
    # return the sorted config_dict
    try:
        config_dict = sorted(
            config_dict.items(), key=lambda x: x[1]["Cost"]
        )  # sort by cost
        return config_dict
    except Exception as e:
        print(f"Error sorting config_dict: {str(e)}")
        return False


def print_inet_status():
    # Print the shared dictionary with the main key and inner key-value pairs on separate lines
    print("config_dict status:")
    print("-------------------")
    for main_key, inner_dict in config_dict.items():
        print(main_key)
        for inner_key, inner_value in inner_dict.items():
            print("\t", inner_key, inner_value)
    print("-------------------")


def main():
    init_config(config_dict)
    get_inet_status()


if __name__ == "__main__":
    main()
