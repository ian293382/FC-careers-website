from sqlalchemy import create_engine, text

# "mysql+pymysql://2yze6advjx083prsxef1:pscale_pw_HzDUxzP5anqUVPhPQyhC5bvN0OIGnl16iyEwfRlNTSc@gcp.connect.psdb.cloud/joviancareers?charset=utf8mb4"
db_connection_string = "mysql+pymysql://zbc024f8fu7wv0i4ea40:pscale_pw_pBslINK2d529o27QJFvWrX12JauRTbnTE0mbck4Qle8@gcp.connect.psdb.cloud/joviancareers?charset=utf8mb4"

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
          "ca": "/etc/ssl/cert.pem"
        }
    })

def load_jobs_from_db():
  with engine.connect() as connection:
      result = connection.execute(text("select * from jobs"))

      jobs = []
      for row in result.all():
          jobs.append(dict(row))
      return jobs

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

