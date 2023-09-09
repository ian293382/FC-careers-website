from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text

app = Flask(__name__)

def load_jobs_from_db():
  with engine.connect() as connection:
      result = connection.execute(text("select * from jobs"))

      jobs = []
      for row in result.all():
          jobs.append(dict(row))
      return jobs


@app.route("/")
def hello_jovian():
    jobs = load_jobs_from_db()
    return render_template('home.html',
                            jobs=jobs,
                            company_name='Jovian'
                          )
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(port="8081", debug=True)