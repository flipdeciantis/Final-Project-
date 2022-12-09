# this is the "web_app/routes/unemployment_routes.py" file...

from flask import Blueprint, request, render_template, redirect, flash

from app.project import fetch_GDP_data, format_pct, fetch_RS_data

project_routes = Blueprint("project_routes", __name__)


@project_routes.route("/project/dashboard")
def project_dashboard():
    print("PROJECT DASHBOARD...")

    try:
        data = fetch_GDP_data()
        latest = data[0]
        latest_rate_pct = (float(latest["value"]))
        latest_date = latest["date"]

        #flash("Fetched Latest GDP Data!", "success")
        return render_template("project_dashboard.html",
            latest_rate_pct=latest_rate_pct,
            latest_date=latest_date,
            data=data
        )
    except Exception as err:
        print('OOPS', err)
        breakpoint()
        #flash("GDP Data Error. Please try again!", "danger")
        return redirect("/")

#
# API ROUTES
#

@project_routes.route("/api/project.json")
def GDP_api():
    print("GDP DATA (API)...")

    try:
        data = fetch_GDP_data()
        return data
    except Exception as err:
        print('OOPS', err)
        return {"message":"Unemployment Data Error. Please try again."}, 404