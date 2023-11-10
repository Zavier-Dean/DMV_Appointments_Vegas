# DMV_Appointments Las Vegas ONLY


# Required Libraries
- selenium
- Chrome must be installed
- **NOTE**: Firefox and Edge will be updated and added 

# About 
- This is a scheduling tool for getting appointments at the Las Vegas DMV. 
- Based off of the month desired 
- In most cases, the DMV is so full that the next couple months are completely full, therefore, really only the month is needed 
**NOTE**: Will update later on with actual times check at a later date 

## How to use
- Download the python file DMV_Appointments.py
- In the terminal write: pip install selenium
- Change location and Action needed based on the number system below 
- Run file 
- Script will cycle through the website several times until a month desired appears 
- If a month is found, It will remain open for 2 minutes awaiting to finish filling out your information {Subject to change in further updates}
- Script will run for 40 attempts 
- In the terminal, press **ctrl + c** to cancel at anytime

## Location guide 
- Change the Location number based on which location
  
1. Carson City 
2. Decatur 
3. Flamingo 
4. Henderson
5. Sahara
6. South Reno

## Action guide
- Change action based on the numbers below

1. ADA - Disabilities Center
2. Drivers License - Renewal 
3. Drivers License - New 
4. Knowledge/ Written Testing
5. License Plate Pickup\ Drop off
6. Multiple Transactions (DL & Registration)
7. Registration - New
8. Registration - Renewal
9. Suspensions (Reinstatements) - Driver License/Revenue Recovery
10. Suspensions (Reinstatements) - Registration/Revenue Recovery

- This selection doesn't really matter, as long as its close to what you need.
- For example, added a motorcycle endorsement to a current license would be under "Drivers License - Renewal"
- **NOTE**: The DMV closes Knowledge tests one hour before they close 

# Developer Notes - What's to come
- Options will be moved to a JSON file where it can be edited easier 
- Firefox and Edge support 
- Time check 
- More options to cancel actions 
- Better structure 
  - __I am a new-ish developer and understand that my code is quite messy and easy to break. I will be working on making it more sound in the future updates__
  - All waiting is on sleeps (Will be fixed fist!)

