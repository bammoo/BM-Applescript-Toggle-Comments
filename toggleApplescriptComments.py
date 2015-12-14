import sublime, sublime_plugin
import re

class toggleApplescriptCommentsCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view = self.view

    for region in view.sel():
      for line_r in reversed(view.lines(region)):
        line_start = line_r.begin()
        text = view.substr(line_r)
        m = re.compile(r'^\s*(--)')
        matched = m.match(text)
        # Already start with --
        if matched:
          view.replace(edit, sublime.Region(line_start + matched.start(1), line_start + matched.end(1)), '')
        else:
          search_first_none_space_character = re.compile(r'^\s*(.*)$')
          matched = search_first_none_space_character.match(text)
          first_text_pos = matched.start(1)
          toggle_pos = line_start + first_text_pos
          view.insert(edit, toggle_pos, '--')