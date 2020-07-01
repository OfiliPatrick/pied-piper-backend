from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import math

app = Flask(__name__)
CORS(app)

@app.route('/', methods=["GET"])
def start():
    return "<h1>Flask is running </h1>"
    # return jsonify('flask is running')
   
@app.route('/api/results', methods=["POST"])
def results():
   
    # req_data = request.get_json()
    # # Internal Diameter  (using continuity  equation)
    # Q = flowRate = float(req_data["flowRate"])
    # p = density = float(req_data["density"])
    # u= viscosity = float(req_data["viscosity"])
    # V = pumpDischarge = float(req_data["pumpDischarge"])
    # E = roughness = float(req_data["roughness"])
    # docText = req_data['docText']
    # pi = math.pi

    # #Internal diameter
    # D = internal_diameter = math.sqrt((4 * Q) / (pi * V)) * 1000
    # #get next available diameter and then calculate new V but for now continue
    # # D = 0.2032
    # V = 2.571
    # A = area = ((pi) * ((D / 2) ** 2)) / 1000000
    # Re = reynolds_number = ((D * V * p) / u) /1000
   
    # #FlowType
    # flowType = ""
    # if Re < 2000:
    #     flowType = "LAMINAR"
    # if Re > 4000:
    #     flowType = "TURBULENT"

    # if 2000 < Re < 4000:
    #     flowType = "TRANSIENT"

    # #Relative Roughness
    # relative_roughness = E / D

    # # return {
    # #     "internal_diameter": str(internal_diameter),
    # #     "area": str(area),
    # #     "reynolds_number": str(reynolds_number),
    # #     "flow_type": flowType,
    # #     "relative_roughness": str(relative_roughness),
    # #     "docText": docText
        
    # # }

    
    return {'ok' :  '200'}        
   

if __name__ == '__main__':
    app.run(debug = True, port = 5000)









# dataDict = json.loads(data2)
# print(dataDict)
# print(data['schedule'])
 # print(request.data)
 