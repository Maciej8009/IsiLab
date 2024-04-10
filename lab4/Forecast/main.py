import matplotlib.pyplot as plt
import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry


# WAZNE!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Prognoza zrobiona jest na 16dni, ze względu na występujące błędy podczas dodawania parametrów "start_date" i "end_date"
#Raz błąd wskazywał na brak możliwości ustawienia "end date" na datę>25.04.2023, a raz po prostu program się wywalał...



weather_codes = {
    0: "czyste niebo",
    1: "głównie bezchmurnie",
    2: "częściowo pochmurno",
    3: "pochmurno",
    45: "mgła",
    48: "opadająca mgła szronowa",
    51: "mżawka lekka",
    53: "mżawka umiarkowana",
    55: "mżawka gęsta",
    56: "zamrażająca mżawka: lekka",
    57: "zamrażająca mżawka: gęsta intensywność",
    61: "deszcz słaby",
    63: "deszcz umiarkowany",
    65: "deszcz intensywny",
    66: "marznący deszcz: intensywność lekka",
    67: "marznący deszcz: intensywność ciężka",
    71: "opady śniegu: intensywność niewielka",
    73: "opady śniegu: intensywność umiarkowana",
    75: "opady śniegu: intensywność duża",
    77: "ziarna śniegu",
    80: "przelotne opady deszczu: słabe",
    81: "przelotne opady deszczu: umiarkowane",
    82: "przelotne opady deszczu: gwałtowne",
    85: "opady śniegu lekkie",
    86: "opady śniegu intensywne",
    95: "burza: Słaba lub umiarkowana",
    96: "burza z lekkim gradem",
    99: "burza z silnym gradem",
}

cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 54.5189,
    "longitude": 18.5319,
    "timezone": "Europe/Berlin",
    "daily": ["weather_code", "temperature_2m_max", "temperature_2m_min", "rain_sum"],
    "forecast_days": 16
}
responses = openmeteo.weather_api(url, params=params)
response = responses[0]

daily = response.Daily()
daily_weather_code = daily.Variables(0).ValuesAsNumpy()
daily_Maxtemp = daily.Variables(1).ValuesAsNumpy()
daily_Mintemp = daily.Variables(2).ValuesAsNumpy()
daily_Rain = daily.Variables(3).ValuesAsNumpy()

weatherType = []
for x in daily_weather_code:
    weatherType.append(weather_codes[x])

daily_data = {"date": pd.date_range(
    start=pd.to_datetime(daily.Time()+7200, unit="s"),
    end=pd.to_datetime(daily.TimeEnd(), unit="s"),
    freq=pd.Timedelta(seconds=daily.Interval()),
    inclusive="left"
), "Typ Pogody?": weatherType, "Najwyższa Temperatura": daily_Maxtemp, "Najniższa Temperatura": daily_Mintemp, "Opady(mm)": daily_Rain}


daily_dataframe = pd.DataFrame(data=daily_data)
pd.set_option('display.max_columns', None)
daily_dataframe.to_csv("weather_data.csv", index=False)
print(daily_dataframe)

plt.figure(figsize=(11, 11))
plt.bar(daily_dataframe["date"], daily_Maxtemp)
plt.xticks(daily_dataframe["date"])
plt.title("Temperature")
plt.ylabel("Degree Celsius")
plt.xlabel("Day")
plt.xticks(rotation=90)
plt.autoscale()
plt.savefig("Forecast.png")
plt.show()

