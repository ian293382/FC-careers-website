from sqlalchemy import create_engine, text
from dotenv import load_dotenv
load_dotenv()
import os

# "mysql+pymysql://2yze6advjx083prsxef1:pscale_pw_HzDUxzP5anqUVPhPQyhC5bvN0OIGnl16iyEwfRlNTSc@gcp.connect.psdb.cloud/joviancareers?charset=utf8mb4"

db_connection_string = os.environ['DB_CONNECTION_STR']
ssl_args = {'ssl_ca': "/etc/ssl/cert.pem"}

engine = create_engine(
    db_connection_string,
    connect_args=ssl_args)

def load_jobs_from_db():
    with engine.connect() as connection:
      result = connection.execute(text("select * from jobs"))

    jobs = []
    for row in result.all():
        jobs.append(dict(row))
    return jobs

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM jobs WHERE id = :val"),
            val=id
        )
        rows = result.all()
        if len(rows) == 0:
            return None
        else:
            return dict(rows[0])

    # print("type(result):",type(result))
    # result_all = result.all()
    # print("type(result.all()):",type(result.all()))
    # print("result.all():",result.all()) #list
    # first_result = result_all[0]

    # print("type(first_result):", type(first_result))

    ##type(first_result): <class 'sqlalchemy.engine.row.LegacyRow'>

#search how to convert sqlalchemy row into python

    # first_result_dict = dict(result_all[0])

    # print("type(first_result_dict):", type(first_result_dict))
    # print(first_result_dict) #dict
def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")

        conn.execute(query,
                    job_id=job_id,
                    full_name=data['full_name'],
                    email=data['email'],
                    linkedin_url=data['linkedin_url'],
                    education=data['education'],
                    work_experience=data['work_experience'],
                    resume_url=data['resume_url']
                    )