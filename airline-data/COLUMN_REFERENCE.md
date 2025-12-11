# Data Dictionary: MCO vs MIA Clean Dataset

**File:** `data/processed/mco_mia_clean.csv.gz`
**Rows:** ~1.6M flights (2004-2008, filtered for MCO/MIA)
**Date Range:** 2004-01-01 to 2008-04-30

---

## Original Columns

### Flight Identification
- **Year** - Flight year (2004-2008)
- **Month** - Month (1-12)
- **DayofMonth** - Day of month (1-31)
- **DayOfWeek** - Day of week (1=Monday, 7=Sunday)
- **UniqueCarrier** - Airline code (e.g., "AA", "DL", "UA")
- **FlightNum** - Flight number
- **TailNum** - Aircraft tail number

### Airports & Distance
- **Origin** - Origin airport code
- **Dest** - Destination airport code
- **Distance** - Flight distance in miles

### Scheduled Times (CRS = Computer Reservation System)
- **CRSDepTime** - Scheduled departure time (HHMM format, e.g., 1625 = 4:25 PM)
- **CRSArrTime** - Scheduled arrival time (HHMM format)
- **CRSElapsedTime** - Scheduled flight duration (minutes)

### Actual Times
- **DepTime** - Actual departure time (HHMM format)
- **ArrTime** - Actual arrival time (HHMM format)
- **ActualElapsedTime** - Actual flight duration (minutes)
- **AirTime** - Time in air (minutes)
- **TaxiOut** - Taxi out time (minutes)
- **TaxiIn** - Taxi in time (minutes)

### Delays
- **DepDelay** - Departure delay (minutes, negative = early)
- **ArrDelay** - Arrival delay (minutes, negative = early)
- **CarrierDelay** - Delay caused by carrier (minutes)
- **WeatherDelay** - Delay caused by weather (minutes)
- **NASDelay** - Delay caused by National Aviation System (minutes)
- **SecurityDelay** - Delay caused by security (minutes)
- **LateAircraftDelay** - Delay caused by late aircraft (minutes)

### Cancellations & Diversions
- **Cancelled** - Cancelled flag (0=No, 1=Yes)
- **CancellationCode** - Reason for cancellation (A=Carrier, B=Weather, C=NAS, D=Security)
- **Diverted** - Diverted flag (0=No, 1=Yes)

---

## Derived Columns (Added in Cleaning)

### Date/Time Features
- **FlightDate** - Full date (datetime format: YYYY-MM-DD)
- **CRSDepTime_Hour** - Scheduled departure hour (0-23)
- **CRSDepTime_Min** - Scheduled departure minute (0-59)
- **DepTime_Hour** - Actual departure hour (0-23)
- **DepTime_Min** - Actual departure minute (0-59)
- **CRSArrTime_Hour** - Scheduled arrival hour (0-23)
- **CRSArrTime_Min** - Scheduled arrival minute (0-59)
- **ArrTime_Hour** - Actual arrival hour (0-23)
- **ArrTime_Min** - Actual arrival minute (0-59)
- **DayName** - Day name (Mon, Tue, Wed, Thu, Fri, Sat, Sun)
- **Quarter** - Quarter of year (1-4)
- **IsHolidaySeason** - Holiday months flag (True for Jun-Aug, Nov-Dec)

### Performance Metrics
- **OnTime** - On-time performance (True if arrived ≤15 min late AND not cancelled)
- **DelayCategory** - Delay severity:
  - `Early` - Arrived early
  - `OnTime` - 0-15 min delay
  - `Delayed` - 15-60 min delay
  - `SeverelyDelayed` - >60 min delay

### Airport Indicators
- **IsMCO** - Flight involves MCO (True if Origin=MCO OR Dest=MCO)
- **IsMIA** - Flight involves MIA (True if Origin=MIA OR Dest=MIA)
- **MCO_Direction** - Direction for MCO flights:
  - `Departure` - Departing from MCO
  - `Arrival` - Arriving at MCO
  - `None` - Doesn't involve MCO
- **MIA_Direction** - Direction for MIA flights:
  - `Departure` - Departing from MIA
  - `Arrival` - Arriving at MIA
  - `None` - Doesn't involve MIA

### Flight Categorization
- **TimeOfDay** - Departure time category:
  - `Night` - 00:00-05:59
  - `Morning` - 06:00-11:59
  - `Afternoon` - 12:00-17:59
  - `Evening` - 18:00-23:59
- **IsWeekend** - Weekend flag (True for Sat/Sun)
- **Season** - Season based on month:
  - `Winter` - Dec, Jan, Feb
  - `Spring` - Mar, Apr, May
  - `Summer` - Jun, Jul, Aug
  - `Fall` - Sep, Oct, Nov
- **DistanceCategory** - Distance range:
  - `Short` - 0-500 miles
  - `Medium` - 500-1000 miles
  - `Long` - 1000-2000 miles
  - `VeryLong` - >2000 miles
- **PrimaryDelayCause** - Main cause of delay:
  - `None` - No delay (arrived early/on-time)
  - `CarrierDelay` - Carrier issues
  - `WeatherDelay` - Weather
  - `NASDelay` - Air traffic control
  - `SecurityDelay` - Security
  - `LateAircraftDelay` - Previous flight late

---

## Key Metrics Summary

**Overall Stats (2004-2008):**
- Total Flights: 1,592,198
- Cancellation Rate: 1.22%
- On-Time Performance: 78.25%
- Average Delay: 8.3 minutes

**Airport Comparison:**
- MCO Departures: 521,651 (OTP: 78.88%)
- MIA Departures: 283,825 (OTP: 74.03%)

---

## Notes

- **2008 data is partial** - Only January through April 2008 (4 months)
- All delay times are in minutes
- Negative delay = flight was early
- Times in HHMM format (e.g., 1625 = 4:25 PM, 0800 = 8:00 AM)
- Missing values exist for cancelled/diverted flights

---

## Usage Example

```python
import pandas as pd

# Load cleaned data
df = pd.read_csv('../data/processed/mco_mia_clean.csv.gz')

# Filter for MCO departures in summer
mco_summer = df[(df['Origin'] == 'MCO') & (df['Season'] == 'Summer')]

# Get average delay by time of day
delay_by_time = df.groupby('TimeOfDay')['ArrDelay'].mean()
```
