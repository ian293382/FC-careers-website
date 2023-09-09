from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://2yze6advjx083prsxef1:pscale_pw_HzDUxzP5anqUVPhPQyhC5bvN0OIGnl16iyEwfRlNTSc@gcp.connect.psdb.cloud/joviancareers?charset=utf8mb4"


engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
          "ca": "/etc/ssl/cert.pem"
        }
    })

with engine.connect() as connection:
    result = connection.execute(text("select * from jobs"))

    result_dicts = []
    for row in result.all():
        result_dicts.append(dict(row))
    print(result_dicts)

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

