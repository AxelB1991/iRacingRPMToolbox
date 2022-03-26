from iracingdataapi.client import irDataClient

import os
import pandas as pd


cars_lapfile = []
cars_results = []
simsession = []
laps = []
subsessionID = int(input("What session would you like to scrape?")) #45043469


idc = irDataClient(username=os.getenv('IRAPI_USR'), password=os.getenv('IRAPI_PWD'))

Data = idc.get_result(subsessionID)

for SessionResult in Data["session_results"]:
    if SessionResult["simsession_type"] == 6: # or SessionResult["simsession_type"] == 5 or SessionResult["simsession_type"] == 4:
        simsession = []
        simsession.append(SessionResult["simsession_type"])  

        for driver in SessionResult["results"]:
            cars_lapfile = []
            cars_lapfile.append(driver["display_name"])  
            cars_lapfile.append(driver["starting_position"])  
            cars_lapfile.append(driver["reason_out"])  
            cars_lapfile.append(driver["finish_position"])  
            cars_lapfile.append(driver["interval"])  
            cars_lapfile.append(driver["laps_lead"])  
            cars_lapfile.append(driver["average_lap"])  
            cars_lapfile.append(driver["best_lap_time"])  
            cars_lapfile.append(driver["best_lap_num"])  
            cars_lapfile.append(driver["laps_complete"])  
            cars_lapfile.append(driver["incidents"])  
            try:
                cars_lapfile.append(driver["club_name"]) 
            except:
                cars_lapfile.append("")
            cars_lapfile.append(driver["newi_rating"])  
            cars_lapfile.append(driver["new_license_level"])  
            cars_lapfile.append(driver["finish_position_in_class"])  
            cars_lapfile.append(driver["car_id"])  
            try:
                cars_lapfile.append(driver["cust_id"])  
            except:
                cars_lapfile.append(driver["team_id"])
            cars_lapfile.append(driver["car_class_id"])  
            cars_lapfile.append(SessionResult["simsession_type"])
            print(cars_lapfile)
    
            cars_results.append(cars_lapfile)
            if SessionResult["simsession_type"] == 6:
            try:
                laps += idc.get_result_lap_data(subsession_id=subsessionID, cust_id=driver["cust_id"])
            except:
                laps += idc.get_result_lap_data(subsession_id=subsessionID, team_id=driver["team_id"])
            

    
df = pd.DataFrame(laps)
df.to_csv(str(subsessionID) + '_laps.csv', index=False)
df = pd.DataFrame(cars_results)
df.to_csv(str(subsessionID) +'_result.csv', index=False)