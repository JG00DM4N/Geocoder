import pandas
from geopy.geocoders import ArcGIS
from werkzeug.utils import secure_filename

nom = ArcGIS()

def geocode(file):

    data = pandas.read_csv(file)

    if "Address" in data.columns or "address" in data.columns:
        proper_format = True

        try:
            for address in data["Address"]:
                data.at[data.Address[data.Address == address].index.tolist()[0], "Latitude"] = nom.geocode(address).latitude
                data.at[data.Address[data.Address == address].index.tolist()[0], "Longitude"] = nom.geocode(address).longitude

        except:
            for address in data["address"]:
                data.at[data.address[data.address == address].index.tolist()[0], "Latitude"] = nom.geocode(address).latitude
                data.at[data.address[data.address == address].index.tolist()[0], "Longitude"] = nom.geocode(address).longitude

        sfn = secure_filename("geocoded_"+file.filename)
        data.to_csv("uploaded/"+sfn, header=True, index=False)

    else:
        proper_format = False


    return (proper_format, data)
