 # Manual Testing
## Admin Login
 * Epic :  Login
 * Prerequisites :  None

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Navigate to Amber page | https://amber-ci.herokuapp.com/ | Page showing <br />1) Links:Home, My account, Login  <br />2) Title  <br />3) Subtitle  <br />4) Splash image | 
| Click Login link |  | Login page appears | 
| Click Login | * Username : **Admin**<br />   * Password : administrate | Page showing <br />1) Links:Home, Add Diagnosis, Add User, My account, Logout <br />2) Title  <br />3) Subtitle  <br />4) Splash image | 

##  Login – incorrect details
 * Epic :  Login
 * Prerequisites :  None

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Navigate to Amber page | https://amber-ci.herokuapp.com/ | Page showing <br />1) Links:Home, My account, Login  <br />2) Title  <br />3) Subtitle  <br />4) Splash image | 
| Click Login link |  | Login page appears | 
| Click Login | * Username : **Admin**<br />   * Password : incorrect | * Blank Login page re-appears  <br />* Message indicating the login failed | 

##  Login – blank username
 * Epic :  Login
 * Prerequisites :  None

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Navigate to Amber page | https://amber-ci.herokuapp.com/ | Page showing <br />1) Links:Home, My account, Login  <br />2) Title  <br />3) Subtitle  <br />4) Splash image | 
| Click Login link |  | Login page appears | 
| Click Login | * Username : (leave blank)   <br />* Password : administrate | Message indicating the username field needs to be filled | 

##  Login – blank password
 * Epic :  Login
 * Prerequisites :  None

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Navigate to Amber page | https://amber-ci.herokuapp.com/ | Page showing <br />1) Links:Home, My account, Login  <br />2) Title  <br />3) Subtitle  <br />4) Splash image | 
| Click Login link |  | Login page appears | 
| Click Login | * Username : Admin   <br />* Password : (leave blank) | Message indicating the password field needs to be filled | 

## Occupational Therapist Login
 * Epic :  Login
 * Prerequisites :  None

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Navigate to Amber page | https://amber-ci.herokuapp.com/ | Page showing <br />1) Links:Home, My account, Login  <br />2) Title  <br />3) Subtitle  <br />4) Splash image | 
| Click Login link |  | Login page appears | 
| Click Login | * Username : **OT**   <br />* Password : Occupational | Page showing <br />1) Links:<br />*    Home<br />*    Add Client<br />*    Edit Client<br />*    Record a Session<br />*    View Session<br />*    Generate Charts<br />*    My account<br />*    Logout  <br />2) Title  <br />3) Subtitle  <br />4) Splash image | 

## Hippotherapy Analyst Login
 * Epic :  Login
 * Prerequisites :  None

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Navigate to Amber page | https://amber-ci.herokuapp.com/ | Page showing <br />1) Links:Home, My account, Login  <br />2) Title  <br />3) Subtitle  <br />4) Splash image | 
| Click Login link |  | Login page appears | 
| Click Login | * Username : **HA**  <br />* Password : *HipAnalyst* | Page showing <br />1) Links:<br />*    Home<br />*    View Session<br />*    Generate Charts<br />*    My account<br />*    Logout  <br />2) Title  <br />3) Subtitle  <br />4) Splash image | 

## Logout
 * Epic :  Login
 * Prerequisites :  None

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Navigate to Amber page | https://amber-ci.herokuapp.com/ | Page showing <br />1) Links:Home, My account, Login  <br />2) Title  <br />3) Subtitle  <br />4) Splash image | 
| Login | Login as any user | Appropriate Home Page shows | 
| Click Logout |  | Sign out page shows | 
| Click Sign Out |  | Page showing <br />1) Links:Home, My account, Login  <br />2) Title  <br />3) Subtitle  <br />4) Splash image | 

## Add Diagnosis
 * Epic :  Maintain Configuration
 * Prerequisites :  Logged in as Admin user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Click Add Diagnosis link |  | ''Add Diagnosis’ page appears<br />Showing a list of existing diagnoses | 
| Fill out ‘Add Diagnosis’ form | * Diagnosis : lmpetigo | Field is filled out | 
| Click Add Diagnosis button |  | ''Add Diagnosis’ page re-appears<br />with message informing that the new diagnosis has been added.<br />The new diagnosis also appears on the list. | 

## Add duplicate Diagnosis
 * Epic :  Maintain Configuration
 * Prerequisites :  Logged in as Admin user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Click Add Diagnosis link |  | ''Add Diagnosis’ page appears<br />Showing a list of existing diagnoses | 
| Fill out ‘Add Diagnosis’ form | * Diagnosis : lmpetigo (or any existing diagnosis) | Field is filled out | 
| Click Add Diagnosis button |  | ''Add Diagnosis’ page re-appears<br />with message informing duplicates are not allowed.<br />The duplicate diagnosis is on the list only once. | 

## Add User – Occupational Therapist
 * Epic :  Maintain Users
 * Prerequisites :  Logged in as Admin user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Click ‘Add User’ link |  | ''Add User’ page appears | 
| Fill out ‘Add User’ form | * Username : Fred<br />* First Name : Freddie<br />* Last Name : Flintstone<br />* Role : **Occupational Therapist** <br />* Password : yabbadabbadoo<br />* Confirm Password : yabbadabbadoo | Fields are all filled out | 
| Click Save New User button |  | ''Add User’ page re-appears<br />with a message informing the new user has been added. | 
| Login as newly created user | * Username : Fred<br />* Password : yabbadabbadoo | Occupational Therapist home page appears with only the appropriate links | 

## Add Duplicate User
 * Epic :  Maintain Users
 * Prerequisites :  Logged in as Admin user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Click Add User link |  | ''Add User’ page appears | 
| Fill out ‘Add User’ form | * Username : Fred<br />* First Name : Freddie<br />* Last Name : Flintstone<br />* Role : Occupational Therapist<br />* Password : yabbadabbadoo<br />* Confirm Password : yabbadabbadoo | Fields are all filled out | 
| Click Save New User button |  | ''Add User’ blank page re-appears<br />With a message informing that duplicate users are not allowed. | 

## Add User – Hippotherapy Analyst
 * Epic :  Maintain Users
 * Prerequisites :  Logged in as Admin user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Click Add User link |  | ''Add User’ page appears | 
| Fill out ‘Add User’ form | * Username : Barney<br />* First Name : Barney<br />* Last Name : Rubble<br />* Role : **Hippotherapy Analyst**<br />* Password :heybetty<br />* Confirm Password : heybetty | Fields are all filled out | 
| Click Save New User button |  | ''Add User’ page re-appears<br />with a message informing the new user has been added | 
| Login as newly created user | * Username : Fred<br />* Password : heybetty | Hippotherapy Analyst home page appears with only the appropriate links | 

## Add User – Admin
 * Epic :  Maintain Users
 * Prerequisites :  Logged in as Admin user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Click Add User link |  | ''Add User’ page appears | 
| Fill out ‘Add User’ form | * Username : Dino<br />* First Name : Dino<br />* Last Name : Saur<br />* Role : **Admin**<br />* Password :pebblespet<br />* Confirm Password : pebblespet | Fields are all filled out | 
| Click Save New User button |  | ''Add User’ page re-appears<br />With a message informing the new user has been added | 
| Login as newly created user | * Username : Dino<br />* Password : pebblespet | Admin home page appears with only the appropriate links | 

## Add User – Cancel
 * Epic :  Maintain Users
 * Prerequisites :  Logged in as Admin user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Click Add User link |  | ''Add User’ page appears | 
| Fill out ‘Add User’ form | * Username : Dino<br />* First Name : Dino<br />* Last Name : Saur<br />* Role : Admin<br />* Password :pebblespet<br />* Confirm Password : pebblespet | Fields are all filled out | 
| Click ‘Cancel’ button |  | The new user is NOT added to the Amber System.<br />Admin Home page appears. | 

## Add User – Reset
 * Epic :  Maintain Users
 * Prerequisites :  Logged in as Admin user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Click Add User link |  | ''Add User’ page appears | 
| Fill out ‘Add User’ form | * Username : Dino<br />* First Name : Dino<br />* Last Name : Saur<br />* Role : Admin<br />* Password :pebblespet<br />* Confirm Password : pebblespet | Fields are all filled out | 
| Click ‘Reset’ button |  | All fields on the form are reset.<br />Text inputs show their placeholder text.<br />Dropdown choices are unselected.<br />Password and Confirm Password fields are blank. | 

## My Account – Change Admin user details
 * Epic :  Maintain Users
 * Prerequisites :  Logged in as Admin user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Click My Account link |  | ''My Account’ page appears<br />Shows my username<br />Text Input filled with my First Name<br />Text Input filled with my Last Name | 
| Change my name | * First Name : New First<br />* Last Name : New Last | Fields are all filled out | 
| Click Save My Account button |  | Home Page is displayed.<br />Welcome message is **Welcome, New First**. | 

## My Account – Cancel
 * Epic :  Maintain Users
 * Prerequisites :  Logged in as Admin user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Click My Account link |  | ''My Account’ page appears<br />Shows my username<br />Text Input filled with my First Name<br />Text Input filled with my Last Name | 
| Change my name | * First Name : Cancel First<br />* Last Name : Cancel Last | Fields are all filled out | 
| Click Cancel button |  | Home Page is displayed.<br />Welcome message shows the **old** First Name. | 

## My Account – Reset Form
 * Epic :  Maintain Users
 * Prerequisites :  Logged in as Admin user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Click My Account link |  | ''My Account’ page appears<br />Shows my username<br />Text Input filled with my First Name<br />Text Input filled with my Last Name | 
| Change my name | * First Name : Reset First<br />* Last Name : Reset Last | Fields are all filled out | 
| Click Reset Form button |  | ''My Account’ page appears.<br />Shows my username.<br />Text Input filled with **original** First Name.<br />Text Input filled with **original** Last Name | 

## My Account – Change Occupational Therapist user details
 * Epic :  Maintain Users
 * Prerequisites :  Logged in as Occupational Therapist user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Click My Account link |  | ''My Account’ page appears<br />Shows my username<br />Text Input filled with my First Name<br />Text Input filled with my Last Name | 
| Change my name | * First Name : OT First<br />* Last Name : OT Last | Fields are all filled out | 
| Click Save My Account button |  | Home Page is displayed.<br />Welcome message is **Welcome, *OT First**. | 

## My Account – Change Hippotherapy Analyst user details
 * Epic :  Maintain Users
 * Prerequisites :  Logged in as Hippotherapy Analyst user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Click My Account link |  | ''My Account’ page appears<br />Shows my username<br />Text Input filled with my First Name<br />Text Input filled with my Last Name | 
| Change my name | * First Name : HA First<br />* Last Name : HA Last | Fields are all filled out | 
| Click Save My Account button |  | Home Page is displayed.<br />Welcome message is **Welcome, *HA First**. | 

## View Session
 * Epic :  Record Session
 * Prerequisites :  Logged in as Hippotherapy Analyst user or Occupational Therapist user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Click View Session link |  | ''Select Client’ page appears | 
| Pick a client | Click the ‘Pick’ button next to a client | ''Select Session’ page appears | 
| Choose a session to view | Click the radio button next to one of the sessions<br />Click the **Select this Session** button | ''View Session’ page appears.<br />Session date<br />Course Number<br />Week Number<br />Horse name<br />Table of tasks performed during session<br />Table of observation scores for the session | 

## View Session – Client Cancel
 * Epic :  Record Session
 * Prerequisites :  Logged in as Hippotherapy Analyst user or Occupational Therapist user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Click View Session link |  | ''Select Client’ page appears | 
| Click the Cancel button |  | Appropriate Home page appears. | 

## View Session – Session Cancel
 * Epic :  Record Session
 * Prerequisites :  Logged in as Hippotherapy Analyst user or Occupational Therapist user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Click View Session link |  | ''Select Client’ page appears | 
| Pick a client | Click the ‘Pick’ button next to a client | ''Select Session’ page appears | 
| Click the Cancel button |  | Appropriate Home page appears. | 

## View Session – Session Reset
 * Epic :  Record Session
 * Prerequisites :  Logged in as Hippotherapy Analyst user or Occupational Therapist user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Click View Session link |  | ''Select Client’ page appears | 
| Pick a client | Click the ‘Pick’ button next to a client | ''Select Session’ page appears | 
| Choose a session to view | Click the radio button next to one of the buttons | Radio button is selected | 
| Reset the form | Click the **Reset Form** button | **No** radio buttons are selected | 

## View Session – None Selected
 * Epic :  Record Session
 * Prerequisites :  Logged in as Hippotherapy Analyst user or Occupational Therapist user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Click View Session link |  | ''Select Client’ page appears | 
| Pick a client | Click the ‘Pick’ button next to a client | ''Select Session’ page appears | 
| Try to View Session without any selected | Click the **Select this Session** button | ''Select Session’ page re-appears.<br />With error message informing that a session needs to be selected before proceeding to view a session | 

## Record Session – New Client
 * Epic :  Record Session
 * Prerequisites :  Logged in as Hippotherapy Analyst user or Occupational Therapist user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Click *Record Session* link |  | ''Select Client’ page appears | 
| Pick a client | Click the ‘Pick’ button next to a client who has no sessions recorded yet | ''Record Session’ page appears.<br />Client name<br />Current Date<br />Course number<br />Week number | 
| Enter session details | Horse<br />Mounted Tasks<br />Unmounted Tasks | Form fields filled out | 
| Save Session | Click the **Save Session** button | ‘Session Observations’ page appears.<br />With message indicating a new session has been created for this user. | 
| Enter session observations | Select a score for each skill (row) under every Function | Form fields filled out | 
| Save Observations | Click the **Save Observations** button | ''Course Chart’ page appears.<br />Shows the chart for this session. | 

## Record Session – Next Week
 * Epic :  Record Session
 * Prerequisites :  Logged in as Hippotherapy Analyst user or Occupational Therapist user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Click *Record Session* link |  | ''Select Client’ page appears | 
| Pick a client | Click the ‘Pick’ button next to a client who has had sessions recorded | ''Last Session’ page appears.<br />Client name<br />Current Date<br />Course number<br />Week number<br />Start a new course checkbox (leave unchecked) | 
| Record Session | Click the **Record Session** button | ''Record Session’ page appears.<br />Client name<br />Current Date<br />Course number = Course number on the previous page<br />Week number = 1 more than the Week number on the previous page | 
| Enter session details | Horse<br />Mounted Tasks<br />Unmounted Tasks | Form fields filled out | 
| Save Session | Click the **Save Session** button | ‘Session Observations’ page appears.<br />With message indicating a new session has been created for this user. | 
| Enter session observations | Select a score for each skill (row) under every Function | Form fields filled out | 
| Save Observations | Click the **Save Observations** button | ''Course Chart’ page appears.<br />Shows the chart for this session. | 

## Record Session – New Course
 * Epic :  Record Session
 * Prerequisites :  Logged in as Hippotherapy Analyst user or Occupational Therapist user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Click *Record Session* link |  | ''Select Client’ page appears | 
| Pick a client | Click the ‘Pick’ button next to a client who has had sessions recorded | ''Last Session’ page appears.<br />Client name<br />Current Date<br />Course number<br />Week number<br />Start a new course checkbox | 
| Start new course | Click the **New Course** checkbox | ''New Course’ checkbox is ticked | 
| Record Session | Click the **Record Session** button | ''Record Session’ page appears.<br />Client name<br />Current Date<br />Course number = 1 more than the Course number on the previous page<br />Week number = 1 | 
| Enter session details | Horse<br />Mounted Tasks<br />Unmounted Tasks | Form fields filled out | 
| Save Session | Click the **Save Session** button | ‘Session Observations’ page appears.<br />With message indicating a new session has been created for this user. | 
| Enter session observations | Select a score for each skill (row) under every Function | Form fields filled out | 
| Save Observations | Click the **Save Observations** button | ''Course Chart’ page appears.<br />Shows the chart for this session. | 

## Record Session – No Horses
 * Epic :  Record Session
 * Prerequisites :  Logged in as Hippotherapy Analyst user or Occupational Therapist user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Click *Record Session* link |  | ''Select Client’ page appears | 
| Pick a client | Click the ‘Pick’ button next to a client who has had sessions recorded | ''Last Session’ page appears.<br />Client name<br />Current Date<br />Course number<br />Week number<br />Start a new course checkbox (leave unchecked) | 
| Record Session | Click the **Record Session** button | ''Record Session’ page appears.<br />Client name<br />Current Date<br />Course number = Course number on the previous page<br />Week number = 1 more than the Week number on the previous page | 
| Enter session details | Horse (leave unselected)<br />Mounted Tasks<br />Unmounted Tasks | Horse Form field unselected | 
| Save Session | Click the **Save Session** button | ‘Record Session’ page re-appears.<br />With message indicating a horse needs to be chosen. | 

## Record Session – Missing observations
 * Epic :  Record Session
 * Prerequisites :  Logged in as Hippotherapy Analyst user or Occupational Therapist user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Click *Record Session* link |  | ''Select Client’ page appears | 
| Pick a client | Click the ‘Pick’ button next to a client who has had sessions recorded | ''Last Session’ page appears.<br />Client name<br />Current Date<br />Course number<br />Week number<br />Start a new course checkbox (leave unchecked) | 
| Record Session | Click the **Record Session** button | ''Record Session’ page appears.<br />Client name<br />Current Date<br />Course number = Course number on the previous page<br />Week number = 1 more than the Week number on the previous page | 
| Enter session details | Horse<br />Mounted Tasks<br />Unmounted Tasks | Form fields filled out | 
| Save Session | Click the **Save Session** button | ‘Session Observations’ page appears.<br />With message indicating a new session has been created for this user. | 
| Enter session observations | Select a score for some skills (rows) under every Function<br />Leave some skills unselected | Some Form fields *not* filled out | 
| Save Observations | Click the **Save Observations** button | ‘Session Observations’ page appears.<br />With error message indicating all skills need to be scored.<br />Previous observations are automatically filled in. | 

## Record Session – Cancel Observations
 * Epic :  Record Session
 * Prerequisites :  Logged in as Hippotherapy Analyst user or Occupational Therapist user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Click *Record Session* link |  | ''Select Client’ page appears | 
| Pick a client | Click the ‘Pick’ button next to a client who has had sessions recorded | ''Last Session’ page appears.<br />Client name<br />Current Date<br />Course number<br />Week number<br />Start a new course checkbox (leave unchecked) | 
| Record Session | Click the **Record Session** button | ''Record Session’ page appears.<br />Client name<br />Current Date<br />Course number = Course number on the previous page<br />Week number = 1 more than the Week number on the previous page | 
| Enter session details | Horse<br />Mounted Tasks<br />Unmounted Tasks | Form fields filled out | 
| Save Session | Click the **Save Session** button | ‘Session Observations’ page appears.<br />With message indicating a new session has been created for this user. | 
| Enter session observations | Select a score for each skill (row) under every Function | Form fields filled out | 
| Cancel Observations | Click the **Cancel** button | Appropriate 'Home’ page appears.<br />Observations are not saved for this session. | 

## Record Session – Reset Observations
 * Epic :  Record Session
 * Prerequisites :  Logged in as Hippotherapy Analyst user or Occupational Therapist user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Click *Record Session* link |  | ''Select Client’ page appears | 
| Pick a client | Click the ‘Pick’ button next to a client who has had sessions recorded | ''Last Session’ page appears.<br />Client name<br />Current Date<br />Course number<br />Week number<br />Start a new course checkbox (leave unchecked) | 
| Record Session | Click the **Record Session** button | ''Record Session’ page appears.<br />Client name<br />Current Date<br />Course number = Course number on the previous page<br />Week number = 1 more than the Week number on the previous page | 
| Enter session details | Horse<br />Mounted Tasks<br />Unmounted Tasks | Form fields filled out | 
| Save Session | Click the **Save Session** button | ‘Session Observations’ page appears.<br />With message indicating a new session has been created for this user. | 
| Enter session observations | Select a score for each skill (row) under every Function | Form fields filled out | 
| Reset Observations | Click the **Reset Form** button | ''Session Observations’ page re-appears.<br />All radio buttons are unselected. | 

## Record Session – Cancel Session
 * Epic :  Record Session
 * Prerequisites :  Logged in as Hippotherapy Analyst user or Occupational Therapist user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Click *Record Session* link |  | ''Select Client’ page appears | 
| Pick a client | Click the ‘Pick’ button next to a client who has had sessions recorded | ''Last Session’ page appears.<br />Client name<br />Current Date<br />Course number<br />Week number<br />Start a new course checkbox (leave unchecked) | 
| Record Session | Click the **Record Session** button | ''Record Session’ page appears.<br />Client name<br />Current Date<br />Course number = Course number on the previous page<br />Week number = 1 more than the Week number on the previous page | 
| Enter session details | Horse<br />Mounted Tasks<br />Unmounted Tasks | Form fields filled out | 
| Cancel Session | Click the **Cancel** button | Appropriate ‘Home’ page appears.<br />Session is **not** saved. | 

## Record Session – Reset Session
 * Epic :  Record Session
 * Prerequisites :  Logged in as Hippotherapy Analyst user or Occupational Therapist user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Click *Record Session* link |  | ''Select Client’ page appears | 
| Pick a client | Click the ‘Pick’ button next to a client who has had sessions recorded | ''Last Session’ page appears.<br />Client name<br />Current Date<br />Course number<br />Week number<br />Start a new course checkbox (leave unchecked) | 
| Record Session | Click the **Record Session** button | ''Record Session’ page appears.<br />Client name<br />Current Date<br />Course number = Course number on the previous page<br />Week number = 1 more than the Week number on the previous page | 
| Enter session details | Horse<br />Mounted Tasks<br />Unmounted Tasks | Form fields filled out | 
| Reset Session | Click the **Reset Form** button | ‘Record Session’ page re-appears.<br />No horse has been chosen.<br />All task checkboxes are unticked. | 

## Record Session – Cancel Last Session
 * Epic :  Record Session
 * Prerequisites :  Logged in as Hippotherapy Analyst user or Occupational Therapist user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Click *Record Session* link |  | ''Select Client’ page appears | 
| Pick a client | Click the ‘Pick’ button next to a client who has had sessions recorded | ''Last Session’ page appears.<br />Client name<br />Current Date<br />Course number<br />Week number<br />Start a new course checkbox (leave unchecked) | 
| Cancel  | Click the **Cancel** button | Appropriate 'Home’ page appears.<br />Session is not saved. | 

## Record Session – Reset Last Session
 * Epic :  Record Session
 * Prerequisites :  Logged in as Hippotherapy Analyst user or Occupational Therapist user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Click *Record Session* link |  | ''Select Client’ page appears | 
| Pick a client | Click the ‘Pick’ button next to a client who has had sessions recorded | ''Last Session’ page appears.<br />Client name<br />Current Date<br />Course number<br />Week number<br />Start a new course checkbox | 
| Start new course | Check the **Start new course** checkbox | ''Start new Course’ checkbox is ticked | 
| Reset | Click the **Reset Form** button | ''Last Session’ page re-appears.<br />‘Start new Course’ checkbox is unticked. | 

## Add Client
 * Epic :  Maintain Client
 * Prerequisites :  Logged in as Occupational Therapist user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| If on a larger screen device | Click the **Client ...** dropdown | ''Add Client’ and ‘Edit Client’ links appear. | 
| Click Add Client link |  | ''Add Client’ page appears | 
| Enter the new client details | First Name : Mickey<br />Last Name : Mouse<br />Gender: Male<br />Date of Birth: 15th May 1928<br />Hat Size: 3 1/2<br />Diagnosis: ADHD<br />Degree of difficulty: Unbearably high-pitched voice<br />Additional Notes: Disney’s most memorable character | Form filled out | 
| Save new client | Click the **Save new client** button | ''Add Client’ page re-appears.<br />Form fields are blank.<br />No Checkboxes are selected.<br />Message indicating that the new client has been added appears. | 

## Add Client – Missing First Name
 * Epic :  Maintain Client
 * Prerequisites :  Logged in as Occupational Therapist user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| If on a larger screen device | Click the **Client ...** dropdown | ''Add Client’ and ‘Edit Client’ links appear. | 
| Click Add Client link |  | ''Add Client’ page appears | 
| Enter the new client details | First Name : (leave blank)<br />Last Name : Mouse<br />Gender: Female<br />Date of Birth: 15th May 1928<br />Hat Size: 3 1/2<br />Diagnosis: ADD<br />Degree of difficulty: Not too difficult<br />Additional Notes: Mickey’s girlfriend | Form filled out | 
| Try to save new client | Click the **Save new client** button | ''Add Client’ page re-appears.<br />Form fields are as previously entered.<br />Message indicating that the first name field needs to be filled in.<br />New client has *not* been added. | 

## Add Client – Missing Last Name
 * Epic :  Maintain Client
 * Prerequisites :  Logged in as Occupational Therapist user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| If on a larger screen device | Click the **Client ...** dropdown | ''Add Client’ and ‘Edit Client’ links appear. | 
| Click Add Client link |  | ''Add Client’ page appears | 
| Enter the new client details | First Name : Minnie<br />Last Name : (leave blank)<br />Gender: Female<br />Date of Birth: 15th May 1928<br />Hat Size: 3 1/2<br />Diagnosis: ADD<br />Degree of difficulty: Not too difficult<br />Additional Notes: Mickey’s girlfriend | Form filled out | 
| Try to save new client | Click the **Save new client** button | ''Add Client’ page re-appears.<br />Form fields are as previously entered.<br />Message indicating that the last name field needs to be filled in.<br />New client has *not* been added. | 

## Add Client – Missing Date of Birth
 * Epic :  Maintain Client
 * Prerequisites :  Logged in as Occupational Therapist user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| If on a larger screen device | Click the **Client ...** dropdown | ''Add Client’ and ‘Edit Client’ links appear. | 
| Click Add Client link |  | ''Add Client’ page appears | 
| Enter the new client details | First Name : Minnie<br />Last Name : Mouse<br />Gender: Female<br />Date of Birth: (leave blank)<br />Hat Size: 3 1/2<br />Diagnosis: ADD<br />Degree of difficulty: Not too difficult<br />Additional Notes: Mickey’s girlfriend | Form filled out | 
| Try to save new client | Click the **Save new client** button | ''Add Client’ page re-appears.<br />Form fields are as previously entered.<br />Message indicating that the date of birth field needs to be filled in.<br />New client has *not* been added. | 

## Add Client – Missing Hat Size
 * Epic :  Maintain Client
 * Prerequisites :  Logged in as Occupational Therapist user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| If on a larger screen device | Click the **Client ...** dropdown | ''Add Client’ and ‘Edit Client’ links appear. | 
| Click Add Client link |  | ''Add Client’ page appears | 
| Enter the new client details | First Name : Minnie<br />Last Name : Mouse<br />Gender: Female<br />Date of Birth: 15th May 1928<br />Hat Size: (leave blank)<br />Diagnosis: ADD<br />Degree of difficulty: Not too difficult<br />Additional Notes: Mickey’s girlfriend | Form filled out | 
| Try to save new client | Click the **Save new client** button | ''Add Client’ page re-appears.<br />Form fields are as previously entered.<br />Message indicating that the hat size field needs to be filled in.<br />New client has *not* been added. | 

## Add Client – Incorrect date format
 * Epic :  Maintain Client
 * Prerequisites :  Logged in as Occupational Therapist user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| If on a larger screen device | Click the **Client ...** dropdown | ''Add Client’ and ‘Edit Client’ links appear. | 
| Click Add Client link |  | ''Add Client’ page appears | 
| Enter the new client details | First Name : Minnie<br />Last Name : Mouse<br />Gender: Female<br />Date of Birth: 12/21/1970<br />Hat Size: 3 1/2<br />Diagnosis: ADD<br />Degree of difficulty: Not too difficult<br />Additional Notes: Mickey’s girlfriend | Form filled out | 
| Try to save new client | Click the **Save new client** button | ''Add Client’ page re-appears.<br />Form fields are as previously entered.<br />Message indicating that the first name field needs to be filled in.<br />New client has *not* been added. | 

## Add Client – Cancel
 * Epic :  Maintain Client
 * Prerequisites :  Logged in as Occupational Therapist user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| If on a larger screen device | Click the **Client ...** dropdown | ''Add Client’ and ‘Edit Client’ links appear. | 
| Click Add Client link |  | ''Add Client’ page appears | 
| Enter the new client details | First Name : Minnie<br />Last Name : Mouse<br />Gender: Female<br />Date of Birth: 15th May 1928<br />Hat Size: 3 1/2<br />Diagnosis: ADD<br />Degree of difficulty: Not too difficult<br />Additional Notes: Mickey’s girlfriend | Form filled out | 
| Cancel the new client | Click the **Cancel** button | ''Home’ page appears.<br />New client has *not* been added. | 

## Add Client – Reset
 * Epic :  Maintain Client
 * Prerequisites :  Logged in as Occupational Therapist user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| If on a larger screen device | Click the **Client ...** dropdown | ''Add Client’ and ‘Edit Client’ links appear. | 
| Click Add Client link |  | ''Add Client’ page appears | 
| Enter the new client details | First Name : Minnie<br />Last Name : Mouse<br />Gender: Female<br />Date of Birth: 15th May 1928<br />Hat Size: 3 1/2<br />Diagnosis: ADD<br />Degree of difficulty: Not too difficult<br />Additional Notes: Mickey’s girlfriend | Form filled out | 
| Reset | Click the **Reset Form** button | ''Add Client’ page re-appears.<br />Form fields are blank.<br />Nothing is selected in the hat size dropdown.<br />No diagnoses are checked.<br />New client has *not* been added. | 

## Edit Client
 * Epic :  Maintain Client
 * Prerequisites :  Logged in as Occupational Therapist user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| If on a larger screen device | Click the **Client ...** dropdown | ''Add Client’ and ‘Edit Client’ links appear. | 
| Click Edit Client link |  | ''List of Clients’ page appears.<br />A list of clients appear.<br />One client per row.<br />At the end of each row is an Edit button and a Delete button | 
| Click the Edit button for one of the clients |  | ''Edit Client’ page appears.<br />Populated with the selected client’s details. | 
| Enter the existing client’s details | First Name : Donald<br />Last Name : Duck<br />Gender: Male<br />Date of Birth: 9th June 1920<br />Hat Size: 5<br />Diagnosis: ASD, ADHD<br />Degree of difficulty: Obstreporous<br />Additional Notes: Gets angry very easily | Form filled out | 
| Save changes | Click the **Save changes** button | ''List of Clients’ page re-appears.<br />Message indicating that client has been changed.<br />Existing client has been modified. | 

## Edit Client – Missing First name
 * Epic :  Maintain Client
 * Prerequisites :  Logged in as Occupational Therapist user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| If on a larger screen device | Click the **Client ...** dropdown | ''Add Client’ and ‘Edit Client’ links appear. | 
| Click Edit Client link |  | ''List of Clients’ page appears.<br />A list of clients appear.<br />One client per row.<br />At the end of each row is an Edit button and a Delete button | 
| Click the Edit button for one of the clients |  | ''Edit Client’ page appears.<br />Populated with the selected client’s details. | 
| Enter the existing client’s details | First Name : (leave blank)<br />Last Name : Duck<br />Gender: Male<br />Date of Birth: 9th June 1920<br />Hat Size: 5<br />Diagnosis: ASD, ADHD<br />Degree of difficulty: Obstreporous<br />Additional Notes: Gets angry very easily | Form filled out | 
| Save changes | Click the **Save changes** button | ''Edit Client’ page re-appears.<br />Form fields are as previously entered.<br />Message indicating that the first name field needs to be filled in.<br />Client has *not* been  modified. | 

## Edit Client – Missing Last name
 * Epic :  Maintain Client
 * Prerequisites :  Logged in as Occupational Therapist user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| If on a larger screen device | Click the **Client ...** dropdown | ''Add Client’ and ‘Edit Client’ links appear. | 
| Click Edit Client link |  | ''List of Clients’ page appears.<br />A list of clients appear.<br />One client per row.<br />At the end of each row is an Edit button and a Delete button | 
| Click the Edit button for one of the clients |  | ''Edit Client’ page appears.<br />Populated with the selected client’s details. | 
| Enter the existing client’s details | First Name : Donald<br />Last Name : (leave blank)<br />Gender: Male<br />Date of Birth: 9th June 1920<br />Hat Size: 5<br />Diagnosis: ASD, ADHD<br />Degree of difficulty: Obstreporous<br />Additional Notes: Gets angry very easily | Form filled out | 
| Save changes | Click the **Save changes** button | ''Edit Client’ page re-appears.<br />Form fields are as previously entered.<br />Message indicating that the last name field needs to be filled in.<br />Client has *not* been  modified. | 

## Edit Client – Missing Date of Birth
 * Epic :  Maintain Client
 * Prerequisites :  Logged in as Occupational Therapist user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| If on a larger screen device | Click the **Client ...** dropdown | ''Add Client’ and ‘Edit Client’ links appear. | 
| Click Edit Client link |  | ''List of Clients’ page appears.<br />A list of clients appear.<br />One client per row.<br />At the end of each row is an Edit button and a Delete button | 
| Click the Edit button for one of the clients |  | ''Edit Client’ page appears.<br />Populated with the selected client’s details. | 
| Enter the existing client’s details | First Name : Donald<br />Last Name : Duck<br />Gender: Male<br />Date of Birth: 9th June 1920<br />Hat Size: 5<br />Diagnosis: ASD, ADHD<br />Degree of difficulty: Obstreporous<br />Additional Notes: Gets angry very easily | Form filled out | 
| Save changes | Click the **Save changes** button | ''Edit Client’ page re-appears.<br />Form fields are as previously entered.<br />Message indicating that the date of birth field needs to be filled in.<br />Client has *not* been  modified. | 

## Edit Client – Cancel
 * Epic :  Maintain Client
 * Prerequisites :  Logged in as Occupational Therapist user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| If on a larger screen device | Click the **Client ...** dropdown | ''Add Client’ and ‘Edit Client’ links appear. | 
| Click Edit Client link |  | ''List of Clients’ page appears.<br />A list of clients appear.<br />One client per row.<br />At the end of each row is an Edit button and a Delete button | 
| Click the Edit button for one of the clients |  | ''Edit Client’ page appears.<br />Populated with the selected client’s details. | 
| Enter the existing client’s details | First Name : Donald<br />Last Name : Duck<br />Gender: Male<br />Date of Birth: 9th June 1920<br />Hat Size: 5<br />Diagnosis: ASD, ADHD<br />Degree of difficulty: Obstreporous<br />Additional Notes: Gets angry very easily | Form filled out | 
| Cancel changes | Click the **Cancel** button | ''List of Clients’ page re-appears.<br />Client has *not* been  modified. | 

## Edit Client – Reset
 * Epic :  Maintain Client
 * Prerequisites :  Logged in as Occupational Therapist user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| If on a larger screen device | Click the **Client ...** dropdown | ''Add Client’ and ‘Edit Client’ links appear. | 
| Click Edit Client link |  | ''List of Clients’ page appears.<br />A list of clients appear.<br />One client per row.<br />At the end of each row is an Edit button and a Delete button | 
| Click the Edit button for one of the clients |  | ''Edit Client’ page appears.<br />Populated with the selected client’s details. | 
| Enter the existing client’s details | First Name : (leave blank)<br />Last Name : Duck<br />Gender: Male<br />Date of Birth: 9th June 1920<br />Hat Size: 5<br />Diagnosis: ASD, ADHD<br />Degree of difficulty: Obstreporous<br />Additional Notes: Gets angry very easily | Form filled out | 
| Reset | Click the **Reset Form** button | ''Edit Client’ page re-appears.<br />Form fields are blank.<br />Hat size dropdown has nothing selected.<br />No diagnoses are checked.<br />Client has *not* been  modified. | 

## Generate Chart
 * Epic :  View Chart
 * Prerequisites :  Logged in as Hippotherapy Analyst user or Occupational Therapist user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Click *Generate Chart*link |  | ''Select Client’ page appears | 
| Pick a client | Click the ‘Pick’ button next to a client | ''Select Course’ page appears | 
| Choose a Course to generate the chart for | Click the radio button next to one of the Courses<br />Click the **Select this Course** button | ''Course Chart’ page appears.<br />Last Session date<br />Course Number<br />Week Number<br />A graph showing the breakdown of latest scores for the chosen course.<br />If there are more than one session in the course then the scores for the baseline (first) course are also shown. | 

## Generate Chart – No course
 * Epic :  View Chart
 * Prerequisites :  Logged in as Hippotherapy Analyst user or Occupational Therapist user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Click *Generate Chart*link |  | ''Select Client’ page appears | 
| Pick a client | Click the ‘Pick’ button next to a client | ''Select Course’ page appears | 
| Choose a Course to generate the chart for | Click the **Select this Course** button without selecting a course | ''Select Course’ page re-appears.<br />With a message indicating a Course needs to be chosen. | 

## Generate Chart – Cancel
 * Epic :  View Chart
 * Prerequisites :  Logged in as Hippotherapy Analyst user or Occupational Therapist user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Click *Generate Chart*link |  | ''Select Client’ page appears | 
| Pick a client | Click the ‘Pick’ button next to a client | ''Select Course’ page appears | 
| Cancel | Click the **Cancel** button | Appropriate 'Home’ page appears.<br />No graph is shown. | 

## Generate Chart – Reset
 * Epic :  View Chart
 * Prerequisites :  Logged in as Hippotherapy Analyst user or Occupational Therapist user

`Test Script :`

| Action | Inputs | Expected Output | 
| --- | --- | --- | 
| Click *Generate Chart*link |  | ''Select Client’ page appears | 
| Pick a client | Click the ‘Pick’ button next to a client | ''Select Course’ page appears | 
| Choose a Course to generate the chart for | Click the radio button next to one of the Courses | Radio button shows that the course is selected. | 
| Reset | Click the **Reset Form** button | ''Select Course’ page appears.<br />No Courses are selected. | 

