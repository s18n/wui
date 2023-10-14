from google_search import GoogleSearchClient
from textual import on
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import OptionList, Footer, Header, Input, Static
from textual.widgets.option_list import Option, Separator


# Google search config
api_key = "AIzaSyDcqqHbZXp6TRxcgyphlSJaimWrdqIMwEg"
cse_id = "9768910b5866b414d"
search_client = GoogleSearchClient(api_key, cse_id)

class SearchBarWidget(Static):
  """A search bar widget."""

  def compose(self) -> ComposeResult:
    yield Input(
      placeholder="Type your query here...", id="search_field"
    )
    yield OptionList(id="result_list")

  @on(Input.Submitted)
  def search(self):
    results_list = self.query_one("#result_list", OptionList)
    results_list.clear_options()

    input = self.query_one(Input)
    query = input.value
    search_results = search_client.search_google(query)

    for result in search_results:
      title = Option(result["title"], disabled=True)
      link = Option(result["link"])
      results_list.add_option(title)
      results_list.add_option(link)
      results_list.add_option(Separator())
      
    input.value = ""


class TerminalWebSearch(App):
  """A TUI for searching Google."""
  CSS_PATH = "wui.css"

  def compose(self) -> ComposeResult:
    yield Header()
    yield Footer()

    with Container():
      yield SearchBarWidget()

if __name__ == "__main__":
    app = TerminalWebSearch()
    app.run()