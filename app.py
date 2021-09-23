"""
    API REST Oil & Gas
"""
from flask import Flask, jsonify, request
import db_controller

app = Flask(__name__)


@app.route('/data/', methods=["GET"])
def get_annual_report():
    well = request.args.get("well")
    if well:
        annual_report = db_controller.get_annual_report_by_id(well)
        return jsonify({
        "oil": annual_report[0],
        "gas": annual_report[1],
        "brine": annual_report[2],
    })
    else:  
        annual_report = db_controller.get_annual_report()
        return jsonify(annual_report)


@app.route("/data/<well>", methods=["GET"])
def get_annual_report_by_id(well):
    annual_report = db_controller.get_annual_report_by_id(well)
    print(annual_report[1])

    return jsonify({
        "oil": annual_report[0],
        "gas": annual_report[1],
        "brine": annual_report[2],
    })


if __name__ == "__main__":
    """
    Here you can change debug and port
    Remember that, in order to make this API functional, you must set debug in False
    """
    app.run(host='127.0.0.1', port=8080, debug=True)