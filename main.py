import psutil, win32process, win32gui, time, datetime, json

programs_structure={}
application_counter=0
applications = []

def get_application_name():
    process = win32gui.GetForegroundWindow()
    pid = win32process.GetWindowThreadProcessId(process)
    return psutil.Process(pid[-1]).name()
    
def structure_activity():
    
    global applications
    global application_counter
    #params
    year = datetime.date.today().year #year
    month = datetime.date.today().strftime("%B")
    day = time.asctime()[8:11] + " " + time.asctime()[0:3]
    today = str(datetime.date.today())
    application_counter = len(applications)
    
    #lists of app and number
    daily_stat=dict([
        ("Number of Applications", application_counter),
        ("Applications", applications)
        ])
    #daily stat
    daily = dict([
        (day, daily_stat),
        ])
    #monthly stat
    monthly = dict([
        (month, daily)
        ])
    #yearly stat: main
    programs_structure[year] = monthly
        
    with open('structure.json', 'w') as json_file:
        json.dump(programs_structure, json_file, indent=4)


def main():
    
    flashes = set()
    global applications
    for index in range(10):
        
        time.sleep(2)
        flashes.add(str(get_application_name())[:-4].upper()) #name of program in upper case)
    applications =list(flashes)
    structure_activity()


if __name__ == "__main__":
    main()

