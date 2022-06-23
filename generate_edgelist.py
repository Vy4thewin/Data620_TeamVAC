
states = [
    "Alabama",
    "Alaska",
    "Arizona",
    "Arkansas",
    "California",
    "Colorado",
    "Connecticut",
    "Delaware",
    "Florida",
    "Georgia",
    "Hawaii",
    "Idaho",
    "Illinois",
    "Indiana",
    "Iowa",
    "Kansas",
    "Kentucky",
    "Louisiana",
    "Maine",
    "Maryland",
    "Massachusetts",
    "Michigan",
    "Minnesota",
    "Mississippi",
    "Missouri",
    "Montana",
    "Nebraska",
    "Nevada",
    "New.Hampshire",
    "New.Jersey",
    "New.Mexico",
    "New.York",
    "North.Carolina",
    "North.Dakota",
    "Ohio",
    "Oklahoma",
    "Oregon",
    "Pennsylvania",
    "Rhode.Island",
    "South.Carolina",
    "South.Dakota",
    "Tennessee",
    "Texas",
    "Utah",
    "Vermont",
    "Virginia",
    "Washington",
    "West.Virginia",
    "Wisconsin",
    "Wyoming"]


edges = [
    [1,1,1,1,1,1,1,1,1],
    [1,1,1,0,1,1,1,1,0],
    [1,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,1,0],
    [1,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,0,1,1],
    [1,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,1,0],
    [1,1,1,0,1,1,1,1,0],
    [1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,0,1,1],
    [0,1,1,0,1,1,1,0,0],
    [1,0,0,0,0,1,1,1,0],
    [1,0,0,0,0,0,0,0,0],
    [1,1,1,0,1,1,1,1,0],
    [1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,1],
    [1,1,1,1,1,0,1,1,0],
    [0,1,1,0,0,1,1,1,1],
    [1,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0],
    [1,1,1,0,1,1,1,1,0],
    [1,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,1,1],
    [1,1,1,1,1,1,1,0,0],
    [0,1,1,0,1,1,0,1,1],
    [1,1,1,0,0,0,0,0,0],
    [0,1,1,0,0,1,0,0,1],
    [0,0,0,0,0,0,1,1,1],
    [1,1,1,1,1,1,1,1,0],
    [1,1,1,0,1,1,1,0,1],
    [1,1,1,1,1,1,1,1,0],
    [1,0,0,0,0,0,0,0,0],
    [0,1,1,0,0,1,1,1,0],
    [1,1,1,1,1,1,1,0,1],
    [0,1,1,0,1,0,0,0,1],
    [0,1,1,1,1,1,0,0,0],
    [1,1,1,1,1,1,1,0,0],
    [1,1,1,0,0,1,0,1,1],
    [0,1,1,1,1,1,1,1,0],
    [0,1,1,1,0,1,0,1,1],
    [0,1,0,0,0,1,0,0,1],
    [1,0,0,0,0,0,0,0,1],
    [1,1,1,0,1,1,0,1,1],
    [1,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,1,1] ]

for i in range(50):
    if edges[i][0] == 1:
        print ("{0},incompat,{{}}".format(states[i]))
    if edges[i][1] == 1:
        print ("{0},cruelty,{{}}".format(states[i]))
    if edges[i][2] == 1:
        print ("{0},desertn,{{}}".format(states[i]))
    if edges[i][3] == 1:
        print ("{0},nonsupp,{{}}".format(states[i]))
    if edges[i][4] == 1:
        print ("{0},alcohol,{{}}".format(states[i]))
    if edges[i][5] == 1:
        print ("{0},felony,{{}}".format(states[i]))
    if edges[i][6] == 1:
        print ("{0},impotenc,{{}}".format(states[i]))
    if edges[i][7] == 1:
        print ("{0},insanity,{{}}".format(states[i]))
    if edges[i][8] == 1:
        print ("{0},separate,{{}}".format(states[i]))
