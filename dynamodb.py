import boto3


class Client():
  def __init__(self):
    self.session = boto3.session.Session(profile_name='m30ent-root', region_name='eu-west-2')
    self.dynamodb = self.session.client('dynamodb')
    self.get_tables()
    self.get_recovery_points()


  def get_tables(self):
    tables_dict = {}
    tables = self.dynamodb.list_tables()

    for t in tables["TableNames"]:
      table_data = self.dynamodb.describe_table(TableName=t)
      tables_dict[t] = {}
      tables_dict[t]["ARN"] = table_data["Table"]["TableArn"]
      tables_dict[t]["ID"] = table_data["Table"]["TableId"]
    
    self.tables = tables_dict
  

  def get_recovery_points(self):
    for t in self.tables:
      recovery_point_data = self.dynamodb.list_backups(TableName=t)
      self.tables[t]["BackupSummaries"] = recovery_point_data["BackupSummaries"]