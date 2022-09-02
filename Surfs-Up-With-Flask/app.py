# 1. imports
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")


# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)


# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return(
         f"Welcome to my climate app! Available routes are: <br/>"
         f"/api/v1.0/precipitation<br/>"  
         f"/api/v1.0/stations<br/>" 
         f"/api/v1.0/tobs<br/>"
         f"/api/v1.0/<start>(Insert start date in YYYY-MM-DD)<br/>" 
         f"/api/v1.0/<start>(Insert start date in YYYY-MM-DD)/<end>(Insert end date in YYYY-MM-DD)"
         )


# Define what to do when a user hits the /api/v1.0/precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Server received request for 'precipitation' page...")
    
    Measurement = Base.classes.measurement

    session = Session(engine)

    sel = [Measurement.date,
       (Measurement.prcp)]

    PrevYearData = session.query(*sel).\
        filter(Measurement.date > '2016-08-23').\
        order_by(Measurement.date).all()
    
    session.close()
    
    prev_year_rain = list(np.ravel(PrevYearData))

    return jsonify(prev_year_rain)




# Define what to do when a user hits the /api/v1.0/stations route
@app.route("/api/v1.0/stations")
def Stations():
    print("Server received request for 'Stations' page...")
    
    Station = Base.classes.station

    session = Session(engine)

    select = [Station.id,
       (Station.station), (Station.name), (Station.latitude), (Station.longitude), (Station.elevation)]

    stationList = session.query(*select).\
        order_by(Station.id).all()
    
    session.close()
    
    stations_all = list(np.ravel(stationList))

    return jsonify(stations_all)
    


# Define what to do when a user hits the /api/v1.0/tobs route
@app.route("/api/v1.0/tobs")
def tobs():
    print("Server received request for 'tobs' page...")
    
    Measurement = Base.classes.measurement

    session = Session(engine)

    selection = [Measurement.station,
       (Measurement.tobs),
            (Measurement.date)]

    ListTobsMostActive = session.query(*selection).\
        filter(Measurement.station == 'USC00519281').\
        order_by(Measurement.tobs).all()
    
    session.close()
    
    tobsMostActive = list(np.ravel(ListTobsMostActive))

    return jsonify(tobsMostActive)



    # Define what to do when a user hits the /api/v1.0/<start> route
@app.route("/api/v1.0/<start>")
def start(start):
    print("Server received request for 'start' page...")
    
    Measurement = Base.classes.measurement

    session = Session(engine)

    selection = [Measurement.station,
       (Measurement.tobs),
            (Measurement.date)]

    ListTobsMostActive = session.query(*selection).\
        filter(Measurement.date > start).\
        order_by(Measurement.tobs).all()
    
    countRows = 0
    sumTemp = 0
    lowest = 999
    highest = 0

    for entry in ListTobsMostActive:
        countRows = countRows + 1
        sumTemp = sumTemp + int(entry.tobs)
        if(entry.tobs > highest ):
            highest = int(entry.tobs)
        if(entry.tobs < lowest ):
            lowest = int(entry.tobs)

        
    print('Lowest temp was ' + str(lowest))
    print('Highest temp was ' + str(highest))
    print('Average was '+str(sumTemp/countRows))

    session.close()

    return (
        f"Lowest temp was {str(lowest)}<br/>" 
        f"Highest temp was {str(highest)}<br/>"
        f"Average temp was {str(sumTemp/countRows)}<br/>"
    
    )

    # Define what to do when a user hits the /api/v1.0/<start>/<end> route
@app.route("/api/v1.0/<start>/<end>")
def startend(start,end):
    print("Server received request for 'start/end' page...")
    
    Measurement = Base.classes.measurement

    session = Session(engine)

    selection = [Measurement.station,
       (Measurement.tobs),
            (Measurement.date)]

    ListTobsMostActive = session.query(*selection).\
        filter(Measurement.date > start).\
        filter(Measurement.date < end).\
        order_by(Measurement.tobs).all()
    
    countRows = 0
    sumTemp = 0
    lowest = 999
    highest = 0

    for entry in ListTobsMostActive:
        countRows = countRows + 1
        sumTemp = sumTemp + int(entry.tobs)
        if(entry.tobs > highest ):
            highest = int(entry.tobs)
        if(entry.tobs < lowest ):
            lowest = int(entry.tobs)

        
    print('Lowest temp was ' + str(lowest))
    print('Highest temp was ' + str(highest))
    print('Average was '+str(sumTemp/countRows))

    session.close()

    return (
        f"Lowest temp was {str(lowest)}<br/>" 
        f"Highest temp was {str(highest)}<br/>"
        f"Average temp was {str(sumTemp/countRows)}<br/>"
    
    )


if __name__ == "__main__":
    app.run(debug=True)
