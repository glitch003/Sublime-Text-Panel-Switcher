import sublime
import sublime_plugin


class PanelSwitchCommand(sublime_plugin.WindowCommand):
  def __init__(self, window):
        super().__init__(window)
        self.previous_active_group = None
        self.is_panel_focused = False

  def run(self):
    terminus = self.window.find_output_panel("Terminus")

    self.previous_active_group = self.window.active_group()


    if terminus == None:
      self.window.run_command('toggle_terminus_panel')

    if self.is_panel_focused == True:
      # terminus is already focused.  switch back to editor
      if self.previous_active_group != None:
        self.window.focus_group(self.previous_active_group)
        self.previous_active_group = None
        self.is_panel_focused = False
    else:
      # focus terminus
      self.window.run_command('show_panel', args={'panel': 'output.Terminus'})
      self.window.focus_view(self.window.find_output_panel("Terminus"))
      self.is_panel_focused = True
