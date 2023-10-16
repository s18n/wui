import boto3


class Client():
  def __init__(self):
    self.session = boto3.session.Session(profile_name='m30ent-root')
    self.dynamodb = self.session.client('dynamodb')
    self.get_tables()
    self.get_recovery_points()


  def get_tables(self):
    tables_dict = {}
    list_tables = self.dynamodb.list_tables()

    for t in list_tables["TableNames"]:
      tables_dict[t] = {}
    
    self.tables = tables_dict
  

  def get_recovery_points(self):
    for t in self.tables:
      recovery_point_data = self.dynamodb.list_backups(TableName=t)
      self.tables[t] = recovery_point_data