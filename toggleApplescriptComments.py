import sublime
import sublime_plugin
import re


class toggleApplescriptCommentsCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        for region in self.view.sel():
            for line_r in reversed(self.view.lines(region)):
                line_start = line_r.begin()
                text = self.view.substr(line_r).encode('utf-8')
                m = re.compile(r'^\s*(--)')
                matched = m.match(text)

                # Already start with --
                if matched:
                    sl_region = sublime.Region(line_start + matched.start(1),
                                               line_start + matched.end(1))
                    self.view.replace(edit, sl_region, '')
                else:
                    first_none_space_character = re.compile(r'^\s*(.*)$')
                    matched = first_none_space_character.match(text)
                    first_text_pos = matched.start(1)
                    toggle_pos = line_start + first_text_pos
                    self.view.insert(edit, toggle_pos, '--')
