from textual import on
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Header, Footer, Static, Select, Pretty
from dynamodb import Client


class DatabaseSelect(Static):
  def compose(self) -> ComposeResult:
    yield Select((table, table) for table in dynamodb.tables)
    self.pretty = Pretty(None, id="database_detail", classes="box")

  @on(Select.Changed)
  def select_table(self):
    input = self.query_one(Select)
    database_detail = dynamodb.tables[input.value]
    self.pretty.update(database_detail)
    self.mount(self.pretty)


class DynamoRecovery(App):

  CSS_PATH = "./dynamoRecovery.css"

  def compose(self):

    yield Header(show_clock=True)
    yield Footer()
    with Container(id="navigation"):
      yield DatabaseSelect(classes="box")

if __name__ == "__main__":
  dynamodb = Client()
  DynamoRecovery().run()