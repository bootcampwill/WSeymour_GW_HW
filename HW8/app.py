
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
session = Session(engine)
# Save reference to the table
Measurement = Base.classes.measurement
Station     = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
	    f"/api/v1.0/tobs<br/>"
	    f"/api/v1.0/<start><br/>"
	    f"/api/v1.0/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    results = session.query(Measurement.prcp, Measurement.date).all()
 
    session.close()

    # Convert list of tuples into normal list
    all_measurements = list(np.ravel(results))

    # Create a dictionary from the row data and append to a list
    all_measurements = []
    for date, prcp in results:
        measurements_dict = {}
        measurements_dict["date"] = date
        measurements_dict["prcp"] = prcp
        all_measurements.append(measurements_dict)

    return jsonify(all_measurements)


@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of stations"""
    # Query all Stations
    results = session.query(Station.station, Station.name, Station.latitude, Station.longitude, Station.elevation).all()

    session.close()

    # Convert list of tuples into normal list
    all_stations = list(np.ravel(results))

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """get dates from 12 months before the last observation and forward"""
    # Query
    results = session.query(Measurement.tobs).filter(Measurement.date >= "2016-08-23").all()

    session.close()
    
    # Convert list of tuples into normal list
    oneYear = list(np.ravel(results))

    return jsonify(oneYear)

@app.route("/api/v1.0/<string:start>/<string:end>")

def calc_temps(start, end):
    session = Session(engine)
    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all()

# function usage example
    print(calc_temps(start, end))

# Use your previous function `calc_temps` to calculate the tmin, tavg, and tmax 
# for your trip using the previous year's data for those same dates.
    print(calc_temps(start, end))
    x = calc_temps(start, end)
    min = x[0][0]
    mean = x[0][1]
    max = x[0][2]

    jsonify(x)
    jsonify(min)
    jsonify(mean)
    jsonify(max)

if __name__ == '__main__':
    app.run(debug=True)