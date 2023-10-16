from textual import on
from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import Tree, Header, Footer, Static
from dynamodb import Client
import boto3


session = boto3.session.Session(profile_name='di-audit')
dynamodb = Client(session)


class DatabaseTree(Static):

  def compose(self) -> ComposeResult:
    table_tree = {}

    tree: Tree[dict] = Tree("Tables")
    tree.show_root = not tree.show_root
    tree.root.expand()
    
    for t in dynamodb.tables:
      table_tree[t] = tree.root.add(t, expand=True)

    yield tree



class DynamoRecovery(App):

  CSS_PATH = "./dynamoRecovery.css"

  def compose(self):
    yield Header(show_clock=True)
    yield Footer()
    with ScrollableContainer(id="navigation"):
      yield DatabaseTree()
    self.dark = not self.dark


if __name__ == "__main__":
  DynamoRecovery().run()